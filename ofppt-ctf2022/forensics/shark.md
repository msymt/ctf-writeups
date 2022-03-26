# Shark

## Description

200

We managed to capture an important conversation.

We need you to find the flag inside the pcap file.

## writeup

HTTP objectをexportするとフラグらしき文字列が見えました。
PDM-DZZPYがOFPPT-CTFで、w43bdc_3rd_g0110P_ci4gv4がフラグの中身になると考え、何かしらの形式でdecodeすれば良いと判断しました。文字がどれもアルファベット上ずれてそうと判断し、cyberchefでrot13, rot47あたりを適用してみました。

```
Gur synt vf }w43bdc_3rd_g0110P_ci4gv4{PDM-DZZPY
Gur synt vf OFPPT-CTF{4lw4ys_F0110w_th3_str34m}
```

部分的に逆順しては、フラグが出てこなかったため、全体を逆順にしてみました。するとフラグが出てきました。

https://gchq.github.io/CyberChef/#recipe=Reverse('Character')ROT13(true,true,false,16)&input=R3VyIHN5bnQgdmYgfXc0M2JkY18zcmRfZzAxMTBQX2NpNGd2NHtQRE0tRFpaUFk

## FLAG

```bash
OFPPT-CTF{4lw4ys_F0110w_th3_str34m}
```
