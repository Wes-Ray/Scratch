#include <stdio.h>

int main() {

    int x = 0xF0;

    // printf("%x", x & (1 << 7));
    x |= 1;
    printf("%x\n", x);
    x &= ~1;
    printf("%x\n", x);

    return 0;
}