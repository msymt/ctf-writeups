# Scavenger Hunt

AUTHOR: MADSTACKS

## Description

There is some interesting information hidden around this site. Can you find it?

## writeup

html

```html
<!-- Here's the first part of the flag: picoCTF{t -->
```

mycss.css

```css
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

myjs.js

```JavaScript
/* How can I keep Google from indexing my website? */
```

jsにヒントらしきものが書かれており，`/robots.txt`にアクセスする．

ちなみにrobots.txtとは

> robots.txt ファイルとは、検索エンジンのクローラに対して、サイトのどの URL にアクセスしてよいかを伝えるものです。(後略)
https://developers.google.com/search/docs/advanced/robots/intro?hl=ja

```html
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

apache serverということで，apache特有のディレクトリにアクセスすれば良いと考える．そこで，`/.htaccess`にアクセスする．

```html
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

Macということで，`/.DS_Store`にアクセスする．

```html
Congrats! You completed the scavenger hunt. Part 5: _a69684fd}
```

## FLAG

```bash
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_a69684fd}
```

## 参考

- https://blog.hamayanhamayan.com/entry/2021/04/08/202410
