# Follow The White Rabbit

25

## description

Will you choose to follow the white rabbit like NEO? THINK wisely or LOOK your path deeply before you take step.

Flag Format: KCTF{S0M3TEXTH3R3}

Author: marufmurtuza

## writeup

`hexdump whiterabbit.jpg`をしました。

```txt
000001e0	78 74 00 00 00 00 43 6f	70 79 72 69 67 68 74 20		xt....Copyright
000001f0	32 30 31 35 2c 20 45 6c	6c 65 20 53 74 6f 6e 65		2015, Elle Stone
00000200	20 28 77 65 62 73 69 74	65 3a 20 68 74 74 70 3a		(website: http:
00000210	2f 2f 6e 69 6e 65 64 65	67 72 65 65 73 62 65 6c		//ninedegreesbel
00000220	6f 77 2e 63 6f 6d 2f 3b	20 65 6d 61 69 6c 3a 20		ow.com/; email:
00000230	65 6c 6c 65 73 74 6f 6e	65 40 6e 69 6e 65 64 65		ellestone@ninede
00000240	67 72 65 65 73 62 65 6c	6f 77 2e 63 6f 6d 29 2e		greesbelow.com).
```

`http://ninedegreesbelow.com/`にアクセスすると`GIMP`が見えたりして、画像を編集すればいいのかな？と考えました。

stegsolveでRGBを反転させると、画像にモールス信号らしきものが見つかりました。

そこで、モールス信号をデコードするサイトに打ち込みました([URL](https://www.boxentriq.com/code-breaking/morse-code))。

```bash
# before
.-.. ----- --- -.- -... ....- -.-- ----- ..- .-.. ...-- ....- .--.
# after
L0OKB4Y0UL34P
```

## FLAG

```txt
KCTF{L0OKB4Y0UL34P}
```
