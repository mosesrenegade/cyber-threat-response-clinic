@ECHO OFF
sc.exe config wuauserv start= demand
net start wuauserv
.\Win7AndW2K8R2-KB3191566-x64.msu
.\NDP452-KB2901907-x86-x64-AllOS-ENU.exe
net stop wuauserv
sc.exe config wuauserv start= disabled
