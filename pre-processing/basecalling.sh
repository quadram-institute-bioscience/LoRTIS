# This will connect to the HPC, do basecalling and copy the result over
mkdir Mark-Webber
sudo mount.cifs //smb.qib-hpc-data.ciscloud/research-groups/Mark-Webber Mark-Webber -o domain=nr4,user=lott,uid=$(id -u),gid=$(id -g)

date

wget https://europe.oxfordnanoportal.com/software/analysis/ont-guppy_3.5.1_linux64.tar.gz
tar -xvf ont-guppy_3.5.1_linux64.tar.gz


mkdir Mark-Webber/Tradis/SequencingData/NanoTraDIS/Biotin_Nanotradis_130820/fastq_pass_hac2/
date

dirs=($(find "Mark-Webber/Tradis/SequencingData/NanoTraDIS/Biotin_Nanotradis_130820/fast5_pass/" -type d))

date
for dir in "${dirs[@]}"; do
  ./ont-guppy/bin/guppy_basecaller -c ont-guppy/data/dna_r9.4.1_450bps_hac.cfg -i $dir -s Mark-Webber/Tradis/SequencingData/NanoTraDIS/Biotin_Nanotradis_130820/fastq_pass_hac2/ -x 'auto'
done


echo "Finished BaseCalling"
date

cat Mark-Webber/Tradis/SequencingData/NanoTraDIS/Biotin_Nanotradis_130820/fastq_pass_hac2/*.fastq > all.fastq
