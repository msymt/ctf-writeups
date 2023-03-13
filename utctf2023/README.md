# UTCTF 2023 <!-- omit in toc -->

https://www.isss.io/utctf/

- [network part1](#network-part1)
- [network part2](#network-part2)


## network part1

netcatするだけ

## network part2

Update: smb port has been moved to 8445 from 445 on networking-misc-p2
betta.utctf.live has other interesting ports. Lets look at 8445 this time. By Robert Hill (@Rob H on discord)
betta.utctf.live:8445

### SOLUTION <!-- omit in toc -->

Finderで`smb://betta.utctf.live`にアクセスすると，マウントするボリューム`Backups`か`WorkShares`のどちらかを選ぶことになりました．後者を選ぶと，ディレクトリの構造が以下だとわかりました．

```bash
/Volumes/WorkShares/shares
.
├── Advertising
│   ├── Advertising Plan
│   └── Logos
│       └── JACT.png
├── IT
│   └── Itstuff
│       └── notetoIT
└── OfficeFun
    └── JaysCats
        └── Meowfoy.jpg
```

`notetoIT`を開くとフラグが書かれていました．

```
I don't understand the fasination with the magic phrase "abracadabra", but too many people are using them as passwords. Crystal Ball, Wade Coldwater, Jay Walker, and Holly Wood all basically have the same password. Can you please reach out to them and get them to change thier passwords or at least get them append a special character? 

-- Arty F.

utflag{out-of-c0ntrol-access}
```

### FLAG <!-- omit in toc -->

```
utflag{out-of-c0ntrol-access}
```