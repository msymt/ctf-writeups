# GET aHEAD

AUTHOR: MADSTACKS

## Description

Find the flag being held on this server to get ahead of the competition

## writeup

GETメソッドデRED，POSTメソッドでBLUEの画面へと遷移している．
タイトルの通り，HEADメソッドを呼び出せば良いと判断する．

```bash
curl --head http://mercury.picoctf.net:53554
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_2e5ba39f}
Content-type: text/html; charset=UTF-8
```

## FLAG

```bash
picoCTF{r3j3ct_th3_du4l1ty_2e5ba39f}
```
