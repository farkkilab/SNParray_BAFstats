import sys
import numpy as np
from optparse import OptionParser

dirsep="/"

#Defining input arguments
parser = OptionParser()

  
#Add options 
parser.add_option("-i", "--input", 
                  dest = "inputfile", 
                  help = "Input file with LogR and BAF values per sample") 
parser.add_option("-o", "--outputdir", 
                  dest = "outdir", 
                  help = "Output directory") 
  
(options, args) = parser.parse_args()

if (options.inputfile == None): 
        print (parser.usage) 
        exit(0)


#Reading input and creating output files
input_file = open(options.inputfile, "r")
output_BAFfile = open(options.outdir + dirsep + "BAFhistograms.txt", "w+")
output_logRfile = open(options.outdir + dirsep + "logRstats.txt", "w+")


count = 0 
binvalues = np.linspace(0,1,21, dtype=np.float32) #Bins for the histogram


#Reading file
for line in input_file:
    line = line.rstrip("\n")
    line = line.split("\t")
    #Checking header
    if count == 0:
        samples = int((len(line) - 3)/3)
        endposition = int(samples * 3 + 2)
        if "GType"  not in line[3] or "Allele"  not in line[4] or "Log"  not in line[5]:
            sys.exit("""ERROR: Malformatted input file.
            Input file should have the next columns first: Name\tChr\tPosition\tGType""")
        else:
            count += 1
            continue
    #Ignoring chrY and chrX
    if 'Y' in line[1] or 'X' in line[1]:
        continue
    
    #Extracting BAF values and getting histograms
    bafvalues = line[4:endposition:3]
    arrbaf = np.array(bafvalues, dtype=np.float32)
    np_hist = np.histogram(arrbaf, bins=binvalues)
    list_hist = np_hist[0]
    
    #Extracting logR values and doing stats
    logRvalues = line[5:endposition:3]
    arrlogR = np.array(logRvalues, dtype=np.float64)
    logRmean = np.mean(arrlogR)
    logRmedian = np.median(arrlogR)
    logRstd = np.std(arrlogR)
    logRfirstq = np.quantile(arrlogR, 0.25)
    logRfourtq = np.quantile(arrlogR, 0.75)


    #Formating to string and writing to file
    list_hist = [str(x) for x in list_hist]
    joined_string = ",".join(list_hist)

    output_BAFfile.write(line[0] + "," + line[1] + "," + line[2] + "," + joined_string + "\n")
    output_logRfile.write(line[0] + "," + line[1] + "," + line[2] + "," + str(logRmean) + "," + str(logRmedian) + "," + str(logRstd) + "," + str(logRfirstq) + "," + str(logRfourtq) + "\n")

    

    count += 1

print ("Processed {0} markers after skipping X & Y chrs".format(str(count)) )
print ("File generated:" + options.outdir + "BAFhistograms.txt")
print ("File generated:" + options.outdir + "logRstats.txt")

#Closing files
output_BAFfile.close()
output_logRfile.close()
input_file.close()
