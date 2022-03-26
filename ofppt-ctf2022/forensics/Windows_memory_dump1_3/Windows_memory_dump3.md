# Windows memory dump3

## Description

250

Using the memory dump file from Window memory dump challenge, find out the name of the malicious process.

Submit the flag as OFPPT-CTF{process-name_pid} (include the file extension). 

Example: OFPPT-CTF{svchost.exe_1234}

## writeup

malfindオプションにより、コードが書き換えられた可能性のある不審なプロセスを確認すると、`Process: userinit.exe Pid: 8180 Address: 0x500000`にて、PEファイルのシグネチャであるMZが見えました。このため、PEファイルがメモリ上に展開されていることから、不審なプロセスと判断しました。

```bash
Process: userinit.exe Pid: 8180 Address: 0x500000
Vad Tag: VadS Protection: PAGE_EXECUTE_READWRITE
Flags: PrivateMemory: 1, Protection: 6

0x0000000000500000  4d 5a e8 00 00 00 00 5b 52 45 55 89 e5 81 c3 14   MZ.....[REU.....
0x0000000000500010  45 00 00 ff d3 81 c3 e5 62 02 00 89 3b 53 6a 04   E.......b...;Sj.
0x0000000000500020  50 ff d0 00 00 00 00 00 00 00 00 00 00 00 00 00   P...............
0x0000000000500030  00 00 00 00 00 00 00 00 00 00 00 00 f0 00 00 00   ................

0x0000000000500000 4d               DEC EBP
0x0000000000500001 5a               POP EDX
0x0000000000500002 e800000000       CALL 0x500007
0x0000000000500007 5b               POP EBX
0x0000000000500008 52               PUSH EDX
0x0000000000500009 45               INC EBP
0x000000000050000a 55               PUSH EBP
0x000000000050000b 89e5             MOV EBP, ESP
0x000000000050000d 81c314450000     ADD EBX, 0x4514
0x0000000000500013 ffd3             CALL EBX
0x0000000000500015 81c3e5620200     ADD EBX, 0x262e5
0x000000000050001b 893b             MOV [EBX], EDI
0x000000000050001d 53               PUSH EBX
0x000000000050001e 6a04             PUSH 0x4
0x0000000000500020 50               PUSH EAX
0x0000000000500021 ffd0             CALL EAX
0x0000000000500023 0000             ADD [EAX], AL
0x0000000000500025 0000             ADD [EAX], AL
0x0000000000500027 0000             ADD [EAX], AL
0x0000000000500029 0000             ADD [EAX], AL
0x000000000050002b 0000             ADD [EAX], AL
0x000000000050002d 0000             ADD [EAX], AL
0x000000000050002f 0000             ADD [EAX], AL
0x0000000000500031 0000             ADD [EAX], AL
0x0000000000500033 0000             ADD [EAX], AL
0x0000000000500035 0000             ADD [EAX], AL
0x0000000000500037 0000             ADD [EAX], AL
0x0000000000500039 0000             ADD [EAX], AL
0x000000000050003b 00f0             ADD AL, DH
0x000000000050003d 0000             ADD [EAX], AL
0x000000000050003f 00               DB 0x0
```

## FLAG

```bash
OFPPT-CTF{userinit.exe_8180}
```
