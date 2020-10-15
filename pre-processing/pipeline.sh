# sudo docker build --tag btpp:1.0l .
# sudo docker run --name btpp1l --mount type=bind,source="$(pwd)",target=/data btpp:1.0l

echo "Started DeMultiplexing"
date

# Demultiplex by Nanopore barcode
qcat -f /data/all.fastq -b /data/qcat-out --tsv > /data/qcat-results.csv

echo "Finished DeMultiplexing"

gzip /data/all.fastq
gzip /data/qcat-out/none.fastq

# Now update qcat to look for the transposon and output those results...
#whereis qcat

# Replace the barcodes file in qcat
#python3 --version

#pwd
#ls -l

mv /usr/local/lib/python3.6/dist-packages/qcat/resources/kits/simple_standard.yml /usr/local/lib/python3.6/dist-packages/qcat/resources/kits/simple_standard.old
cp /simple_standard.yml /usr/local/lib/python3.6/dist-packages/qcat/resources/kits/

# The following will eventually be put into a Snakemake pipeline
qcat -f /data/qcat-out/barcode01.fastq -b /data/qcat-out/barcode01 --simple --simple-barcodes standard --tsv > /data/qcat-barcode01.csv
gzip /data/qcat-out/barcode01.fastq

qcat -f /data/qcat-out/barcode04.fastq -b /data/qcat-out/barcode04 --simple --simple-barcodes standard --tsv > /data/qcat-barcode04.csv
gzip /data/qcat-out/barcode04.fastq

qcat -f /data/qcat-out/barcode05.fastq -b /data/qcat-out/barcode05 --simple --simple-barcodes standard --tsv > /data/qcat-barcode05.csv
gzip /data/qcat-out/barcode05.fastq

qcat -f /data/qcat-out/barcode08.fastq -b /data/qcat-out/barcode08 --simple --simple-barcodes standard --tsv > /data/qcat-barcode08.csv
gzip /data/qcat-out/barcode08.fastq

# Reset the qcat configuration
rm /usr/local/lib/python3.6/dist-packages/qcat/resources/kits/simple_standard.yml
mv /usr/local/lib/python3.6/dist-packages/qcat/resources/kits/simple_standard.old /usr/local/lib/python3.6/dist-packages/qcat/resources/kits/simple_standard.yml


FILE=/data/qcat-out/barcode01/transposon_rc.fastq
if test -f "$FILE"; then
    cat /data/qcat-out/barcode01/transposon.fastq /data/qcat-out/barcode01/transposon_rc.fastq > /data/qcat-out/barcode01/barcode01t.fastq
else
    cp /data/qcat-out/barcode01/transposon.fastq /data/qcat-out/barcode01/barcode01t.fastq
fi


FILE=/data/qcat-out/barcode04/transposon_rc.fastq
if test -f "$FILE"; then
    cat /data/qcat-out/barcode04/transposon.fastq /data/qcat-out/barcode04/transposon_rc.fastq > /data/qcat-out/barcode04/barcode04t.fastq
else
    cp /data/qcat-out/barcode04/transposon.fastq /data/qcat-out/barcode04/barcode04t.fastq
fi


FILE=/data/qcat-out/barcode05/transposon_rc.fastq
if test -f "$FILE"; then
    cat /data/qcat-out/barcode05/transposon.fastq /data/qcat-out/barcode05/transposon_rc.fastq > /data/qcat-out/barcode05/barcode05t.fastq
else
    cp /data/qcat-out/barcode05/transposon.fastq /data/qcat-out/barcode05/barcode05t.fastq
fi


FILE=/data/qcat-out/barcode08/transposon_rc.fastq
if test -f "$FILE"; then
    cat /data/qcat-out/barcode08/transposon.fastq /data/qcat-out/barcode08/transposon_rc.fastq > /data/qcat-out/barcode08/barcode08t.fastq
else
    cp /data/qcat-out/barcode08/transposon.fastq /data/qcat-out/barcode08/barcode08t.fastq
fi


python3 trim-reads.py /data/qcat-out/barcode01/barcode01t.fastq
python3 trim-reads.py /data/qcat-out/barcode04/barcode04t.fastq
python3 trim-reads.py /data/qcat-out/barcode05/barcode05t.fastq
python3 trim-reads.py /data/qcat-out/barcode08/barcode08t.fastq


# Echo all of the file names in here and then run BioTradis once...
printf "/work/qcat-out/barcode01/barcode01tt.fa\n/work/qcat-out/barcode04/barcode04tt.fa\n/work/qcat-out/barcode05/barcode05tt.fa\n/work/qcat-out/barcode08/barcode08tt.fa" > /data/input-files.txt

# Now everything is in place to run BioTradis on the input files..
