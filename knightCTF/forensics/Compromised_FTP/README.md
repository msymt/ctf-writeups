# Compromised FTP

## description

25
We detected some malicious activity on our FTP server. Someone has performed bruteforce attack to gain access to our FTP server. Find out the Compromised FTP account username & the attacker IP from the following.

## writeup

ログに大量のFAILがあったため、除外してみました。次に除外したログから成功を表すログがないか調べました。

```bash
Mon Jan  3 15:24:13 2022 [pid 5399] [ftpuser] OK LOGIN: Client "::ffff:192.168.1.7"
```

## FLAG

```txt
KCTF{ftpuser_192.168.1.7}
```
