//一个整数，加100是完全平方数，再加168也是完全平方数
#include <stdio.h>
#include <math.h>

int main() {
    int t1, t2;
    for(int i = 0; i <= 100000; i++) {
        t1 = sqrt(i + 100);
        t2 = sqrt(i + 168);
        if((t1 * t1 == i + 100) && (t2 * t2 == i + 168)) {
            printf("the right number: %d\n", i);
        }
    }
}