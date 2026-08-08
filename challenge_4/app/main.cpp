#include <unistd.h>

void win() {
    write(1, "FLG{_oc1v1dn3_m0c_j3dn0duch3_}\n", 32);
    _exit(0);
}

int main() {
    char buf[16];
    write(1, "Jmeno> ", 7);
    read(0, buf, 64);
    write(1, "Ahoj!\n", 6);
    return 0;
}
