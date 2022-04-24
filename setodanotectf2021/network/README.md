# Network

## Host（30）

Hostを目grepしたら見つけました．

```txt
flag{ctf.setodanote.net}
```

## tkys_never_die（50）

`/flag.html`, `/flag.png`があったため，直接アクセスするも404.

Wiresharkの「file -> Exports Objects -> Http」の順でポチポチすると画像ファイルを取得できました．

```txt
flag{a_treasure_trove}
```

## stay_in_touch(150)

Wiresharkの「analyze -> Follow -> TCP stream」を使う．

Stream12でbase64を使ってエンコードしていたので，デコードしてzipに書き込みます．
解凍時にpassを要求されたので，別のstreamを覗くと14にそれらしきものがありました．

stream 12

```
--------------E3A9083942D9027C4375FEE4
Content-Type: application/x-zip-compressed;
 name="Report-AV-T0097.zip"
Content-Transfer-Encoding: base64
Content-Disposition: attachment;
 filename="Report-AV-T0097.zip"

UEsDBBQAAQAAADBq8FK0Nz5zSgAAAD4AAAATAAAAUmVwb3J0LUFWLVQwMDk3LnR4dAzRMzm6
s5vAM3huF0n2GEKFrarxVD3WvzurjKz9sjA7iD6nWis0GBRcIdcyrQkqliocBi2lCUB6J0hR
UgHzDVCnVx6LnLS5LenqUEsBAj8AFAABAAAAMGrwUrQ3PnNKAAAAPgAAABMAJAAAAAAAAAAg
AAAAAAAAAFJlcG9ydC1BVi1UMDA5Ny50eHQKACAAAAAAAAEAGADNWpx++XnXARJtllL6edcB
0TOVfvl51wFQSwUGAAAAAAEAAQBlAAAAewAAAAAA
--------------E3A9083942D9027C4375FEE4--

* 19 EXISTS
* 1 RECENT
13 OK [APPENDUID 1625832838 19] Append completed (0.002 + 0.001 secs).
14 noop
14 OK NOOP completed (0.001 + 0.000 secs).
15 IDLE
+ idling

```

stream 14

```
To: akari <akari@setodanote.net>
From: setoda <setoda@setodanote.net>
Subject: =?UTF-8?B?44OR44K544Ov44O844OJ6YCa55+l?=
Message-ID: <4ffd1fe8-3df8-05cb-b7dc-b698a361736b@setodanote.net>
Date: Thu, 21 Feb 2002 17:20:27 +0900
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101
 Thunderbird/78.11.0
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8; format=flowed
Content-Language: en-US
Content-Transfer-Encoding: 8bit

.....................

.....................
..................

......................................................

......Yatagarasu-Takama-Kamuyamato2


...............
.......................................

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
CTF............................................................
TEL 03-6030-3333
Mail setoda@setodanote.net
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

```python
import base64
data = b"UEsDBBQAAQAAADBq8FK0Nz5zSgAAAD4AAAATAAAAUmVwb3J0LUFWLVQwMDk3LnR4dAzRMzm6s5vAM3huF0n2GEKFrarxVD3WvzurjKz9sjA7iD6nWis0GBRcIdcyrQkqliocBi2lCUB6J0hRUgHzDVCnVx6LnLS5LenqUEsBAj8AFAABAAAAMGrwUrQ3PnNKAAAAPgAAABMAJAAAAAAAAAAgAAAAAAAAAFJlcG9ydC1BVi1UMDA5Ny50eHQKACAAAAAAAAEAGADNWpx++XnXARJtllL6edcB0TOVfvl51wFQSwUGAAAAAAEAAQBlAAAAewAAAAAA"
base64_decoded=base64.b64decode(data)
f = open("Report-AV-T0097.zip","wb")
f.write(base64_decoded)
f.close()
```

解凍するとフラグゲットです．

```txt
This is Flag.

 flag{SoNtOkIhAmOuKaTaHoUmOtSuMuRuNoSa;)}
```