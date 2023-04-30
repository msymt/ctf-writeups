# UMCTF2023 <!-- omit in toc -->

<!-- ctf link -->

ポケモンを題材にしたCTFでした。

## Gone Missing 1


### SOLUTION <!-- omit in toc -->

ストリートビューの近くに写る建物をGoogle画像検索で調べると、
ノルウェーのロイヤル城であることがわかりました。

[ストリートビュー](https://www.google.com/maps/@59.9170629,10.7298181,3a,75y,252.96h,84.73t/data=!3m8!1e1!3m6!1sAF1QipOUkl6k12cD3_wuXunz2vO6ZTdJIhQPrFllGUWV!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOUkl6k12cD3_wuXunz2vO6ZTdJIhQPrFllGUWV%3Dw203-h100-k-no-pi-0-ya264.4473-ro0-fo100!7i7744!8i3872)

### FLAG <!-- omit in toc -->

```
UMDCTF{I_b3t_rainbolt_c0uld_g3t_th1s_!n_thr33_s3c0nd5}
```

### REF <!-- omit in toc -->

https://www.istockphoto.com/jp/%E3%82%B9%E3%83%88%E3%83%83%E3%82%AF%E3%83%95%E3%82%A9%E3%83%88/%E3%83%AD%E3%82%A4%E3%83%A4%E3%83%AB%E5%9F%8E%E3%83%8E%E3%83%AB%E3%82%A6%E3%82%A7%E3%83%BC%E3%82%AA%E3%82%B9%E3%83%AD-gm92694741-3530704


## Mirror Unknown

I found some unknown symbols in a nearby collapsed cave. Can you figure out what they mean?

(Note: Ancient civilizations didn't believe in whitespace of lowercase)

Author: Ishaan514

### SOLUTION <!-- omit in toc -->

アンノーン文字をアルファベットに変換したあと、鏡文字であることに注意して順番を変換しました。

```
# 画像の通り
hojnis
sniur

# 鏡文字を考慮した場合
sinjoh
ruins
```

### FLAG <!-- omit in toc -->

```
UMDCTF{sinjohruins}
```

### REF <!-- omit in toc -->

https://www.google.com/url?sa=i&url=https%3A%2F%2Fkokorogu.com%2Farceus-8&psig=AOvVaw2TgCGKYEd138B6SNXFJhh_&ust=1682940170820000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCIiJ_-u-0f4CFQAAAAAdAAAAABAE


## MISC/A TXT For You and Me

We may not have A, AAAA, or even an MX, but boy do we have a TXT for you! Just grab it from a-txt-for-you-and-me.chall.lol

### SOLUTION <!-- omit in toc -->

MX, TXTという単語から、DNSレコードのことだと推測しました。

nslookupツールを使い、TXTオプションを指定するとフラグがでてきました。


https://www.cman.jp/network/support/nslookup.html

### FLAG <!-- omit in toc -->

```
UMDCTF{just_old_school_texting}
```

### REF <!-- omit in toc -->

https://server-99.com/dns-record/


---

途中

## Gone Missing 2

### SOLUTION <!-- omit in toc -->

近くに星形の建造物がありました。
Google Lensを使用すると、その建造物の名前が、Star of Palawooだと判明しました。

http://www.westphalfamily.com/star.html

そこの設置場所がAltadenaであることも判明しました。

## No.352

password 1: the name of pokemon #352 in lowercase
password 2: timetofindwhatkecleonishiding

art by Elz#7408

Author: Angela

### SOLUTION <!-- omit in toc -->

図鑑番号352のポケモンはカクレオン(Kecleon)

password 1: kecleon
password 2: timetofindwhatkecleonishiding


### FLAG <!-- omit in toc -->

```
```

### REF <!-- omit in toc -->

https://zukan.pokemon.co.jp/detail/0352#:~:text=%E3%82%AB%E3%82%AF%E3%83%AC%E3%82%AA%E3%83%B3%EF%BD%9C%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E3%81%9A%E3%81%8B%E3%82%93
