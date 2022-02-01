LoRTIS: A complete workflow to construct insertion plots from FASTQ sequencing data. Additionally, 10 pre/post processing utilities are provided which compliment transposon insertion analysis such as that performed by the main LoRTIS workflow or similar software such as Bio-Tradis https://github.com/sanger-pathogens/Bio-Tradis.

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

### Shread reads

This takes as input a FASTA file of sequence data from long read sequencing and shreads the reads into short reads, the output file has a .shreaded extension.

<pre>
python3 shred-reads.py long-reads.fasta
</Pre>

## Post-processing

The following examples are based on an insertion plot called <b>a.insert_plot</a>, this should be replaced with your own file name such as the <b>CP009273.1.insert_plot</b> file which results from running the examples.

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

### Reduce the insertion plot
Insertion plots can have any number of insertions and this can make it difficult to compare like-for-like between experiments when there are a significantly different number of mutants. The following script makes a new file called 

<pre>
python3 reduce-insertion-plot.py a.insert_plot 1000 > a.1000.insert_plot
</pre>

### Remove background insertions

Occasionally sequencing data includes reads for transposons which are scattered throughout the genome and may correspond to dead or dying mutants. To clean up this background noise, a script is provided which masks sites where there are fewer than a given threshold of insertions by setting them to zero.

<pre>
python3 remove-background-insertions.py a.insert_plot 3 > a.bgremoved.insert_plot


### Remove insertions after the end of the reference genome

In our experience, the Bio-Tradis software can construct insertion plots which are longer than the reference genome and therefore cannot be loaded into Artemis. We do not find similar problems with our workflow. To overcome this problem a script is provided.

<pre>
python3 remove-insertions-after-end.py a.insert_plot 4631469 > a.corrected.insert_plot
</pre>

### Identify spikes

Sometimes there are sites in the insertion plot with an unusually large numebr of insertions. Moreover, a number of those sites with a large number of insertions may be contigous to one another and form part of a larger 'spike'. To identify these spikes, a script is provided which lists the spikes in CSV format which is suitable for loading into a spreadsheet package.

<pre>
python3 spikes.py a.insert_plot
</pre>

