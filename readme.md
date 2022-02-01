LoRTIS: A complete workflow from Nanopore sequencing FAST5 files, or Illumina short read FASTQ files, through to Tradis insertion 
plot files.


# Prerequiste: Download the repository

<pre>
git clone https://github.com/quadram-institute-bioscience/LoRTIS/
</pre>

# Main workflow

## Example 1: Long read FASTQ data to transposon insertion plot.
<pre>
cd example
sh long-reads.sh
# Finally load the example.embl into Artemis and add user plot
</pre>

This uses gzipped long read data in fastq format in a file called <b>long-reads.fq.gz</b>. Additionally, a reference genome in fasta format called <b>reference.fasta</b> is used to map the reads to. This example script will copy the input files into a Docker volume, run the workflow and then copy the results out into a directory called <b>results-lr</b>.

The results can be viewed in Artemis with <b>File > Open</b> then select the reference.embl. Next, go to <b>Graph > Add User Plot</b> and select the relevant <b>.insert_plot</b> file. Right clicking on the plot and selecting <b>scaling</b> allows more easy inspection of the insertions.

## Example 2: Short read FASTQ data to transposon insertion plot.
<pre>
cd example
sh short-reads.sh
# Finally load the example.embl into Artemis and add user plot
</pre>

The workflow proceeds as in example 1 but short read mapping software is used.


# Optional Utilities

This is a collection of additional scripts which aid in the processing of data before and after the main workflow.

## Pre-processing

### Shuffle reads

Where a subset of reads is required, for example to perform a like-for-like comparison between experiments, the shuffle-reads.py script can assist. For example, to obtain a random subset of 10,000 reads from a fastq file, the following command can be performed.

<pre>
python3 shuffle-reads.py all-reads.fastq 10000 > all-reads.10000.fastq
</pre>


## Post-processing

The following examples are based on an insertion plot called <b>a.insert_plot</a>, this should be replaced with your own file name such as <b>CP009273.1.insert_plot</b> which results from running the examples.

### Change sign of insertions on the reverse strand of an insertion plot

This changes the sign of the insertions on the reverse stran in an insertion plot from positive to negative. Consequently, the insertions on the negative strand are shown below the x axis in Artemis which makes them more distinguishable from those on the positive strand.

<pre>
python3 change-plot.py a.insert_plot > another.insert_plot
</pre>


### Combine insertion plots

This takes as input two insertion plot files and creates a new plot file in which each site has the sum total of the insertions in the input plot files.

<pre>
python3 combine-plot-files.py a.insert_plot b.insert_plot > ab.insert_plot
</pre>

### List non-empty sites

This takes as input an insertion plot and lists all sites which do not have any insertions.

<pre>
python3 list-non-empty-sites.py a.insert_plot
</pre>


### Find operons

Often genes, exist as part of operons rather than individually, this script is designed to identifies such groups of genes.

<pre>
python3 operons.py reference.embl > operons.txt
</pre>


# 4. Explore the results
Check plot files are correct, change the format e.g. second number is negative, launch Artemis, identify spikes and operons. Combine plot files e.g. different barcodes. Remove background noise (sites with 1 insertion set to 0).

reduce-insertion-plot.py takes as input an insertion plot and the number of insertions that you would like to keep and makes a new plot file with .reduced on the end of the name
