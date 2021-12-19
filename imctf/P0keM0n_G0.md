# P0keM0n G0🥎

## 難易度

medium

## solve数

11

## 問題文

スマホアプリ「ポケモンGo」のポケストップが写ったスクリーンショットから，ポケストップの緯度経度を特定せよ．

ポケストップとは

「ポケストップ」は、世界中のあらゆる場所にあります。名所旧跡や有名な建物などはもちろん、普段気にしていなかった身近なあの場所も、実は「ポケストップ」かもしれません。(https://www.pokemongo.jp/play/)

フラグ形式:`imctf{緯度,経度}`

例えば，緯度:35.391751，経度:139.444050の場合は，imctf{35.391751,139.444050}となる． 緯度,経度は小数第6位まで入力せよ．

## write-up

「PokemonGo OSINT」と検索すると,OSINTに使えそうな資料がまとまったサイトがヒットする([URL](https://www.osintdojo.com/resources/#pokemon_go))．

そこから，[POGOMAP](https://www.pogomap.info/)を選ぶ．

サイト右下の検索機能から「PokeStops」を選択し，「金鎚少年」と検索する．

最後に「More Infomation」をクリックすると，緯度経度が現れる．

## FLAG

```bash
imctf{35.156641,136.963986}
```
