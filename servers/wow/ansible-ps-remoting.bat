@ECHO OFF
sc.exe config wuauserv start= demand
net start wuauserv
.\Windows6.1-KB2506143-x64.msu
