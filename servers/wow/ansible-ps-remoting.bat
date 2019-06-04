@ECHO OFF
sc.exe config wuauserv start= demand
net start wuauserv
.\Win7AndW2K8R2-KB3191566-x64.msu
