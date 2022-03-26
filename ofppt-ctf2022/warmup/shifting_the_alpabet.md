# Shifting the alphabet

## Description

200
Can you decipher this flag?
}g3o4ucy4_3ug_gs1uF_qa4_3fe3i3e{SGP-GCCSB

## writeup

文字をずらすということで、ROT変換であることが予想されます。

https://tools.m-bsys.com/original_tooles/str_rotN.php

そのまま渡してもフラグらしきものが出てこなかったため、逆順にしてみると出てきました。

https://gchq.github.io/CyberChef/#recipe=Reverse('Character')ROT13(true,true,false,13)&input=fWczbzR1Y3k0XzN1Z19nczF1Rl9xYTRfM2ZlM2kzZXtTR1AtR0NDU0I

## FLAG

```bash
OFPPT-CTF{r3v3rs3_4nd_Sh1ft_th3_4lph4b3t}
```
