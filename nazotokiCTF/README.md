# ナゾトキCTF

https://ctf.nazotoki.tech/

Team: Ir0nMaidenとして参加しました。謎解き要素が分からずヒント解放ボタンをめちゃくちゃ押しました。

- [ナゾトキCTF](#ナゾトキctf)
  - [Misc/かに座](#miscかに座)
    - [SOLUTION](#solution)
    - [FLAG](#flag)
  - [Misc/さそり座](#miscさそり座)
    - [SOLUTION](#solution-1)
    - [FLAG](#flag-1)
  - [Misc/うお座](#miscうお座)
    - [SOLUTION](#solution-2)
    - [FLAG](#flag-2)
    - [REF](#ref)
  - [riddle/おひつじ座](#riddleおひつじ座)
    - [SOLUTION](#solution-3)
    - [FLAG](#flag-3)
  - [2nd Challenge/へびつかい座](#2nd-challengeへびつかい座)
    - [SOLUTION](#solution-4)
    - [FLAG](#flag-4)
  - [Last Challenge/最終問題](#last-challenge最終問題)
    - [SOLUTION](#solution-5)
    - [FLAG](#flag-5)

## Misc/かに座

仲間はずれを探せ

### SOLUTION

zipファイルの中身を見ると、一つだけtextファイルがありました。catをするとフラグがありました。

```bash
$ file ./*
./0961db32a59b8a83c1996498f9d1d80e: pcapng capture file - version 1.0
./397cbf6db9d7ae6906ae420aedc5346c: pcapng capture file - version 1.0
./44ca0844398b2d010d8cd4a31ddb023d: pcapng capture file - version 1.0
./4de447a391e32baeb5a52c55aa14467b: pcapng capture file - version 1.0
./550eadb88a230018bf043d1b6ad15863: pcapng capture file - version 1.0
./635cbc8a5dc1a528c3b5cb9eecdc1086: pcapng capture file - version 1.0
./7463543d784aa59ca86359a50ef58c8e: pcapng capture file - version 1.0
./766cc4dd4d5005652e8514e3513683f8: pcapng capture file - version 1.0
./7c70e2cb2b4a13c4590f6b15c30385fd: pcapng capture file - version 1.0
./a0678bcea04dbd6852c219062ab2bb3c: pcapng capture file - version 1.0
./b9c94e8a87e3647c5a0fa4ff358ecc65: pcapng capture file - version 1.0
./f0525aafa095ed2665d03681537a70ea: UTF-8 Unicode text
./f8a5c386478fa64f118056b82acc31d2: pcapng capture file - version 1.0
$ cat ./f0525aafa095ed2665d03681537a70ea
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
Open in Notepad.Open in Notepad.Open in Notepad.Open in Notepad.
nazotokiCTF{イイワケ}
```

### FLAG

```
イイワケ
```

## Misc/さそり座

世界一かわいいうちの犬を紹介します

### SOLUTION

画像を拡大すると犬の瞳にフラグが書かれていました。

![dog](./images/scorpio.jpg)

### FLAG

```
カクダイ
```

## Misc/うお座

みずがめ座からてんびん座に向かうとき、ひみつの鍵が手に入るだろう。水の中に浮かぶ真実を見定めよ。

### SOLUTION

encファイルを復号することで、パスワード付きzipのパスワードを特定します。

ヒントを使うと

1. みずがめ座からてんびん座に向かうとき…ヘッダー情報に記録されるものはなんでしょうか？
2. どうやらリファラーの情報にaquariusが含まれた状態でてんびん座のサイトにアクセスすると鍵が手に入りそうです。書き換えられないでしょうか？やり方がわからない人は「リファラー　書き換え」とかでぐぐると良いかもしれません。

とあったので、Burpsuiteを使い`Referer:aquarius`を加えました。すると秘密鍵が表示されました。

```txt
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAunVG5a8SbXgsayNWhd4f9FYsWb8z57P2Ql8Yq+fQgq0Y2xcH
/HgHO0vZrgSbjFLxnpx4D9arOtvGdn06GLZcL3eU32jPvqVh8QhqmaQ8bdUDlEp8
yt45DMoleYflw8c9q2dDsRjLUoE2qhtMm2xR8B9U+mRq+vVgEJdvNMgmn+XtsmRx
A41n3nHTfTcOznZaNRxyAqZjooDOuUoVBStJVUqbd4a3EzMCBbdAzyQ2VdQEigT0
PVstPiMI0draaO9oKlZkfuGkJJ3Ftn8+A4cjIG8ycihsGqfEMSVUpLmUI+Etb0+C
3iD+B7P25v0CDNdD2odWIRipjdE8TmuTA+AsuQIDAQABAoIBAQCBCSw5Q4EzNNk4
g8oa9m+SvhgPO90F2mrv37PJM7H+3R+4byXduIr4pDNO1G15HOWNaKdF/r+dCf88
fMk51OnTB6SFP5mVTAqNrc9n6FrRf3rsoufd1RASI8rvYfbGGBo7hkk4Q/phbH6S
FjZb0QibbnN2nQvUBP+oO8R/+IuSV3NgxvtQ3CggRnqTiwx99kHO3gEXJVHozq09
mceaWIQeT6jAf5nMsNKl2YlBxomMkeXZ8jEcCJQcAPuHJjZ2SJmLpbADIffg/c95
oaLejnoEWUflnN/QPw7shHE2F50uKyEYAh5uNCjVHRQE15jUOQZBr5aLMtpyCkfJ
3bPrzFcBAoGBAOyEMyBBwAh2Kuk+QS9OCsFcxjTQPV/jkHnk2nU8I7xrO0MqONOL
/ily+GcbTrY4bx8zkIKuYwEAp/5Mybd+C/kRsjeSGZVrNxNDNG32JYTn49Z1miKv
jNMGUJsfOoKI6G1gKnI3j5WlP2E+xXtQkJUMwqj5vdafCTVJhWrucFyxAoGBAMnR
ave7rOChNxVEoS7YmwMUSEk/PlM4MLkv7WkOPdNATxZ2u5fj8RrHfI4pGt//QXUX
pI0dE6Y8ndM24YhynvqGYr8cyygBj+BpMZFXSFmf2ozRTawFbo2IgqqsZ6AszQVb
EUuq5k5mx5Mg+ilMMzTmxjL4AD5GRy/2ofYK5DKJAoGACdhW6HjULYX9s0fMHtP4
zqO1/GzOoTcvxGMqVMb0FdvA08LmKqghJEiM3n3cgOlIdtwGn+nyZRBJ7eP0YZb1
mKCL8pQ6TGXyHPMnM4yTczzT1xF+IQN9sSsKH+rk3JomUqc2HRsC9w+x27JpNgDc
g9fMIoyCwnRMRdORoinas4ECgYAausnYFdtHxRJulrBia/3b4ovQZ7fxfbe2T0q6
Z1B48kOHTiJ6c44zZchxa7BLips4zvDUX82CbvTYTKSCVewIclQRy9Z8bfiIWGZg
QZcrh6iCjhYjenSx+iqUQFFZPZXJ583an7/xElvMeMmpPpZpo0cM6RvfI5+6EohQ
9hBTQQKBgQCBiu+qiElJXJUTrwr3XESHUEsCPz27VWViYlj/n6GsY80QSf4Y1F0d
ynDDCJ4zE0FL1WfFFGMqaE86wvQZwvv9NCqSkpxhfbYhf/lKUmyNIyqoQYkV7kAK
NjQ0gdNlw4NLioSXny6/0k5G4OIzwh8QNf38sZGKhm7FMVQ4G8r1Yw==
-----END RSA PRIVATE KEY-----
```

次に秘密鍵を用いてencファイルを復号すると、`fomalhaut`がパスワードだと分かりました。

```bash
$ openssl rsautl -decrypt -in password.enc -inkey private.ky
The password for the zip is "fomalhaut".
```

入力すると以下の画像がでてきました。

![pisces](./images/pisces.jpg)

stegsolveを使い、Offsetをずらすとフラグが出てきました。

![keppaku](./images/keppaku.png)

### FLAG

```
ケッパク
```

### REF

- https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Referer
- http://ctf.publog.jp/tag/Crypto

## riddle/おひつじ座

あなたが目指しているものの間を読め

### SOLUTION

ヒントを見ると

1. プロローグをよく読んでね
2. あなたが目指してるものは「セキュリティ業界の星」 つまり…「★」どこかにマークがなかったでしょうか？テキストとは限りませんよ？

となっていました。

プロローグのページの画像を見ると、不自然なインデントの画像がありました。
星マークの箇所を縦読みすると「ハンドル」と書かれてしました。

![intro](./images/ai-intro.png)

### FLAG

```
ハンドル
```

## 2nd Challenge/へびつかい座

最終問題に進むためのフラグを導く魔法の解答用紙をご用意しました（謎解きによくあるやつ）

※使い方のヒント

PDF版とPNG版を用意してますが内容は一緒です
印刷できる環境がある方は印刷するといいかも
PDF版は文字入力ができるようになってます
お使いのIMEによるかもしれませんがカタカナ入力よりひらがな入力のほうがやりやすいかも（どっちでも大丈夫です）
tabキーで次の入力欄に移動できるようになってます
あとで提出が必要になったりするとかではないので最悪使わなくても大丈夫です
ただし、用紙の様式はよくみておいたほうが良さそうです

### SOLUTION

answersheetには、12とそれに対応した4つの空白が書かれていました。

![answersheet](./images/answersheet.png)

今までのフラグを書き込めば良いと判断し、順番は[プロローグ](https://ctf.nazotoki.tech/prologue)にあった星座の番号をあてはめました。

```txt
おひつじ：ハンドル
おうし：テントウ
ふたご：ナイーブ
かにイイワケ
しし：チーター
おとめ：オワスプ
てんびん：クローン
さそりカクダイ
いて：イースト
やぎ：タイスウ
みずがめ：タカハシ
うお：ケッパク
```

先頭を縦読みすると`ハテナイチオクカイタタケ`。スコアサーバ左上にハテナマークがあったので、クリックするとCokkieに`nazotoki`という項目が追加されました。最後にここを1億に書き換え、ページをリロードするとフラグが出てきました。

![second](./images/second.png)


### FLAG

```
ポラリス
```

## Last Challenge/最終問題

パスワードを解け

### SOLUTION

ヒントを見ると以下のようになってました。

```
かに座の問題にはpcapファイルが12個ありました。

パケットには前のパケットを示す Sequence number と後ろのパケットを示す Acknowledgment number いう情報が付与されており、それを見るとバラバラの12個はもともとひとつのストリームのなかでつながったパケットであったことがわかります。

パケット同士の前後関係を確認し、流れに従って並び替えると

うお座
やぎ座
かに座
てんびん座
おひつじ座
みずがめ座
おとめ座
しし座
ふたご座
さそり座
いて座
おうし座 の順番になるようです。
```

フラグを並び替えると以下の通りとなりました。
```
うお座: ケッパク
やぎ座:タイスウ
かに座:イイワケ
てんびん座:クローン
おひつじ座:ハンドル
みずがめ座:タカハシ
おとめ座:オワスプ
しし座:チーター
ふたご座:ナイーブ
さそり座:カクダイ
いて座:イースト
おうし座:テントウ
```

右から2番目の列を縦読みすると`パスワードはスターダスト`でした。

`stardust`をパスワードフォームに入力すると

https://ctf.nazotoki.tech/oort-cloud

にリダイレクトしました。フラグはこのサイトに書かれていました。

### FLAG

```
オールト
```

