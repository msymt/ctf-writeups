# Sometime you need to look wayback

## description

point: 25

Challenge Link: http://wayback.kshackzone.com/index.html

Flag Format : KCTF{something_here}

Note : Burte Force/Fuzzing not required and not allowed.

Author: 0xmahi

## writeup

URLにアクセスし，ソースを見るとリポジトリのURLが記載．

```HTML
<!--Test Bot Source Code: https://github.com/KCTF202x/repo101-->
```

コミットログを`KCTF`で検索すると，フラグを発見．

https://github.com/KCTF202x/repo101/commit/74bf8c5679108c685d4c52dd18c191d605b53977

## FLAG

```txt
KCTF{version_control_is_awesome}
```
