# Robots.txt

## description

25

What is the file path in robots.txt?

Use Compromised CTF Platform's Challenge file to analyze.

Flag Format: KCTF{/path/path}

Author : TareqAhamed

## writeup

pcapファイルからrobots.txtが関係するキャプチャを探すために、`http`でフィルターをかけます。

`Follow Http Stream`からrobots.txtのレスポンスを確認するとフラグがありました。

![image1](images/image1.png)

![image2](images/image2.png)

## FLAG

```txt
KCTF{/includes/users.php}
```
