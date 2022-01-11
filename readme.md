A complete workflow from Nanopore sequencing fast5 files through to Tradis plot files.


# 1. Basecalling
Run basecalling.sh. Downloads and runs guppy, takes a day or two for a typical Nanopore dataset.

# 2. Demultiplex and trim the reads
Run the preprocessing docker image (qcat, trim/flip reads)
<b>Note: This typically takes 5-10 hours, most of this time is used by qcat</b>

# 3. Bio-Tradis with Minimap2

## 3.1. Short reads
<pre>
sudo docker login
sudo docker build --tag lortis:1.0 .
sudo docker tag lortis:1.0 martinclott/lortis:latest
sudo docker push martinclott/lortis:latest
sudo docker run --name lotris1 --mount source=excapevol,target=/data martinclott/lortis:latest
</pre>


sudo docker run --rm -v $PWD:/source -v lortisvol:/data -w /source alpine cp reference.fasta short-reads.fq.gz /data
sudo docker run --name lotris6 --mount source=lortisvol,target=/data martinclott/lortis:latest

short-reads.fq.gz

reference.fasta

sudo singularity build lortis.sif Singularity.def

singularity run lortis.sif




# 4. Explore the results
Check plot files are correct, change the format e.g. second number is negative, launch Artemis, identify spikes and operons. Combine plot files e.g. different barcodes. Remove background noise (sites with 1 insertion set to 0).

reduce-insertion-plot.py takes as input an insertion plot and the number of insertions that you would like to keep and makes a new plot file with .reduced on the end of the name
