# where are the robots

AUTHOR: ZARATEC/DANNY

## Description

Can you find the robots?

## writeup

robotsということで，`/robots.txt`にアクセスすると，以下が表示された．

```html
User-agent: *
Disallow: /477ce.html
```

`/477ce.html`に直接アクセスすると，フラグが出現した．

```txt
Guess you found the robots
picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
```

## FLAG

```bash
picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
```
