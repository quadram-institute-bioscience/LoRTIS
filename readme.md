LoRTIS: A complete workflow from Nanopore sequencing FAST5 files, or Illumina short read FASTQ files, through to Tradis insertion 
plot files.


# Prerequiste: Download the repository

<pre>
git clone https://github.com/quadram-institute-bioscience/LoRTIS/
</pre>


# Example 1: Long read FASTQ data to transposon insertion plot.
<pre>
cd example
sh long-reads.sh
</pre>

# Finally run Artemis

# Optional: 1. Basecalling for Nanopore data
This is performed using the Guppy basecaller, an example is provided in <b>pre-processing/basecalling.sh</b>

# Optional: 2. Demultiplex and trim the reads for the transposon
This uses QCat, which has been modified to search for the transposon sequence as listed in <b>simple_standard.yml</b>. The workflow can be run using pipeline.sh

Run the preprocessing docker image (qcat, trim/flip reads)
<b>Note: This typically takes 5-10 hours, most of this time is used by qcat</b>

# 3. Bio-Tradis with Minimap2

## 3.1. Short reads

sudo docker run --rm -v $PWD:/source -v lortisvol:/data -w /source alpine cp reference.fasta short-reads.fq.gz /data
sudo docker run --name lotris6 --mount source=lortisvol,target=/data martinclott/lortis:latest

short-reads.fq.gz

reference.fasta

sudo singularity build lortis.sif Singularity.def

singularity run lortis.sif




# 4. Explore the results
Check plot files are correct, change the format e.g. second number is negative, launch Artemis, identify spikes and operons. Combine plot files e.g. different barcodes. Remove background noise (sites with 1 insertion set to 0).

reduce-insertion-plot.py takes as input an insertion plot and the number of insertions that you would like to keep and makes a new plot file with .reduced on the end of the name
