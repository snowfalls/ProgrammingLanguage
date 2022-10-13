#include <stdio.h>

enum location {xian, shanghai=1000, beijign, wuhan, chongqing};

union test {
    int a;
    char b;
}; //union used a shared location of memory so when writing the location the coverage may happen

int main() {
    

    enum location a = wuhan;
    printf("location: %d\n", a);

    union test t;
    t.b = 'a';
    t.a = 10;
 
    printf("%c\n", t.b);

    // int a = 0;
    // if(a<>0) {
    //     printf("a is not 0");
    // } // we cannot write != as the above format
}