# Windows memory dump

## Description

250

A Windows computer has been infected. The attacker managed to exploit a portion of a database backup that contains sensitive employee and customer private information. All memory dump challenges use the same file.
Inspect the memory dump and tell us the Windows Major Operating System Version, bit version, and the image date/time (UTC, no spaces or special characters). Submit the flag as OFPPT-CTF{OS_BIT_YYYYMMDDhhmmss}. 

Example: OFPPT-CTF{WindowsXP_32_20220120095959} File: 1.5 GB Decompressed: 5 GB

## writeup

Suggested Profile(s) : Win10x64_19041
Image date and time : 2021-09-07 14:57:44 UTC+0000

から、

Example: OFPPT-CTF{WindowsXP_32_20220120095959}

を参考にフォーマットをかけると、`OFPPT-CTF{Windows10_64_20210907145744}` となる。


```bash
$ python2 vol.py -f /example/physmemraw imageinfo                                   
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...

          Suggested Profile(s) : Win10x64_19041
                     AS Layer1 : SkipDuplicatesAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/example/physmemraw)
                      PAE type : No PAE
                           DTB : 0x1aa000L
                          KDBG : 0xf8005e600b20L
          Number of Processors : 4
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0xfffff8005ba60000L
                KPCR for CPU 1 : 0xffff82804f9c0000L
                KPCR for CPU 2 : 0xffff82804f5e8000L
                KPCR for CPU 3 : 0xffff82804f7ca000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2021-09-07 14:57:44 UTC+0000
     Image local date and time : 2021-09-07 07:57:44 -0700
```

## FLAG

```bash
OFPPT-CTF{Windows10_64_20210907145744}
```
