@ECHO OFF
sc.exe config wuauserv start= demand
net start wuauserv
wusa.exe .\Windows6.1-KB3033929-x64.msu /quiet
wusa.exe .\Win7AndW2K8R2-KB3191566-x64.msu /quiet
.\NDP452-KB2901907-x86-x64-AllOS-ENU.exe /q /norestart
net stop wuauserv
sc.exe config wuauserv start= disabled
