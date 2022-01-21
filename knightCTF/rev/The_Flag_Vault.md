# 


```bash
The_Flag_Vault: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=8db1599916703d131749a488d7c16fd334f6a84d, for GNU/Linux 3.2.0, not stripped
```

```
# ./The_Flag_Vault

Hi there!

Please enter the password to unlock the flag vault: 1

Sorry!

You have entered a wrong password!

Please try with a valid one!

If you don't have the password, you can buy that here at https://knightsquad.org

~/ctf/knight# ./The_Flag_Vault

Hi there!

Please enter the password to unlock the flag vault: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Sorry!

You have entered a wrong password!

Please try with a valid one!

If you don't have the password, you can buy that here at https://knightsquad.org
*** stack smashing detected ***: terminated
Aborted
```

Ghidraで見てみる

```C
  local_72 = 0x4b;
  local_70 = 0x7d;
  local_6e = 0x77;
  local_6c = 99;
  local_6a = 0x30;
  local_68 = 0x54;
  local_66 = 0x46;
  local_64 = 0x43;
  local_62 = 0x5f;
  local_60 = 0x6d;
  local_5e = 0x74;
  local_5c = 0x72;
  local_5a = 0x76;
  local_58 = 0x73;
  local_56 = 0x7b;
  local_54 = 0x6e;
  local_52 = 0x33;
  local_50 = 0x65;
  local_4e = 0x67;
  local_4c = 0x6c;
  local_4a = 0x69;
  local_28 = 0x6164616361726261;
  local_20 = 0x6861686168617262;
  local_18 = 0x61;
  printf("\nHi there!\n\nPlease enter the password to unlock the flag vault: ");
  __isoc99_scanf(&DAT_00102049
local_48);
  iVar1 = strcmp((char *)&local_28
local_48);
  if (iVar1 == 0) {
    uVar2 = 0x1012d9;
    puts("\nCongratulations! Here is your flag:\n");
    printf("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n\n"
&local_72,
           &local_64,&local_68,&local_66,&local_56,&local_6e,&local_50,&local_4c,&local_6c,&local_6a
           ,&local_60,&local_50,&local_62,&local_5e,&local_6a,&local_62,&local_5c,&local_50,
           &local_5a,&local_50,&local_5c,&local_58,&local_50,&local_62,&local_52,&local_54,&local_4e
           ,&local_4a,&local_54,&local_50,&local_50,&local_5c,&local_4a,&local_54,&local_4e,
           &local_70,uVar2);
  }
```

順番に比較していることがわかったため，当てはめていきます．

```txt
4b 43 54 46 7b 77 65 6c 99 30 6d 65 5f 74 30 5f 72 65 76 65 72 73 65 5f 33 6e 67 69 6e 65 65 72 69 6e 67 7d
KCTF{wel0me_t0_reverse_3ngineering}
```

一部欠損しているため，予想します．

## FLAG

```txt
KCTF{welc0me_t0_reverse_3ngineering}
```
