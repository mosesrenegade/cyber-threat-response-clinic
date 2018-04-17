#/usr/bin/env bash

#Make sure we have nginx and apache and php7
sudo apt update -y && sudo apt install apache2 nginx libapache2-mod-php7.0 -y

#Make a cert and put it into a good place.
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/LIVE/attacker-infra/self-signed-cert-gen.sh
chmod a+x self-signed-cert-gen.sh
sudo ./self-signed-cert-gen.sh

#Replace Apache2 ports
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/LIVE/attacker-infra/ports.conf
sudo mv ports.conf /etc/apache2/ports.conf

#Replace Nginx Default site
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/LIVE/attacker-infra/nginx-cloudfront-config.conf
sudo mv nginx-cloudfront-config.conf /etc/nginx/sites-enabled/default
sudo service nginx restart

#Replace Apache2 Default Site
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/LIVE/attacker-infra/apache-default.conf
sudo mv apache-default.conf /etc/apache2/sites-enabled/000-default
sudo service apache2 restart

