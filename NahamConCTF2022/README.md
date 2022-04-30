# NahamCon CTF 2022

https://ctf.nahamcon.com

## Flagcat

見るだけ

## Quirky

PNG形式を表しているようでした。cyberchefのmagicを適用すると、QRコードのようでした。

https://gchq.github.io/CyberChef/#recipe=From_Hex('%5C%5Cx')Parse_QR_Code(false)

```bash
echo -en '<quirkyの中身>'
PNG

IHDRoo

      #PLTEٟtRNSȵ        pHYs

                            ~%IDAT81 б\%@kq%Ε/@:
#EfhR,!!
DkD.urf*I~
        v炝L'Nb(u+7DsZ~Ofdx:%9Vy/tqW[l4ysS;63s`R~FwomJv:%I"D8(%ͥSgD9Q=!X%:vihLT-,Y'Rд4<Uq
i7wn    IENDB`%

```

## Mobilize

apkファイルを`jadx-gui`ツールを使い、デコンパイルし、`flag{`で調べると`res/values/strings.xml`にフラグがありました。

```xml
    <string name="flag">flag{e2e7fd4a43e93ea679d38561fa982682}</string>
```

### 参考

https://qiita.com/maika_kamada/items/904e842c691e4a66e4a8

## Jurassic Park

Dr. John Hammond has put together a small portfolio about himself for his new theme park, Jurassic Park. Check it out here!

### solution

/robots.txtにアクセスすると、`Disallow /ingen/` となっていた。/ingenにアクセスするとフラグが手に入った。

```
flag{c2145f65df7f5895822eb249e25028fa}
```

## Prisoner

色々入力しても反応がなかったため、Ctrl-Dを押すと、Pythonが動いていることがわかりました。flag.txtをopenして読めばいけます。

```python
  _________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||\
   / ||--_||_____||_--|| \
  (_(||)-| SP1337 |-(||)_)
          --------

Hello prisoner, welcome to jail.
Don't get any ideas, there is no easy way out!
: Traceback (most recent call last):
  File "/home/user/jail.py", line 27, in <module>
    input(": ")
EOFError
>>> \n
  File "<stdin>", line 1
    \n
     ^
SyntaxError: unexpected character after line continuation character
>>> print(flag.txt)
>>> open('flag.txt')
<_io.TextIOWrapper name='flag.txt' mode='r' encoding='UTF-8'>
>>> file = open('flag.txt')
>>> data = file.read()
>>> print(data)
flag{c31e05a24493a202fad0d1a827103642}
```
