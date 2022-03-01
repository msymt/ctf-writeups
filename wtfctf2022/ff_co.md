# FF.CO

139

Mr F is starting a new company named FF.C0, an important and essential image file document is acting weird. He needs your help to help figure it out. A flag maybe your reward!

Author: Ilham

## 解法

exiftoolをhint.jpegに対して適用すれば、フラグが出てきました。

```bash
$ exiftool ./hint.jpg > out.txt | cat out.txt
ExifTool Version Number         : 12.30
File Name                       : hint.jpg
Directory                       : .
File Size                       : 50 KiB
File Modification Date/Time     : 2022:02:27 23:53:33+09:00
File Access Date/Time           : 2022:02:27 23:57:58+09:00
File Inode Change Date/Time     : 2022:02:27 23:57:27+09:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Little-endian (Intel, II)
Orientation                     : Horizontal (normal)
X Resolution                    : 96
Y Resolution                    : 96
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0210
Components Configuration        : Y, Cb, Cr, -
Flashpix Version                : 0100
Color Space                     : Uncalibrated
Exif Image Width                : 1920
Exif Image Height               : 1080
Ads Created                     : 2021-12-25
Ads Ext Id                      : 4e5bc376-1250-4971-aae8-4918738abcfc
Ads Fb Id                       : 525265914179580
Ads Touch Type                  : 2
Title                           : wtfctf{IHDR_h34d3r_w4s_th3_k3y}
Author                          : Ilham Rahm
Creator Tool                    : Canva
Image Width                     : 350
Image Height                    : 130
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 1
Image Size                      : 350x130
Megapixels                      : 0.045
```

## FLAG

```bash
wtfctf{IHDR_h34d3r_w4s_th3_k3y}
```
