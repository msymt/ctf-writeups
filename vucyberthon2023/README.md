# VU CYBERTHON 2023 <!-- omit in toc -->

forensicが多めでした．配布ファイルがクソデカすぎて，ダウンロードにめちゃくちゃ時間を要しました．
自宅の回線は平凡でこの有様だったので，他にも同じような人がいたんじゃないかと思います．

点数と難易度は釣り合っていないと思います．

https://2023.cyberthon.lt/


- [Digital Forensics/What is SHA1 checksum of image file blk0\_mmcblk0.bin ?: 10 points](#digital-forensicswhat-is-sha1-checksum-of-image-file-blk0_mmcblk0bin--10-points)
- [Crypto/Weak Password: 10 points](#cryptoweak-password-10-points)
- [Network-Security/Blue-Baby-Shark](#network-securityblue-baby-shark)
- [OSINT/Find Location: 15 points](#osintfind-location-15-points)
- [Rev/Reverse ME: 50points](#revreverse-me-50points)


## Digital Forensics/What is SHA1 checksum of image file blk0_mmcblk0.bin ?: 10 points

Extract the archive file blk0_mmcblk0.7z. What is SHA1 checksum of the image?...

binファイルのsha-1ハッシュ値がフラグ

配布ファイル：`イメージファイル.7z`

### SOLUTION <!-- omit in toc -->

7zで圧縮されていたので，7zipで解凍しました．
あとは，sha-1ハッシュ値を求めるだけです．

```bash
# windows
cerutil -hashfile ./blk0_mmcblk0.bin
5377521a476be72837053390b24bc167d8f9182c
```

### FLAG <!-- omit in toc -->

```
VU{5377521a476be72837053390b24bc167d8f9182c}
```

## Crypto/Weak Password: 10 points

Such a password is recognized as one of the weakest passwords in the country that organizes VU Cybe..(省略)

### SOLUTION <!-- omit in toc -->

[この記事](https://lonesec.com/2021/12/07/zip_password_security/)を参考に，John the ripperを実行すると，30分ほどでパスワードを特定しました．

```bash
./zip2john ./taskweakpassword.zip > ./taskweakpassword.zip.hash
 ./john --incremental=ASCII ./taskweakpassword.zip.hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
Kaunas           (taskweakpassword.zip/taskweakpassword/about.txt)
1g 0:00:47:49 DONE (2023-02-25 21:04) 0.000348g/s 8688Kp/s 8688Kc/s 8688KC/s Kaundn..Kaunee
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

./taskweakpassword/about.txtには，以下の内容が書かれていました．

```txt
You can read about it in the research conducted (translated article):
https://www-delfi-lt.translate.goog/mokslas/technologijos/paskelbe-20-populiariausiu-slaptazodziu-lietuvoje-ar-jusiskis-sarase.d?id=86533765&_x_tr_sl=lt&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp

Your
Cyberthon Team
https://www.cyberthon.lt
```

以上から，パスワードがフラグだと思い入力すると，その通りでした．

### FLAG <!-- omit in toc -->

```
VU{Kaunas}
```
## Network-Security/Blue-Baby-Shark

> I got recomendation from one of our common acquaintance. I’m a new into all of this CTF stuff. I g...

配布ファイル：pcapファイル

### SOLTION <!-- omit in toc -->

TCPストリームを眺めていると，Dataが存在するパケットが存在しました．
そこから，Follow TCP Streamをすると，/etc/passwdの中身が送られていました．`vu:x:1337:b4by_5h4rk_fly_4w4y`がフラグでした．

```bash
id
uid=0(root) gid=0(root) groups=0(root)
cat /etc/passwd
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:997:997:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:107::/nonexistent:/usr/sbin/nologin
tss:x:101:109:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:102:65534::/var/lib/strongswan:/usr/sbin/nologin
tcpdump:x:103:110::/nonexistent:/usr/sbin/nologin
usbmux:x:104:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
dnsmasq:x:106:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
avahi:x:107:113:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
speech-dispatcher:x:108:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
pulse:x:109:114:PulseAudio daemon,,,:/run/pulse:/usr/sbin/nologin
saned:x:110:117::/var/lib/saned:/usr/sbin/nologin
lightdm:x:111:118:Light Display Manager:/var/lib/lightdm:/bin/false
polkitd:x:996:996:polkit:/var/lib/polkit-1:/usr/sbin/nologin
rtkit:x:112:119:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:113:120:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
nm-openvpn:x:114:122:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
nm-openconnect:x:115:123:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
mysql:x:116:124:MySQL Server,,,:/nonexistent:/bin/false
stunnel4:x:995:995:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
geoclue:x:118:126::/var/lib/geoclue:/usr/sbin/nologin
vu:x:1337:b4by_5h4rk_fly_4w4y
Debian-snmp:x:119:127::/var/lib/snmp:/bin/false
sslh:x:120:129::/nonexistent:/usr/sbin/nologin
ntpsec:x:121:132::/nonexistent:/usr/sbin/nologin
redsocks:x:122:133::/var/run/redsocks:/usr/sbin/nologin
rwhod:x:123:65534::/var/spool/rwho:/usr/sbin/nologin
iodine:x:124:65534::/run/iodine:/usr/sbin/nologin
miredo:x:125:65534::/var/run/miredo:/usr/sbin/nologin
statd:x:126:65534::/var/lib/nfs:/usr/sbin/nologin
redis:x:127:134::/var/lib/redis:/usr/sbin/nologin
postgres:x:128:135:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
mosquitto:x:129:136::/var/lib/mosquitto:/usr/sbin/nologin
inetsim:x:130:137::/var/lib/inetsim:/usr/sbin/nologin
_gvm:x:131:139::/var/lib/openvas:/usr/sbin/nologin
king-phisher:x:132:140::/var/lib/king-phisher:/usr/sbin/nologin
kali:x:1000:1000:,,,:/home/kali:/usr/bin/zsh
Looks Great!
```

### FLAG <!-- omit in toc -->

```
VU{b4by_5h4rk_fly_4w4y}
```

## OSINT/Find Location: 15 points

[LOCATION](https://vuknf.file.core.windows.net/vucyberthon2023/Location.jpeg?sv=2021-10-04&st=2023-02-20T12%3A21%3A10Z&se=2024-02-21T12%3A21%3A00Z&sr=f&sp=r&sig=8wpC74vfb64zxWKobYWFM48WN9FtIzbW0rhvgSXTCfI%3D)

![](./images/Location.jpeg)

### SOLTION <!-- omit in toc -->

exiftoolを使うだけ．

```bash
ExifTool Version Number         : 12.42
File Name                       : Location.jpeg
Directory                       : .
File Size                       : 253 kB
File Modification Date/Time     : 2023:02:25 21:28:57+09:00
File Access Date/Time           : 2023:02:25 21:29:20+09:00
File Inode Change Date/Time     : 2023:02:25 21:29:14+09:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
XMP Toolkit                     : FILE
Location                        : VU{d5bc0961009b25633293206cde4ca1e0}
...
```

### FLAG <!-- omit in toc -->

```
VU{d5bc0961009b25633293206cde4ca1e0}
```

## Rev/Reverse ME: 50points

（loginとpasswordがそのままフラグになる云々と書かれていました）．

配布ファイル：Task-ReverseME(ELF)

### SOLUTION <!-- omit in toc -->

binjaで配布されたファイルを開くと，標準入力から受け取った値が`0x3f1`かつ`0x62b`のとき，`sucess`関数を呼び出していました．そこでそれぞれ，10進数に変換しました．

```c
000011dd  int32_t main(int32_t argc, char** argv, char** envp)

000011dd  {
000011e9      void* fsbase;
000011e9      int64_t rax = *(int64_t*)((char*)fsbase + 0x28);
000011f8      int32_t var_20 = 0;
000011ff      int32_t var_1c = 0;
00001206      int32_t var_18 = 0x3f1;
0000120d      int32_t var_14 = 0x62b;
00001223      printf("Enter login:");
0000123e      __isoc99_scanf(&data_2058, &var_20);
00001252      printf("Enter password:");
0000126d      __isoc99_scanf(&data_2058, &var_1c);
00001284      if ((0x3f1 != var_20 || (0x3f1 == var_20 && 0x62b != var_1c)))
0000127f      {
00001297          fail();
00001297      }
00001284      if ((0x3f1 == var_20 && 0x62b == var_1c))
0000127f      {
0000128b          success();
0000128b      }
000012a5      *(int64_t*)((char*)fsbase + 0x28);
000012ae      if (rax == *(int64_t*)((char*)fsbase + 0x28))
000012a5      {
000012b6          return 0;
000012b6      }
000012b0      __stack_chk_fail();
000012b0      /* no return */
000012b0  }
```

### FLAG <!-- omit in toc -->

```
VU{1009,1579}
```
