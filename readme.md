


# 1. Basecalling
Run basecalling.sh. Downloads and runs guppy, takes a day or two for a typical Nanopore dataset.

# 2. Demultiplex and trim the reads
Run the preprocessing docker image (qcat, trim/flip reads)

# 3. Bio-Tradis with Minimap2
Run the new version of BioTradis with Minimap2

# 4. Explore the results
Check plot files are correct, change the format e.g. second number is negative, launch Artemis, identify spikes and operons
