//1,2,3,4分别能组成多少个不同的数字，要求这些数字各不相同
#include<stdio.h>

int main() {
    int a[1000];
    int index = 0, tmp, rp_flag = 0;
    for(int i = 1; i < 5; i++) {
        for(int j = 1; j < 5; j++) {
            for (int k = 1; k < 5; k++) {
                tmp = i * 100 + j * 10 + k;
                for (int t = 0; t < index; t++) {
                    if(a[t] == tmp) {
                        rp_flag = 1;
                        break;
                    }
                }
                if(rp_flag != 1) {
                    a[index++] = tmp;
                    printf("%d\n", tmp);
                }
                else {
                    rp_flag = 0;
                }
            }
        }
    }
    printf("total number:%d\n", index);
}