#include<stdio.h>
#define FUN(x, y) ((x+y)*(x+y))

int main() {
    int x = 1, y = 2;
    int z = FUN(x, y);
    printf("z = %d", z);
    return 0;
}