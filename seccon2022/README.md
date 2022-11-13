# SECCON CTF 2022

https://ctftime.org/event/1764

解けなかったため、復習用としてまとめました。

- [SECCON CTF 2022](#seccon-ctf-2022)
  - [misc/finding](#miscfinding)
    - [解放1](#解放1)
    - [解放2](#解放2)


## misc/finding

```python
#!/usr/bin/env python3.9
import os

FLAG = os.getenv("FLAG", "FAKECON{*** REDUCTED ***}").encode()

def check():
    try:
        filename = input("filename: ")
        if open(filename, "rb").read(len(FLAG)) == FLAG:
            return True
    except FileNotFoundError:
        print("[-] missing")
    except IsADirectoryError:
        print("[-] seems wrong")
    except PermissionError:
        print("[-] not mine")
    except OSError:
        print("[-] hurting my eyes")
    except KeyboardInterrupt:
        print("[-] gone")
    return False

if __name__ == '__main__':
    try:
        check = check()
    except:
        print("[-] something went wrong")
        exit(1)
    finally:
        if check:
            print("[+] congrats!")
            print(FLAG.decode())

```

怪しいと思った点

- 環境変数が保存されているファイルがあれば、そこを読み取れば...?
- `check()`のExceptionが少ない気がする。


### 解放1

> check = check() となっている部分で、 check() で定義されていない Error で落ちると check に False を代入する処理がスキップされ、 check は関数のままになります。このとき bool(check) は True となります。何故か exit(1) を呼んだ後に finally 以下の処理がなされてから終了する挙動をしていたため、これでフラグが読み取れます。
条件を満たすエラーとして、入力を b"\x00" にしました。
https://blog.y011d4.com/20221113-seccon-ctf-writeup#find-flag


type命令を上に挟んでみました。

```python
def check():

if __name__ == '__main__':
    try:
        check = check()
    except:
        print("[-] something went wrong")
        exit(1)
    finally:
        print(type(check)) # check is a boolean or function
        if check:
            print("[+] congrats!")
            print(FLAG.decode())
```

`<class 'function'>`とあるので、関数が帰ってきていることが再現できました。

```bash
% python3 solver.py    
[+] Starting local process './target': pid 74104
  conn.recvuntil("filename: ")
[+] Receiving all data: Done (68B)
[*] Process './target' stopped with exit code 0 (pid 74104)
b"[-] something went wrong\n<class 'function'>\n[+] congrats!\nSECCON{A}\n"
```

本番環境

```bash
$ python3 solver.py
[+] Opening connection to find-flag.seccon.games on port 10042: Done
  conn.recvuntil("filename: ")
[+] Receiving all data: Done (89B)
[*] Closed connection to find-flag.seccon.games port 10042
b'[-] something went wrong\n[+] congrats!\nSECCON{exit_1n_Pyth0n_d0es_n0t_c4ll_exit_sysc4ll}\n'
```

```
SECCON{exit_1n_Pyth0n_d0es_n0t_c4ll_exit_sysc4ll}
```

### 解放2

Ctrl-Dで降ってきた

```bash
$ nc find-flag.seccon.games 10042
filename: [-] something went wrong
[+] congrats!
SECCON{exit_1n_Pyth0n_d0es_n0t_c4ll_exit_sysc4ll}
```