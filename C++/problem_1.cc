// 有一个数学等式：AB*CD=BA*DC，式中的一个字母代表一位数字，试找出所有符合上述要求的乘积式并打印输出。
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    for(int i = 0; i < 100; i++) {
        for(int j = 0; j < 100; j++) {
            int a, b, c, d, k, m;
            a = i / 10;
            b = i - a * 10;
            c = j / 10;
            d = j - c * 10;
            k = b * 10 + a;
            m = d * 10 + c;
            if((i * j == k * m) && (i != k && i != m && j != k && j != m) && (a != 0 && c != 0)) {
                printf("%d x %d = %d x %d\n", i, j, k, m);
            }
        }
    }
    return 0;
}