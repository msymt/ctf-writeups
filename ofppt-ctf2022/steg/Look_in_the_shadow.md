# Look in the shadow

## Description

327

We received a suspicious png file! Can you find a hidden message?

## writeup

exiftool, binwalk, stegonlineを試しましたが特に情報が得られず。

そこで、steghideを使い、パスワードは無しでやってみると解けました。

```bash
$ steghide extract -sf  ./LookInTheShadows.jpg
Enter passphrase:
the file "secret.txt" does already exist. overwrite ? (y/n)

steghide: did not write to file "secret.txt".
$ cat secret.txt
OFPPT-CTF{3mb3dd3d_H1dd3n_73x7_d4t4}
```

## FLAG

```bash
OFPPT-CTF{3mb3dd3d_H1dd3n_73x7_d4t4}
```
