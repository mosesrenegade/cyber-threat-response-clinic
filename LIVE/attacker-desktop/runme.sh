#!/usr/bin/env bash

# Make kali is fixed
wget https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2018.1_all.deb
dpkg -i kali-archive-keyring_2018.1_all.deb
     
sudo apt update -y && sudo apt dist-upgrade -y && sudo apt install bloodhound -y && sudo apt autoremove -y

#Shut Down nginx
sudo systemctl disable nginx
sudo service nginx stop

#Empire
cd /opt/empire
git pull
cd /opt/empire/setup/
./install.sh
./reset.sh

#Make me a stager
cd /opt/empire
wget https://github.com/mosesrenegade/cyber-threat-response-clinic/tree/master/LIVE/attacker-desktop/empire.rc
mv empire.rc /tmp
./empire -r /tmp/empire.rc

#Finish up
echo "CTR-3.1" > /etc/ctr-version

#Addtl notes
echo "Perform the following steps"
echo "cd /opt/empire"
echo "./empire"
echo "Once empire loads you need to create a http listener and a stager that is launcher_bat"
echo "move this over to http://198.18.133.5/files/launcher.bat"
echo "Sorry I can't automate this"
echo "exeucte the following" 
