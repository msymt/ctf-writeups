# Rev

## HelloWorld

exeを実行して、`flag` を第1引数に設置すれば良いと判断しました。

```bash
$ helloworld.exe
Nice try, please set some word when you run me.
$ helloworld.exe a
Good job, but please set 'flag' when you run me.
$ helloworld.exe flag
flag{free_fair_and_secure_cyberspace}
```

## ELF
fileコマンドを使うとdata formatが現れました。
hex editorで見るとバイナリの先頭が書き変わっていたので、修正しました。

```
58585858 XXXX
7F454C46 ELF
```

```
$ ./elf
flag{run_makiba}
```

## Passcode

`20150109`がpasscodeだと思い、入力しました。

```
$ strings ./passcode
Invalid passcode.
Invalid passcode. Too short.
Invalid passcode. Too long.
20150109
The passcode has been verified.
Flag is : flag{%s}
Invalid passcode. Nice try.

$./passcode
Enter the passcode: 20150109
The passcode has been verified.

Flag is : flag{20150109}
```

## passcode2

入力文字数の調べた後、スタック領域から順にxor 0x2a をしていました。

```c
000012b6      char var_124 = 0x18;
000012bd      char var_123 = 0x1f;
000012c4      char var_122 = 4;
000012cb      char var_121 = 0x79;
000012d2      char var_120 = 0x4f;
000012d9      char var_11f = 0x5a;
000012e0      char var_11e = 4;
000012e7      char var_11d = 0x18;
000012ee      char var_11c = 0x1a;
000012f5      char var_11b = 0x1b;
000012fc      char var_11a = 0x1e;
00001303      char var_119 = 0;
...
000013e9              int64_t var_10_1 = 0;
0000142b              while (true)
0000142b              {
00001434                  if (var_10_1 >= strlen(&var_124))
00001428                  {
00001434                      break;
00001434                  }
0000141a                  if (*(int8_t*)(var_10_1 + &var_118) != (&var_124[var_10_1] ^ 0x2a))
00001415                  {
0000141a                      break;
0000141a                  }
0000141c                  var_10_1 = (var_10_1 + 1);
0000141c              }
0000144c              if (var_10_1 != strlen(&var_124))
00001440              {
00001483                  printf("Invalid passcode. Nice try.");
00001477              }
00001455              else
00001455              {
00001455                  puts("The passcode has been verified.\n");
00001470                  printf("Flag is : flag{%s}", &var_118);
00001461              }
...
```

```python
data = ['18', '1f', '4', '79', '4f', '5a', '4', '18', '1a', '1b', '1e']

for i in data:
  print(chr(int(i, 16) ^ int('2a', 16)), end='')
print()
# 5.Sep.2014
```

`flag{}`をつければ通りました.

```
flag{5.Sep.2014}
```

## to_analyze

fileコマンドにより、Mono/.Net assemblyであることがわかりました。ある環境で動くということで、mac上かつmono, Windows上かつmono、.Netと3パターン試しましたがどれも結果は一緒。

```
$ file to_analyze.exe
to_analyze.exe: PE32 executable (console) Intel 80386 Mono/.Net assembly, for MS Windows
```

assemblyということで、C#製の逆コンパイルツールILSpyを使いました。

以下でフラグを出力してそうだったので、`Directory.Exists(A_0)`の通り`A_0`のディレクトリを作る必要があることが分かりました。

```C#
// a
using System;
using System.IO;
using System.Text;

private static void a(string A_0, byte[] A_1)
{
	if (Directory.Exists(A_0))
	{
		Console.WriteLine("Yes, that's the right answer.");
		byte[] array = new byte[27]
		{
			9, 37, 48, 34, 41, 61, 199, 49, 220, 63,
			115, 59, 220, 200, 46, 115, 57, 220, 214, 50,
			53, 46, 47, 37, 124, 62, 9
		};
		for (int i = 0; i < array.Length; i++)
		{
			array[i] ^= A_1[12];
			array[i] ^= A_1[8];
			array[i] ^= A_1[3];
			array[i] ^= 35;
			if (a(array[i], 113))
			{
				array[i] += 3;
			}
			array[i] ^= 21;
			array[i] -= 32;
			array[i] = b(array[i], 114);
		}
		Console.WriteLine(Encoding.ASCII.GetString(array));
	}
	else
	{
		Console.WriteLine("nice try!");
	}
}
```

`A_0`を生成している部分が、以下の2コードです。

```C#
// a
using System.Text;

private static void a(string[] A_0)
{
	byte[] array = new byte[15]
	{
		65, 127, 89, 80, 182, 160, 183, 182, 89, 118,
		119, 116, 177, 189, 177
	};
	for (int i = 0; i < array.Length; i++)
	{
		array[i] ^= 35;
		if (a(array[i], 119))
		{
			array[i] += 3;
		}
		array[i] ^= 21;
		array[i] -= 32;
		array[i] = b(array[i], 39);
	}
	a(Encoding.ASCII.GetString(array), array);
}

```

```C#
// a
private static bool a(byte A_0, int A_1)
{
	if (A_1 == 119)
	{
		if (A_0 == 107 || A_0 == 117 || A_0 == 108 || A_0 == 102 || A_0 == 98)
		{
			return true;
		}
	}
	else if (A_0 == 110 || A_0 == 119 || A_0 == 99 || A_0 == 111 || A_0 == 97 || A_0 == 101 || A_0 == 112 || A_0 == 103 || A_0 == 108 || A_0 == 107 || A_0 == 112 || A_0 == 113)
	{
		return true;
	}
	return false;
}
```

ここをPythonで再現すると`C:\Users\321txt`が出力しました。このディレクトリを作成後、配布されたバイナリを実行するとflagが現れました。

```python
data = [65, 127, 89, 80, 182, 160, 183, 182, 89, 118, 119, 116, 177, 189, 177]
for i in range(len(data)):
  data[i] ^= 35

for i in range(len(data)):
  A_0 = data[i]
  if(A_0 == 107 or A_0 == 117 or A_0 == 108 or A_0 == 102 or A_0 == 98):
    data[i] += 3

for i in range(len(data)):
  data[i] ^= 21

for i in range(len(data)):
  data[i] -= 32

for i in range(len(data)):
  data[i] ^= 19

for i in data:
  print(chr(i), end='') # C:\Users\321txt
```

```
$ ./to_analyze.exe
Yes, that's the right answer.

flag{Do_y0u_Kn0w_Ursnif?}
```
