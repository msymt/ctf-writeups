# I Love Java

## description

Can you Java?

Author: TSBloxorz
Difficulty: Medium

## solution

デコンパイラツールでclassファイルを開くと、最後のif文で、ある数字列と処理が施された入力値を比較している箇所がありました．
```java
if (s.equals("116.122.54.50.93.66.98.117.75.51.97.78.104.119.90.53.94.36.105.84.40.69."))
```

```Java
import java.util.Random;
import java.util.Scanner;

public class CrackMe
{
    public static void main(final String[] array) {
        final Scanner scanner = new Scanner(System.in);
        System.out.println("What is the flag?");
        final String nextLine = scanner.nextLine();
        if (nextLine.length() != 22) {
            System.out.println("Not the flag :(");
            return;
        }
        final char[] array2 = new char[nextLine.length()];
        for (int i = 0; i < nextLine.length(); ++i) {
            array2[i] = nextLine.charAt(i);
        }
        for (int j = 0; j < nextLine.length() / 2; ++j) {
            final char c = array2[nextLine.length() - j - 1];
            array2[nextLine.length() - j - 1] = array2[j];
            array2[j] = c;
        }
        final int[] array3 = { 19, 17, 15, 6, 9, 4, 18, 8, 16, 13, 21, 11, 7, 0, 12, 3, 5, 2, 20, 14, 10, 1 };
        final int[] array4 = new int[array2.length];
        for (int k = array3.length - 1; k >= 0; --k) {
            array4[k] = array2[array3[k]];
        }
        final Random random = new Random();
        random.setSeed(431289L);
        final int[] array5 = new int[nextLine.length()];
        for (int l = 0; l < nextLine.length(); ++l) {
            array5[l] = (array4[l] ^ random.nextInt(l + 1));
        }
        String s = "";
        for (int n = 0; n < array5.length; ++n) {
            s = invokedynamic(makeConcatWithConstants:(Ljava/lang/String;I)Ljava/lang/String;, s, array5[n]);
        }
        System.out.println(invokedynamic(makeConcatWithConstants:(Ljava/lang/String;)Ljava/lang/String;, s));
        if (s.equals("116.122.54.50.93.66.98.117.75.51.97.78.104.119.90.53.94.36.105.84.40.69.")) {
            System.out.println("Congrats! You got the flag!");
        }
        else {
            System.out.println("Not the flag :(");
        }
    }
}
```

適当に22文字入力すると以下のように帰ってきました。

```bash
$java CrackMe
What is the flag?
aaaaaaaaaaaaaaaaaaaaaa

YOUR FLAG: 97.96.99.96.99.100.101.96.96.102.98.102.97.107.100.100.96.113.107.99.109.112.
Not the flag :(
```

22文字に対して、入力値と変換後がどこかで一対一に対応していると思い、`bctf{aaaaaaaaaaaaaaaa}`を初期値として、`{}`の中身を総当たりしました。

```
import subprocess, sys, string

data = [116,122,54,50,93,66,98,117,75,51,97,78,104,119,90,53,94,36,105,84,40,69]
# 最初はbctf{aaaaaaaaaaaaaaaa}
flag = 'bctf{J4V4_I$_th3_G04T}'
index = -1 # ここを書き換える(5, 20)

for i in string.printable:
  flag = flag[:index] + i + flag[index+1:]
  cp = subprocess.run(['java', 'CrackMe'], input=flag, encoding='utf-8', stdout=subprocess.PIPE)
  out = cp.stdout.splitlines()[2]
  out_array = out.split('.')
  out_array[0] = out_array[0][11:]
  print(flag, str(i), out_array)
```

stdoutに以下のような結果が現れるため、目grepでどの入力値が正しいのか確認しました。

```bash
bctf{J4V4_I$_th3_G04T} 0 ['116', '122', '54', '50', '93', '66', '98', '117', '75', '51', '97', '78', '104', '119', '90', '53', '94', '36', '105', '84', '40', '69', '']
bctf{J4V4_I$_th3_G14T} 1 ['116', '122', '54', '50', '93', '66', '98', '117', '75', '51', '97', '78', '104', '119', '90', '52', '94', '36', '105', '84', '40', '69', '']
bctf{J4V4_I$_th3_G24T} 2 ['116', '122', '54', '50', '93', '66', '98', '117', '75', '51', '97', '78', '104', '119', '90', '55', '94', '36', '105', '84', '40', '69', '']
bctf{J4V4_I$_th3_G34T} 3 ['116', '122', '54', '50', '93', '66', '98', '117', '75', '51', '97', '78', '104', '119', '90', '54', '94', '36', '105', '84', '40', '69', '']
```

## FLAG

```
bctf{J4V4_I$_th3_G04T}
```
