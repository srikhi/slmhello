# Clean up
set -x
find . -name *.pyc -delete
# sudo docker ps -a -q | xargs -r sudo docker stop
sudo docker ps -a -q | xargs -r sudo docker rm -fv
sudo docker images -q -f dangling=true | xargs -r sudo docker rmi
sudo docker rmi -f slmweb:latest
