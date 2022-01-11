# Get a version of Snakemake
FROM snakemake/snakemake:v5.7.4

# Set the working directory, this lives in the container file system
WORKDIR /usr/src/app

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8080

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

CMD snakemake --use-conda --use-singularity /data/summary-stats.tsv
