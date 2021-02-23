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

It is necessary that the columns corresponding for each sample info, contain the strings: "GType", "B Allele Freq", "Log R Ratio"

### How to generate input file

For Illumina-SNP arrays the input file can be generated using the Genome Studio software ([link](https://www.illumina.com/techniques/microarrays/array-data-analysis-experimental-design/genomestudio.html)).

Here there is a tutorial about how to prepare a Genome Studio project: <https://www.youtube.com/embed/s23379Gya0Y?autoplay=1&rel=0>

Once that the project is setup and the call rates have been generated, next select the columns necessary for this script and export those in a text file. Here is a tutorial that describe how to select the columns: [link](http://penncnv.openbioinformatics.org/en/latest/user-guide/input/#preparing-input-signal-intensity-files-from-beadstudio-project-files)

