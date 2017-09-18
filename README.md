# syms2elf for Binary Ninja

This repo is a fork of the popular [syms2elf](https://github.com/danigargu/syms2elf) plugin for IDA Pro and radare2, adapted as a [Binary Ninja](https://binary.ninja/) plugin.

## INSTALLATION

Copy the `syms2elf` folder in your `Binary Ninja` plugins folder.

## EXAMPLE

You start out with a stripped binary in `Binary Ninja`.

```bash
$ file test
test: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=354d4653de8a3089fe350d23b7c8638226791cd3, stripped
```

![Binary Ninja loaded stripped ELF](https://raw.githubusercontent.com/monosource/monosource.github.io/master/images/syms2elf_example_1.png)

Add function names

![Binary Ninja using Syms2Elf](https://raw.githubusercontent.com/monosource/monosource.github.io/master/images/syms2elf_example_2.png)

Choose a filename

![Binary Ninja Syms2Elf choosing filename](https://raw.githubusercontent.com/monosource/monosource.github.io/master/images/syms2elf_example_3.png)

Now you can use the newly written ELF in other tools.

```gdb
$ file test_with_symbols 
test_with_symbols: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=354d4653de8a3089fe350d23b7c8638226791cd3, not stripped
$ chmod u+x test_with_symbols
$ gdb ./test_with_symbols
gdb-peda$ b util_strxor
Breakpoint 1 at 0x4006ed
gdb-peda$ r 1234
========
|  HI  |
========

 [----------------------------------registers-----------------------------------]
RAX: 0x7ffcdbad0420 --> 0x0 
RBX: 0x0 
RCX: 0x17 
RDX: 0x7ffcdbad0400 ("5uper5ecret5ecret5tring")
RSI: 0x7ffcdbad108c --> 0x5f434c0034333231 ('1234')
RDI: 0x7ffcdbad0420 --> 0x0 
RBP: 0x7ffcdbad03b0 --> 0x7ffcdbad0440 --> 0x7ffcdbad0470 --> 0x4008d0 (<init>:	push   r15)
RSP: 0x7ffcdbad03b0 --> 0x7ffcdbad0440 --> 0x7ffcdbad0470 --> 0x4008d0 (<init>:	push   r15)
RIP: 0x4006ed (<util_strxor+4>:	mov    QWORD PTR [rbp-0x18],rdi)
R8 : 0x7fd5d41f7700 (0x00007fd5d41f7700)
R9 : 0xd ('\r')
R10: 0x7fd5d3ff6b78 --> 0xc3e410 --> 0x0 
R11: 0x246 
R12: 0x400530 (<_start_main>:	xor    ebp,ebp)
R13: 0x7ffcdbad0550 --> 0x2 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4006e8 <util_memcmp+86>:	ret    
   0x4006e9 <util_strxor>:	push   rbp
   0x4006ea <util_strxor+1>:	mov    rbp,rsp
=> 0x4006ed <util_strxor+4>:	mov    QWORD PTR [rbp-0x18],rdi
   0x4006f1 <util_strxor+8>:	mov    QWORD PTR [rbp-0x20],rsi
   0x4006f5 <util_strxor+12>:	mov    QWORD PTR [rbp-0x28],rdx
   0x4006f9 <util_strxor+16>:	mov    DWORD PTR [rbp-0x2c],ecx
   0x4006fc <util_strxor+19>:	mov    DWORD PTR [rbp-0x4],0x0
[------------------------------------stack-------------------------------------]
0000| 0x7ffcdbad03b0 --> 0x7ffcdbad0440 --> 0x7ffcdbad0470 --> 0x4008d0 (<init>:	push   r15)
0008| 0x7ffcdbad03b8 --> 0x4007fd (<check_key+186>:	lea    rcx,[rbp-0x60])
0016| 0x7ffcdbad03c0 --> 0x0 
0024| 0x7ffcdbad03c8 --> 0x7ffcdbad108c --> 0x5f434c0034333231 ('1234')
0032| 0x7ffcdbad03d0 --> 0x0 
0040| 0x7ffcdbad03d8 --> 0x7fd5d3ff7620 --> 0xfbad2a84 
0048| 0x7ffcdbad03e0 --> 0x60e6a0604150752 
0056| 0x7ffcdbad03e8 --> 0x11130617522b160b 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x00000000004006ed in util_strxor ()
gdb-peda$ 
```

## AUTHORS

  * Daniel García (@danigargu)
  * Jesús Olmos (@sha0coder)
