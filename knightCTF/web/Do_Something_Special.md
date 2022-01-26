# Do Something Special

## description

50

Alex is trying to get a flag from this website. But something is wrong with the button. Can you help him to get the flag?

Note : Burte Force/Fuzzing not required and not allowed.

Flag Format: KCTF{S0M3_TEXT_H3R3}

Author: marufmurtuza

## writeup

URLにアクセスし、ボタンをクリックすると、特殊文字が混ざったURLにアクセスしました。
特殊文字を意味が通ずる文字に変えても404が返ってきたので、特殊文字をASCIIコードに変換しました。

```
/gr@b_y#ur_fl@g_h3r3!
Not Found
The requested URL was not found on this server.

Additionally, a 404 Not Found error was encountered while trying to use an ErrorDocument to handle the request.

/gr%40b_y%23ur_fl%40g_h3r3%21
KCTF{Sp3cial_characters_need_t0_get_Url_enc0ded}
```

## FLAG

```txt
KCTF{Sp3cial_characters_need_t0_get_Url_enc0ded}
```
