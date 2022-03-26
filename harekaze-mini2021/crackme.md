# Reversing crackme

## 問題文

入力した文字列がフラグか判定してくれるようです。

## writeup

フラグが31文字以内の時，calc関数を呼び出してフラグ判定を行なってましたが，解読しきれなかったため，angrに頑張ってもらいました．

```Python
import angr
import claripy
src = "./crackme"
base_addr = 0x400000
find_addr = base_addr + 0x125f  # correct address
avoid_addr = base_addr + 0x1229  # incorrect address

proj = angr.Project(src, auto_load_libs=False)
length = 31
flag = claripy.BVS("flag", length*8)
state = proj.factory.entry_state(args=[src, flag])
simgr = proj.factory.simulation_manager(state)
simgr.explore(find=find_addr, avoid=avoid_addr)

try:
    simstate = simgr.found[0]
    print(simstate.posix.dumps(1))
    print(simstate.solver.eval(flag, cast_to=bytes))
except Exception as e:
    print(e)
```

## FLAG

```bash
HarekazeCTF{quadrat1c_3quati0n}
```
