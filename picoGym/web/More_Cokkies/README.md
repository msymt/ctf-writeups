# More Cookies

AUTHOR: MADSTACKS

## Description

I forgot Cookies can Be modified Client-side, so now I decided to encrypt them!

## writeup

EditThisCokkieからCokkieを見ると

```bash
auth_name: bHE3Skphcjhpb0VNUFdjOWdsYnVrQ01NbXJrL3pRa1FuWmVENnF4SzMwWlB1OXU1UFFBNFd4d3NRc0VRZ0ttOE1CdWwvdktIK0JJdExFeVpvWWhFeTFFLzNobzdOdWNibUhBMk5MMjJhWVJCRjhqcVpuYzgwZWtVSWtMVzFWbmM=
name: admin
```

となっている．base64でdecodeすると`lq7JJar8ioEMPWc9glbukCMMmrk/zQkQnZeD6qxK30ZPu9u5PQA4WxwsQsEQgKm8MBul/vKH+BItLEyZoYhEy1E/3ho7NucbmHA2NL22aYRBF8jqZnc80ekUIkLW1Vnc`が得られる．

(ここから[こちら](https://tech.kusuwada.com/entry/2021/04/08/121028)を見て解きました．)

ここで，ヒントと問題文からCBCが見えたため，CBCのbitflipを使う．

base64ということで候補値は64個(アルファベットの大文字（26文字）と小文字（26文字）、数字（10文字）、「+」「/」の2つの記号)を1つずつflipする．

## FLAG

```bash
picoCTF{cO0ki3s_yum_82f39377}
```

## 参考

- https://tech.kusuwada.com/entry/2021/04/08/121028
- https://docs.abbasmj.com/ctf-writeups/picoctf2021#more-cookies
