# Clean up
set -x
sudo docker ps -a -q | xargs -r sudo docker stop
sudo docker ps -a -q | xargs -r sudo docker rm -fv
sudo docker images -q -f dangling=true | xargs -r sudo docker rmi
