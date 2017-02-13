./launchwebapp.sh
sudo docker-compose -f /deployment/slm/conf/slmwebapp-compose.yml down
sudo docker-compose -f /deployment/slm/conf/slmwebapp-compose.yml up --force-recreate
