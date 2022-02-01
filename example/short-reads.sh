sudo docker run --rm -v $PWD:/source -v lortisvol:/data -w /source alpine rm -R /data
sudo docker run --rm -v $PWD:/source -v lortisvol:/data -w /source alpine cp reference.* short-reads.fq.gz /data
sudo docker run --name lotrissr --mount source=lortisvol,target=/data martinclott/lortis:latest
sudo docker run --rm -v $PWD:/source -v lortisvol:/data -w /source alpine cp -R /data ./results-sr
