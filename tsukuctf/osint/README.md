# OSINT

## ramen(100)

> ハッカーにとってラーメンは必須の飲み物だといわれています。写真のラーメン店の本店のインスタグラムIDを特定してください。

画像を突っ込む
https://www.reverseimagesearch.com/

Yandexにて似たようなラーメン屋を発見
- https://yandex.com/images/search?url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F2273763%2FuRCNepmrBwpw-8ECPPqdSQ7023%2Forig&rpt=imageview&source=collections&cbir_id=2273763%2FuRCNepmrBwpw-8ECPPqdSQ7023&cbir_page=similar

銀座 篝というラーメン屋らしい．
- https://es.foursquare.com/v/%E9%8A%80%E5%BA%A7-%E7%AF%9D/56548771498e4a9d47e6d8b5/photos
- https://www.instagram.com/explore/tags/%E9%8A%80%E5%BA%A7%E7%AF%9D/

全国展開してるから，何店舗かアカウントが存在する
- https://www.instagram.com/p/B0vbvOXgZhd/?igshid=tt1vi6kroc9l

 ~~こういう時は，本店アカウントが狙い目だと思い，入力 ~~　問題文の指示通り本店アカウントを入力．
- https://www.instagram.com/kagari_honten/?hl=ja

```txt
TsukuCTF{kagari_honten}
```
## shop(100)

> Tsukushiくんはショッピングモールにデートに来ましたが、相手がいなかったことに到着してから気づきました。帰ろうと思いましたがここがどこかわかりません。動画内に映っているショッピングモールの店舗名を特定してください。

最後に滋賀ナンバーが映った．滋賀でイオンモールと言えば草津のクソでかイオンだと思い，検索．

```txt
TsukuCTF{イオンモール草津}
```

## Beach(100)

「東京 ビーチ C オブジェ」で検索．サザンビーチちがさきというらしい．
- https://rtrp.jp/articles/62176/

最寄りえきは，「電車　JR東海道線・相模線 茅ヶ崎駅下車」
- https://www.city.chigasaki.kanagawa.jp/kankou_list/koen/1006949/1006955.html

```txt
TsukuCTF{Chigasaki}
```

## dam(100)

> 友人に添付画像の写真にバス釣りに行くと誘われた。しかし、肝心の行き方を友人に聞こうとしたが友人の携帯電話は圏外であり、電話に出ない...。行き先の貯水池の名前を突き止めよう。

「貯水池　赤い橋」で検索すると河内貯水池が引っかかった．

https://www.kitakyushu-museum.jp/resources/2394


```txt
TsukuCTF{河内貯水池}
```

## fishing(100)

画像を突っ込む
https://www.reverseimagesearch.com/

以下のサイトのマップがそれっぽいのでストリートビューで探索
- Koto Ward Wakasu Public Park - 東京港埠頭株式会社
  - https://www.tptc.co.jp/en/c_park/03_09

```txt
TsukuCTF{若洲海浜公園}
```

## train2(100)

> 今いる駅名を答えてください。駅名は漢字で答えてください。例: 京都駅の場合はTsukuCTF{京都}がフラグになります。

画像を拡大すると，「出町？9号」と書かれた看板が見えます．

検索して，ストリートビューで眺めるとそれっぽい駅が引っかかりました

```txt
TsukuCTF{元田中}
```

----

以下時間以内に解けなかった問題

## cafe(100)

>　私の彼氏(@7aru7aru)が最近どうやらメイドカフェにハマっているみたいなんだけど、そのカフェの場所が知りたいの！そのお店の公式 HPのURLがフラグです。ただし、もしそのお店がチェーン店の場合は店舗専用HPのURLがフラグです。

「@7aru7aru メイドカフェ」で調べたり，画像ツイを眺めたらツーショットが出てきました．

そこのいいね欄に，関係者らしきアカウントがいっぱいあったため，そちらからHPへ．

https://maidreamin.com

注意点として，

> ただし、もしそのお店がチェーン店の場合は店舗専用HPのURLがフラグです。

とあったので，元ツイの背景とチェーン店を睨めっこしました．

以下フラグです（入力チェックしてません．）

```txt
TsukuCTF{https://maidreamin.com/shop/detail.html?id=5}
```