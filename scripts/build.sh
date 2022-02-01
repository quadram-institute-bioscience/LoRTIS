sudo docker login
sudo docker build --tag lortis:1.0 .
sudo docker tag lortis:1.0 martinclott/lortis:latest
sudo docker push martinclott/lortis:latest
sudo docker run --name lotris1 --mount source=lortisvol,target=/data martinclott/lortis:latest
