#include<stdio.h>

struct t {
    char c;
    int a;
    char b;
};

int main() {
    struct t test;
    printf("%d byte\n", sizeof(test));
}