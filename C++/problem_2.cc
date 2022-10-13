// 请在整数n=742683613984中删除8个数字，使得余下的数字按原次序组成的新数最小。要求如下:
// （1）整数n和删除数字的个数“8”在源程序中完成赋值，程序直接输出运行结果； 
// （2）程序结果输出先后被删除的数字（之间以逗号分隔）和删除后所得的最小数。

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 这个问题其实是比较好解决的，因为这个程序中的后面4个数字要组成一个完整的数字，就需要保证最前面的那个数字最小，其实找出前8个数字中最小的一个作为这个数字的
// 最高位



int main() {
    char number[20] = "742683613984";
    // 找到前9个数字中最小的数

    int index1 = 0;
    char min = '9';
    for(int i = 0; i < 9; i++) {
        if(number[i] < min) {
            index1 = i;
            min = number[i];
        }
    }

    int index2 = index1;
    min = '9';
    for(int i = index1 + 1; i < 10; i++) {
        if(number[i] < min) {
            index2 = i;
            min = number[i];
        }
    }

    int index3 = index2;
    min = '9';
    for(int i = index2 + 1; i < 11; i++) {
        if(number[i] < min) {
            index3 = i;
            min = number[i];
        }
    }

    int index4 = index3;
    min = '9';
    for(int i = index3 + 1; i < 12; i++) {
        if(number[i] < min) {
            index4 = i;
            min = number[i];
        }
    }

    printf("deleted number:");
    for(int i = 0; i < 12; i++) {
        if(i != index1 && i != index2 && i != index3 && i != index4) {
            printf("%c", number[i]);
        }
    }
    printf("\n");

    printf("the rest number:");
        for(int i = 0; i < 12; i++) {
        if(i == index1 || i == index2 || i == index3 || i == index4) {
            printf("%c", number[i]);
        }
    }
    printf("\n");
}