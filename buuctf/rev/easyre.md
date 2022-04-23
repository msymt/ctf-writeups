# easyre

## solution

デコンパイラツールで配布されたexeファイル(easyre.exe)を開き、main関数を見ると、フラグが書かれていました。

```bash
004014f8      __main()
00401512      int32_t var_10
00401512      int32_t var_c
00401512      scanf("%d%d", &var_c, &var_10)
00401517      uint64_t rdx_1 = zx.q(var_c)
0040151f      if (rdx_1.d != var_10)
00401536          printf("sorry,you can't get flag", rdx_1)
00401528      else
00401528          printf("flag{this_Is_a_EaSyRe}", rdx_1)
0040154f      return 0
```

## FLAG

```
flag{this_Is_a_EaSyRe}
```
