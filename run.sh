echo -e "______________________________________________________________\n\n\n\n"

cmake -B build
make -C build
./build/test-1

echo -e "\n Fin :)"