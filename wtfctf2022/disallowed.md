# Disallowed

78
Catch me if you can! boring

Author: Swati Verma

## 解法

devtoolsからソースを開くと、robots.txtを開くよう誘導があった。
robots.txtを開くと/007.htmlにdisallowの表記があった。

```html
User-agent: *
Disallow: /007.html
```

/007.htmlを開き、devtoolを開くと、フラグがコメントアウトされていた。

```html
<html>
    <head>
        <style>
            body{
                background-color: black;
            }
        </style>
    </head>
    <body>
        <div style='font-size:64px;text-align:center;color:white;padding:50px'>@_@</div>
        <div style='color:pink;font-size:40px;text-align:center'>Good , now only if you look around here a little more you will find the flag.</div>
    </body>
    <!--wtfCTF{r0b0ts_N0t_4ll0w3d}-->
</html>
```

## FLAG

```bash
wtfCTF{r0b0ts_N0t_4ll0w3d}
```
