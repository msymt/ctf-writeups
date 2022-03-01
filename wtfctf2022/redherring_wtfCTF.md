# redherring wtfCTF

400

Setup and call me!

[redherringwtfCTF.git](https://github.com/madjelly/redherringwtfCTF)

Author: madjelly & theProton

## 解法

docker-compose upでコンテナを立ち上げた後、Get Hashed Flagをクリックしたら、devToolsにフラグが出力されました。

(Fetch all flagsのとこは何をやっているんだろう？)

```javascript
{_id: '61e815323b78f9332783f264', flag: 'wtfCTF{4p1_fl4g_h4sh}', isHashed: true, __v: 0}
flag: "wtfCTF{4p1_fl4g_h4sh}"
isHashed: true
__v: 0
_id: "61e815323b78f9332783f264"
```

## FLAG

```bash
wtfCTF{4p1_fl4g_h4sh}
```
