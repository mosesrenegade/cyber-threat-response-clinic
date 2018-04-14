Step 1 - Get on Jumphost
Step 2 - Open Putty - Kali
Step 3 - Kali run this command:

     sudo apt update -y && sudo apt dist-upgrade -y && sudo apt install bloodhound -y && sudo apt autoremove -y && sudo reboot

Step 4 - On kali once back in run this:
     cd /opt/empire
     git pull
     cd setup
     ./install.sh
     
Step 4 - Back on Jumphost open putty
Step 5 - Save the following session:
     198.18.133.5
     Name: Infra.attack.com



Step 0 - Add infra.attacker.com to Putty Session on main Jumphost
Step 0a - 

Step 1 - Add new DNS Pointer to 'safe' biomedical DNS which points to 'Load Balancer' simulating Domain Fronting

Step 2 - Add new Front Page for the SPA for biomed domain called www.happybio.com

Step 3 - Add new DNS Pointer to CloudLB called lb.publiccloud.co
Step 4 - Build certs that are trusted for *.publiccloud.co make it trusted across all systems
:

Install Node.JS
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install -y build-essential
Install Electron
sudo npm install -g electron-packager

