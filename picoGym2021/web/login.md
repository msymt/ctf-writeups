# login

AUTHOR: MADSTACKS

## Description


## writeup

ソースを見るとflagらしきものが見える．

```javascript
(async()=>{
    await new Promise((e=>window.addEventListener("load", e))),
    document.querySelector("form").addEventListener("submit", (e=>{
        e.preventDefault();
        const r = {
            u: "input[name=username]",
            p: "input[name=password]"
        }
          , t = {};
        for (const e in r)
            t[e] = btoa(document.querySelector(r[e]).value).replace(/=/g, "");
        return "YWRtaW4" !== t.u ? alert("Incorrect Username") : "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ" !== t.p ? alert("Incorrect Password") : void alert(`Correct Password! Your flag is ${atob(t.p)}.`)
    }
    ))
}
)();
```

`btoa()`とは
> WindowOrWorkerGlobalScope.btoa() メソッドは、 Base64 でエンコードされた ASCII 文字列をバイナリ文字列 (例えば String オブジェクトのうち、文字列中のすべての文字がバイナリデータのバイトとして扱うことができるもの) から生成します。
このメソッドを使用すると、通信に支障をきたす可能性のあるデータをエンコードして送信し、その後 atob() メソッドを使用して再度デコードすることができます。例えば ASCII で 0 から 31 の値ような制御文字をエンコードすることもできます。
https://developer.mozilla.org/ja/docs/Web/API/btoa

ということなので，base64からASCII文字列にデコードするために，atob()を使います．

```javascript
// console
atob("cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ")
'picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}'
```

以下の内容でsubmitするとalertが出現しました．

```html
username=admin
password=picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
```

```html
Correct Password! Your flag is picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}.
```

## FLAG

```bash
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
```
