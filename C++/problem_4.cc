// 在小于10的素数中有3、5、7组成的等差数列，在小于30的素数中有11、17、23、29组成的等差数列。
// 试找出区间[100,1000]内的素数构成的最大等差数列（即等差数列包含的素数个数最多）并打印输出。 

//先找到所有素数，然后计算素数之间的距离，找到距离相等的最长序列

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int judge_number(int number) {
    int sqt = ceil(sqrt(number));
    for(int i = 2; i <= sqt; i++) {
        if(number == ((float)(number/i) * i)) {
            return -1;
        }
    }
    return number;
}

int main() {
    int number[1000], size = 0;
    for(int i = 100; i <= 1000; i++) {
        int n = judge_number(i);
        if(n != -1) {
            number[size++] = n;
            printf("%d ", n);
        }
    }
    printf("\n");

    // 现在 number数组有size个元素 0~size-1

    // 遍历前 size-2个元素，步长从1到最后一个元素减去当前元素
    int max_length = 1;
    int last_ele = number[size - 1];
    int max_ele = number[0], max_step = 1;
    for(int i = 0; i < size - 1; i++) {
        int cur_step = last_ele - number[i];
        for(int j = 1; j < cur_step; j++) {
            int next = number[i] + j;
            int tmp_length = 1;
            while(judge_number(next) != -1 && next <= 1000) {
                tmp_length++;
                next += j;
                if (tmp_length > max_length) {
                    max_length = tmp_length;
                    max_step = j;
                    max_ele = number[i];
                }
            }
        }
    }
    printf("max_element=%d max_step=%d max_length=%d\n", max_ele, max_step, max_length);
    for(int t = 0; t < max_length; t++) {
        printf("%d ", max_ele + max_step * t);
    }
    printf("\n");
    return 0;
}