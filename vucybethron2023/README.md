# VU CYBERTHON 2023 <!-- omit in toc -->

forensicが多めでした．配布ファイルがクソデカすぎて，ダウンロードに時間がめちゃくちゃ時間を要しました．
自宅の回線は平凡でこの有様だったので，他にも同じような人がいたんじゃないかと思います．

点数と難易度は釣り合っていないと思います．

https://2023.cyberthon.lt/


- [Digital Forensics/What is SHA1 checksum of image file blk0\_mmcblk0.bin ?: 10 points](#digital-forensicswhat-is-sha1-checksum-of-image-file-blk0_mmcblk0bin--10-points)
- [Crypto/Weak Password: 10 points](#cryptoweak-password-10-points)
- [OSINT/Find Location: 15 points](#osintfind-location-15-points)
- [Rev/Reverse ME: 50points](#revreverse-me-50points)


## Digital Forensics/What is SHA1 checksum of image file blk0_mmcblk0.bin ?: 10 points

Extract the archive file blk0_mmcblk0.7z. What is SHA1 checksum of the image?...

binファイルのsha-1ハッシュ値がフラグ

配布ファイル：`イメージファイル.7z`

### SOLUTION <!-- omit in toc -->

7zで圧縮されていたので，7zipで解凍しました．
あとは，sha-1ハッシュ値を求めるだけです．

```bash
# windows
cerutil -hashfile ./blk0_mmcblk0.bin
5377521a476be72837053390b24bc167d8f9182c
```

### FLAG <!-- omit in toc -->

```
VU{5377521a476be72837053390b24bc167d8f9182c}
```

## Crypto/Weak Password: 10 points

Such a password is recognized as one of the weakest passwords in the country that organizes VU Cybe..(省略)

### SOLUTION <!-- omit in toc -->

[この記事](https://lonesec.com/2021/12/07/zip_password_security/)を参考に，John the ripperを実行すると，30分ほどでパスワードを特定しました．

```bash
./zip2john ./taskweakpassword.zip > ./taskweakpassword.zip.hash
 ./john --incremental=ASCII ./taskweakpassword.zip.hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
Kaunas           (taskweakpassword.zip/taskweakpassword/about.txt)
1g 0:00:47:49 DONE (2023-02-25 21:04) 0.000348g/s 8688Kp/s 8688Kc/s 8688KC/s Kaundn..Kaunee
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

./taskweakpassword/about.txtには，以下の内容が書かれていました．

```txt
You can read about it in the research conducted (translated article):
https://www-delfi-lt.translate.goog/mokslas/technologijos/paskelbe-20-populiariausiu-slaptazodziu-lietuvoje-ar-jusiskis-sarase.d?id=86533765&_x_tr_sl=lt&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp

Your
Cyberthon Team
https://www.cyberthon.lt
```

以上から，パスワードがフラグだと思い入力すると，その通りでした．

### FLAG <!-- omit in toc -->

```
VU{Kaunas}
```

## OSINT/Find Location: 15 points

[LOCATION](https://vuknf.file.core.windows.net/vucyberthon2023/Location.jpeg?sv=2021-10-04&st=2023-02-20T12%3A21%3A10Z&se=2024-02-21T12%3A21%3A00Z&sr=f&sp=r&sig=8wpC74vfb64zxWKobYWFM48WN9FtIzbW0rhvgSXTCfI%3D)

![](./images/Location.jpeg)

### SOLTION <!-- omit in toc -->

exiftoolを使うだけ．

```bash
ExifTool Version Number         : 12.42
File Name                       : Location.jpeg
Directory                       : .
File Size                       : 253 kB
File Modification Date/Time     : 2023:02:25 21:28:57+09:00
File Access Date/Time           : 2023:02:25 21:29:20+09:00
File Inode Change Date/Time     : 2023:02:25 21:29:14+09:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
XMP Toolkit                     : FILE
Location                        : VU{d5bc0961009b25633293206cde4ca1e0}
...
```

### FLAG <!-- omit in toc -->

```
VU{d5bc0961009b25633293206cde4ca1e0}
```

## Rev/Reverse ME: 50points

（loginとpasswordがそのままフラグになる云々と書かれていました）．

配布ファイル：Task-ReverseME(ELF)

### SOLUTION <!-- omit in toc -->

binjaで配布されたファイルを開くと，標準入力から受け取った値が`0x3f1`かつ`0x62b`のとき，`sucess`関数を呼び出していました．そこでそれぞれ，10進数に変換しました．

```c
000011dd  int32_t main(int32_t argc, char** argv, char** envp)

000011dd  {
000011e9      void* fsbase;
000011e9      int64_t rax = *(int64_t*)((char*)fsbase + 0x28);
000011f8      int32_t var_20 = 0;
000011ff      int32_t var_1c = 0;
00001206      int32_t var_18 = 0x3f1;
0000120d      int32_t var_14 = 0x62b;
00001223      printf("Enter login:");
0000123e      __isoc99_scanf(&data_2058, &var_20);
00001252      printf("Enter password:");
0000126d      __isoc99_scanf(&data_2058, &var_1c);
00001284      if ((0x3f1 != var_20 || (0x3f1 == var_20 && 0x62b != var_1c)))
0000127f      {
00001297          fail();
00001297      }
00001284      if ((0x3f1 == var_20 && 0x62b == var_1c))
0000127f      {
0000128b          success();
0000128b      }
000012a5      *(int64_t*)((char*)fsbase + 0x28);
000012ae      if (rax == *(int64_t*)((char*)fsbase + 0x28))
000012a5      {
000012b6          return 0;
000012b6      }
000012b0      __stack_chk_fail();
000012b0      /* no return */
000012b0  }
```

### FLAG <!-- omit in toc -->

```
VU{1009,1579}
```
