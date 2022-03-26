# Windows memory dump2

## Description

250

Using the memory dump file from Window memory dump challenge, submit the infected computer name as the flag.

Submit the flag as OFPPT-CTF{COMPUTER-NAME}.

## writeup

userinit.exeをメモリダンプし、stringsしたところ、Jimmieというユーザーが感染していることがわかりました。
COMPUTER-NAMEということから、DESKTOP-hogeのような形式だと思い、調べると`COMPUTERNAME=DESKTOP-IT8QNRI`が出てきました。

```bash
$ python2 vol.py -f physmemraw --profile=Win10x64_19041 memdump -D . -p 8180
$ strings 8180.dmp > 8180.txt
ALLUSERSPROFILE=C:\ProgramData
USERPROFILE=C:\Users\Jimmie
COMPUTERNAME=DESKTOP-IT8QNRI
USERDOMAIN=DESKTOP-IT8QNRI
```

## FLAG

```bash
OFPPT-CTF{DESKTOP-IT8QNRI}
```
