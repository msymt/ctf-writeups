# Vuln

## description

25

What vulnerability did the attacker exploited?

Use Compromised CTF Platform's Challenge file to analyze.

Flag Format: KCTF{vulnerability_name}

Author : TareqAhamed

## writeup

`/hackerz_arena/includes/login_confirm.php`に対して、`username=admin&password=admin123&csrf=ba8bd9bceadd168c6e0973da91b5d86d0f6895c8&submit=`とusernameとpasswordの値からSQL Injection関係かな？と思いました(これで合ってるのかな...)。

## FLAG

```txt
KCTF{sql_injection}
```

## 所感

フラグの形式が微妙ですね。。
