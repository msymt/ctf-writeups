# Waves

## Description

261

An employee has received a strange audio file, can you find what message is hidden?

Submit the flag as OFPPT-CTF{hidden_message}.

## writeup

以下の解析サイトに投げるとメッセージが出てきました。
https://morsecode.world/international/decoder/audio-decoder-adaptive.html

```
EEEEDSEÆNEVFENYN'NIÐEUEU5SEEEEEE IEEEEEETEEIEESEISERIAUEŚØWSIIDRHSEIEIIEE TTTTTTTANPT<BT>CTFM0RS3C0D31SFUN
```

OFPPT-CTF{CTFM0RS3C0D31SFUN}と思ったがincorrect。

モースル信号の部分を切り取って、再び再生すると
```
OFPPT<BT>CTFM0RS3C0D31SFUN
```

BTが本文の始まりなので、CTFM0RS3C0D31SFUNを解読することに。
このままでは、incorrectなので意味が通るようにする。しかし、MORSECODEISFUNでもincorrect。

そこで、`OFPPT<BT>CTF`を`OFPPT-CTF`と判断し、後ろをhidden_messageと見なすとcorrectとなりました。

## FLAG

```bash
OFPPT-CTF{M0RS3C0D31SFUN}
```
