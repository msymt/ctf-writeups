lddで不足しているライブラリのパスを通して実行したらフラグゲットです

```
as -o main.o main.s 
gcc -I./ -L./ -o main main.o -lprint
$ ldd main
        linux-vdso.so.1 (0x00007ffca1590000)
        libprint.so => not found
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f3f9b636000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f3f9bc29000)
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/vagrant/wani/rev-execute
$ ./main
Flag is "FLAG{c4n_y0u_execu4e_th1s_fi1e}"
```
