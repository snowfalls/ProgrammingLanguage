// 1．求某正整数插入乘号后乘积的最大值。（50分） 
// 1.	描述：编程实现在一个9位数的正整数n中插入4个乘号，使分得的5个整数的乘积最大； 
// 2.	输入：正整数n； 
// 3.	输出：被分得的5个整数、得到的最大乘积值。 
// 例如： 
// Please input n：734019862  （回车） 
// 屏幕输出：73*401*9*8*62=130674672

// 如果是一个9位正整数那么int类型足够进行存储，我们这里使用字符串进行存放

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<assert.h>


int multi(char num[], int p1, int p2, int p3, int p4, int p5) {
    int s1 = 0, s2 = 0, s3 = 0, s4 = 0, s5 = 0;
    int index = 0;
    while(p1 >= 1) {
        s1 += (num[index++] - '0') * p1;
        p1 /= 10;
    }

    while(p2 >= 1) {
        s2 += (num[index++] - '0') * p2;
        p2 /= 10;
    }

    while(p3 >= 1) {
        s3 += (num[index++] - '0') * p3;
        p3 /= 10;
    }

    while(p4 >= 1) {
        s4 += (num[index++] - '0') * p4;
        p4 /= 10;
    }

    while(p5 >= 1) {
        s5 += (num[index++] - '0') * p5;
        p5 /= 10;
    }
    assert(index == 9);
    return s1 * s2 * s3 * s4 * s5;
}


int main() {
    char number[10];
    printf("please input a number:\n");
    scanf("%s", number);
    int max = 0, max_i, max_j, max_k, max_t;
    for(int i = 1; i < 5; i++) {
        int p1 = 1, ti = i;
        while(ti != 1) {ti--; p1*=10;}
        for(int j = 1; j < 6 - i; j++) {
            int p2 = 1, tj = j;
            while(tj != 1) {tj--; p2*=10;}
            for(int k = 1; k < 7 - i - j; k++) {
                int p3 = 1, tk = k;
                while(tk != 1) {tk--; p3*=10;}
                for(int t = 1; t < 8 - i - j - k; t++) {
                   
                    int p4 = 1, tt = t;
                    while(tt != 1) {tt--; p4*=10;}
                    int p5 = 1, ll = 9 - i - j - k - t;
                    while(ll != 1) {ll--; p5*=10;}
                     printf("%d %d %d %d %d\n", p1, p2, p3, p4, p5);
                    int tmp = multi(number, p1, p2, p3, p4, p5);
                    printf("tmp:%d\n", tmp);
                    if(tmp > max) {
                        max = tmp;
                        max_i = i;
                        max_j = j;
                        max_k = k;
                        max_t = t;
                        printf("%d %d %d %d\n", i, j, k, t);
                    }
                }
            }
        }
    }

    int index = 0;
    while(number[index] != 0) {

        if(index == max_i) {
            printf("x");
        }
        if(index == max_i + max_j) {
            printf("x");
        }
        if(index == max_i + max_j + max_k) {
            printf("x");
        }
        if(index == max_i + max_j + max_k + max_t) {
            printf("x");
        }
        printf("%c", number[index]);
        index++;
    }
    printf("=%d\n", max);
}