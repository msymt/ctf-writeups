# Royalty

## Description

201

This image has some special rights! Find the flag?

## writeup

exiftoolを使うと、copyrightのとこにbase64でエンコードされた文字列が出てきました。デコードするとflagでした。

```bash
 exiftool ./image.png
ExifTool Version Number         : 11.88
File Name                       : image.png
Directory                       : .
File Size                       : 199 kB
File Modification Date/Time     : 2022:01:30 23:50:52+00:00
File Access Date/Time           : 2022:03:24 13:18:52+00:00
File Inode Change Date/Time     : 2022:03:24 13:18:48+00:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 677
Image Height                    : 273
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Pixels Per Unit X               : 3780
Pixels Per Unit Y               : 3780
Pixel Units                     : meters
Copyright Notice                : T0ZQUFR7M3gxZnQwMGxfdDBfY2g0bmczX20zdDRkNHQ0fQ==
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 12.39
Creator                         : Creator
Rights                          : ©2012 John Doe, all rights reserved
Image Size                      : 677x273
Megapixels                      : 0.185
```

## FLAG

```bash
OFPPT{3x1ft00l_t0_ch4ng3_m3t4d4t4}
```
