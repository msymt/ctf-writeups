# geographic-mapping

## 問題文

Find the coordinates of each location!

Flag format: flag{picture1 latitude,picture1 longitude,picture2 latitude,picture2 longitude}, all latitudes and longitudes to the nearest THREE decimal digits after the period. No spaces in the flag.

Example format: flag{12.862,48.066,-13.477,-48.376} The challenge author will not confirm individual locations, nor check your decimal digits. Three decimal digits gives a range of ~111 meters.

## 解法

### picture1.png

海岸線沿いで，赤と白で縦に分かれてる国旗があります．凝視すると，端に黒いマークのあることがわかります．

調べてみると，マルタと呼ばれる地中海に位置する国だとわかります．ここは気合いです．

画像中にヒントとして，方角が書かれていたので，西側に建物，東側が海岸となっている箇所を探します．

すると見つかりました（[URL](https://www.google.co.jp/maps/@35.8980603,14.517932,3a,75y,355.71h,86.61t/data=!3m6!1e1!3m4!1s_whGCsQQ2BK4r0s9tzcSqA!2e0!7i13312!8i6656?hl=ja)）

### picture2.png

高台から撮っており，右手にロープウェイが見えます．

国旗は水色と白色が主体で模様はありません．模様があった場合はサンマリノだと思いましたが，実は1842年に改定されたようです([出典](https://www.wikiwand.com/ja/%E3%82%B5%E3%83%B3%E3%83%9E%E3%83%AA%E3%83%8E%E3%81%AE%E5%9B%BD%E6%97%97))，

というわけで，サンマリノで決まりです．

あとはロープウェイを探して，高台へ移動したら終わりです．

試しに「サンマリノ　ロープウェイ」で調べたらひっかかりました([URL](https://www.google.com/maps/@43.9376694,12.4458827,3a,75y,357.77h,101.86t/data=!3m6!1e1!3m4!1snYl_K8Cr0zd5Etaxh7UKKA!2e0!7i13312!8i6656!5m2!1e4!1e1?hl=en))．


### flag

問題文に，緯度経度をそれぞれ小数第4位で四捨五入？しろと書かれているので，flagは

**flag{35.898,14.518,43.938,12.446}**

です．
