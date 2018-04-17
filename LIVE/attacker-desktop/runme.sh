#!/usr/bin/env bash

# Make kali is fixed
wget https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2018.1_all.deb
dpkg -i kali-archive-keyring_2018.1_all.deb
     
sudo apt update -y && sudo apt dist-upgrade -y && sudo apt install bloodhound -y && sudo apt autoremove -y

cat "CTR-3.1" > /etc/ctr-version
