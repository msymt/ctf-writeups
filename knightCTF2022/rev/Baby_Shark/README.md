# Baby Shark

## description

50

During my holiday in Bahamas, I met a baby shark. The shark wanted to sing me something but couldn't. Can you sing that for me?


Flag Format: KCTF{S0m3_T3xt_H3re}

Author: fazledyn

## writeup

jarファイルをデコンパイルすると，babyshark.jar -> kctf -> flag -> Flag.javaにてフラグがハードコードされていましたが，こちらは偽物でした．

実際は，kctf -> constants -> String.javaにてフラグがbase64でエンコードされてました．

```java
/*
 * Decompiled with CFR 0.150.
 */
package kctf.constants;

public class Strings {
    public static final String _0xf1a6 = "7P0HJKddEnGG==";
    public static final String _0xflac = "LoE2301mP00FZFWeEQJJR==";
    public static final String _0xface = "N5tFdK18ZKN0442LDVZXSWE7k71Dfr==";
    public static final String _0xfj23 = "ns3PTTDkVYsslUI==";
    public static final String _0xfka6 = "rN88230S8892KL332GDxV1DK=";
    public static final String _0xflag = "S0NURns3SDE1X1dANV8zNDVZX1IxNkg3P30=";
}
```

## FLAG

```txt
KCTF{7H15_W@5_345Y_R16H7?}
```
