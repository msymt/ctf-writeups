# Bad C2

## Description

Not very versatile malware

## writeup

Bad C2ということで、外部サーバと通信し、何かしら実行しようとしてると思いwiresharkを開きました。

POSTメソッドをFollow TCP Streamで調べると`{please: false}`を送った後、`sorry, you didn't say please`との履歴が残ってました。
そこで、trueに変更するとフラグが帰ってくると思い、実行しました。

```
POST /get/secret HTTP/1.1
Host: maliciouspayload.delivery
User-Agent: python-requests/2.21.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
Content-Length: 19
Content-Type: application/json

{"please": "false"}HTTP/1.1 200 OK
Server: Werkzeug/2.1.0 Python/3.8.10
Date: Tue, 29 Mar 2022 23:52:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 28

sorry, you didn't say please
```

```zsh
curl -i -X POST -H "Content-Type: application/json" -d '{ "please": "true"}' http://maliciouspayload.delivery/get/secret
RS{m4gic_word_is_4lw4ys_b31ng_p0lit3}
```

## FLAG

```bash
RS{m4gic_word_is_4lw4ys_b31ng_p0lit3}
```

## メモ

```
GET /get/command HTTP/1.1
Host: maliciouspayload.delivery
User-Agent: python-requests/2.21.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

HTTP/1.1 200 OK
Server: Werkzeug/2.1.0 Python/3.8.10
Date: Tue, 29 Mar 2022 23:52:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 20

execute memecats.dll
```