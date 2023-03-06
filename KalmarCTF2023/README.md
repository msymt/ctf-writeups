# KalmarCTF 2023  <!-- omit in toc -->

https://ctftime.org/event/1878/

- [sewing-waste-and-agriculture-leftovers](#sewing-waste-and-agriculture-leftovers)
- [cards](#cards)


## sewing-waste-and-agriculture-leftovers

UDP - UNRELIABLE datagram protocol.

### SOLUTION <!-- omit in toc -->

data部分を取得すると，一部が欠損していた．他のパケットのdataでは埋まっていたため，全てを埋めていった．

`awk -F'    Text: ' '{print $2}' ./swaal_text2.txt > ./swaal_text2_ascii.txt`

### FLAG <!-- omit in toc -->

```
kalmar{if_4t_first_you_d0nt_succeed_maybe_youre_us1ng_udp}
```

## cards

Follow the shuffle.

### SOLUTION <!-- omit in toc -->

FTPのパケットをFollow Streamで確認すると，CWDとPassive Modeの値だけがパケットごとに変わっていた．

```
220 FTP Server
USER user
331 Please specify the password.
PASS 123
230 Login successful.
SYST
215 UNIX Type: L8
CWD 357
250 Directory successfully changed.
TYPE I
200 Switching to Binary mode.
PASV
227 Entering Passive Mode (0,0,0,0,156,69).
RETR flagpart.txt
150 Opening BINARY mode data connection for flagpart.txt (1 bytes).
226 Transfer complete.
QUIT
221 Goodbye.
```

```
220 FTP Server
USER user
331 Please specify the password.
PASS 123
230 Login successful.
SYST
215 UNIX Type: L8
CWD 356
250 Directory successfully changed.
TYPE I
200 Switching to Binary mode.
PASV
227 Entering Passive Mode (0,0,0,0,156,71).
RETR flagpart.txt
150 Opening BINARY mode data connection for flagpart.txt (1 bytes).
226 Transfer complete.
QUIT
221 Goodbye.
```

データ部分だけ流れてきた順に並べると以下の通りとなった．
```
m_tfwr_flf_3eccaykdw_hhuhrld{erae
_onsuo}04afr__ar_u1ut_ksffklas_hsce33f_e3p_hn
```

このままではフラグの形式とあっていない．
そこで，CWDの値を基準にパケットをソートすればフラグになると考えた．

```py
# ref: https://github.com/Daste745/kalmarctf-2023/blob/master/cards/analyze.py
import json

with open("cards.json") as f:
    packets = json.load(f)

collect_packets: list[tuple[str, str]] = []
last_cwd = "0"
for packet in packets:
    layers = packet["_source"]["layers"]

    if "ftp" in layers:
      cwd = layers["ftp.current-working-directory"]
      last_cwd = cwd

    if "data" in layers:
      data = layers["data"]["data.data"]
      collect_packets.append((data, last_cwd))

# CWDでソート
collect_packets.sort(key = lambda x: x[1])

for packet, cwd in collect_packets:
  value = int(packet, base=16) # hex string -> int
  print(chr(value), end="")
print()
```

<!-- `frame.number >= 1622 && data.len > 0` -->


### FLAG <!-- omit in toc -->

```
kalmar{shuffle_shuff1e_can_you_k33p_tr4c_of_where_th3_ckads_are_shuffl3rd_n0w}
```

### REF <!-- omit in toc -->

https://blog.hamayanhamayan.com/entry/2023/03/06/083921#web-Ez-


<!-- ## BabyOneTimePad

## CycleChaser

## mjs

https://uz56764.tistory.com/89 -->
