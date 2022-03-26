# Déja vu

## Description

200

We received another strange message.
can you help us decipher it?

## writeup

モールス信号が書かれたテキストファイルが渡されたため、解析器でデコードしました。

```bash
$ git clone git@github.com:kusuwada/morse-code.git
$ python3 morse.py
input mode (d: decode, e: encode) > d
input your message > --- ..-. .--. .--. - -....- -.-. - ..-. / - .... .---- ... ..--.- .---- ... ..--.- - .... ...-- ..--.- ----- .-.. -.. ..--.- ... -.-. .... ----- ----- .-.. ..--.- -- ----- .-. ...-..- ...-- ..--.- -.-. ----- -.. ...-- /
[ERROR] There's invalid character: /
[ERROR] There's invalid character: /
OFPPT-CTF*/*TH1S_1S_TH3_0LD_SCH00L_M0R$3_C0D3*/*
```

## FLAG

```bash
OFPPT-CTF{TH1S_1S_TH3_0LD_SCH00L_M0R$3_C0D3}
```
