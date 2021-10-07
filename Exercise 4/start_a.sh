nasm -f elf64 ./task1/hello.asm
ld ./task1/hello.o
./a.out 2>out.txt
echo "Exit code: "$? >>out.txt
rm ./task1/hello.o a.out
