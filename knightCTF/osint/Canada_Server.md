# Canada Server

## description

50

Our sponsor NS TechValley had some problems last year. Their Canada server was not working as expected. Can you find the IP address of that server?

Flag Format : KCTF{IP_Address_Here}

Example Flag : KCTF{127.0.0.1}

Author : NomanProdhan

## writeup

NS TechValley社のドメインを調べて、pingを送ってみると出ました。

```bash
 % ping nstechvalley.com
PING nstechvalley.com (192.99.167.83): 56 data bytes
64 bytes from 192.99.167.83: icmp_seq=0 ttl=50 time=176.172 ms
64 bytes from 192.99.167.83: icmp_seq=1 ttl=50 time=173.513 ms
```

## FLAG

```txt
KCTF{192.99.167.83}
```
