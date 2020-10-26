A complete workflow from Nanopore sequencing fast5 files through to Tradis plot files.


# 1. Basecalling
Run basecalling.sh. Downloads and runs guppy, takes a day or two for a typical Nanopore dataset.

# 2. Demultiplex and trim the reads
Run the preprocessing docker image (qcat, trim/flip reads)
<b>Note: This typically takes 5-10 hours, most of this time is used by qcat</b>

# 3. Bio-Tradis with Minimap2
Run the new version of BioTradis with Minimap2

# 4. Explore the results
Check plot files are correct, change the format e.g. second number is negative, launch Artemis, identify spikes and operons. Combine plot files e.g. different barcodes. Remove background noise (sites with 1 insertion set to 0).
