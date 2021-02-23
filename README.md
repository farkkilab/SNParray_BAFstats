# SNParray_BAFstats

Python script for the calculation of BAF stats from SNP array. As input is necessary a table with BAF and LogR per marker.

## Getting started

### Requirements

- Python 3
- Python package: numpy

### Input file

The input file needs to be a text file with information for each sample in each SNP probe. It most contain the next columns first:

- 1) Probe name
- 2) Chromosome name
- 3) Chromosome position

And then for each sample in most contain the colums:

- SampleName.GType
- SampleName.B Allele Freq
- SampleName.Log R Ratio

Example:

```
Name    Chr     Position        Sample_2.GType  Sample_2.B Allele Freq  Sample_2.Log R Ratio    Sample_10.GType Sample_10.B Allele Freq Sample_10.Log R Ratio
rs1566058       8       9626103 AC      0.4652651       -3.241315       AC      0.740777        -4.247029
rs180981568     8       7011720 AC      0.02673887      -2.99316        AC      0.6640925       -5.381115
```

It is necessary that the columns corresponding for each sample info, contain the strings: "GType", "B Allele Freq", "Log R Ratio". You can find an example input file in this repository: `Example_input.txt`.

### How to generate input file

For Illumina-SNP arrays the input file can be generated using the Genome Studio software ([link](https://www.illumina.com/techniques/microarrays/array-data-analysis-experimental-design/genomestudio.html)).

Here there is a tutorial about how to prepare a Genome Studio project: <https://www.youtube.com/embed/s23379Gya0Y?autoplay=1&rel=0>

Once that the project is setup and the call rates have been generated, next select the columns necessary for this script and export those in a text file. Here is a tutorial that describe how to select the columns: [link](http://penncnv.openbioinformatics.org/en/latest/user-guide/input/#preparing-input-signal-intensity-files-from-beadstudio-project-files)


## The script execution

### How to run it

Once that you have generated the input file. Execute the script with the next comand:

`python3 Histograms_BAF.py -i Inputfile.txt -o outputdirectory/`

This is the corresponding usage for the script:

```
Usage: Histograms_BAF.py [options]

Options:
  -h, --help            show this help message and exit
  -i INPUTFILE, --input=INPUTFILE
                        Input file with LogR and BAF values per sample
  -o OUTDIR, --outputdir=OUTDIR
                        Output directory
```

### Running example

You can use as example the `Example_input.txt` and run the script in the next way:

`python3 Histograms_BAF.py -i Example_input.txt -o example_output2`

The files generated in example\_output2/ should be the same as in example\_output/


### Results

Inside the outputdirectory that you selected during the script execution, you will find the files `BAFhistograms.txt` and `logRstats.txt`.

- `logRstats.txt`: This file contain a line for each marker, the first three columns correspond to the probes info (name, chr, position) and the last columns to LogRatios mean, median, 1qt, 3qt and SD.

- `BAFhistograms.txt`: This file contain a line for each marker, the first three columns correspond to the probes info (name, chr, position) and the last columns to the histogram of BAFs
