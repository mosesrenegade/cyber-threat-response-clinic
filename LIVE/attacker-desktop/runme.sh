#!/usr/bin/env bash

# Make kali is fixed
wget https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2018.1_all.deb
dpkg -i kali-archive-keyring_2018.1_all.deb
     
sudo apt update -y && sudo apt dist-upgrade -y && sudo apt install bloodhound -y && sudo apt autoremove -y

cd /opt/empire
git pull
cd /opt/empire/setup/
./install.sh
./reset.sh

#Now for the manual crap!

cd /opt/empire
wget https://github.com/mosesrenegade/cyber-threat-response-clinic/tree/master/LIVE/attacker-desktop/empire.rc
./empire -r empire.rc


echo "CTR-3.1" > /etc/ctr-version

echo "Perform the following steps"
echo "cd /opt/empire"
echo "./empire"
echo "Once empire loads you need to create a http listener and a stager that is launcher_bat"
echo "move this over to http://198.18.133.5/files/launcher.bat"
echo "Sorry I can't automate this"
echo "exeucte the following" 
