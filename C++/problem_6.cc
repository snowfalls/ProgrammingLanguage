// 2．求西瓜均分问题。（70分） 
// 描述：地面上有12个西瓜，它们的重量（单位为“两”，为计算方便已全部转化为整数，如98即为9斤8两）如下： 
// 98，93，57，64，50，82，18，34，69，56，16，61
// （1）设计程序：实现对以上12个瓜“二堆均分”（每堆6个，两堆重量相等），要求打印输出均分的各种可能方案； 
// （a）输入：数据输入由程序完成，执行程序后不需要任何数据输入； 
// （b）输出：程序执行后输出以下格式， X分别代表一个西瓜重量的数字，如下： 
// No1：X  X  X  X  X  X，X  X  X  X  X  X
// No2：X  X  X  X  X  X，X  X  X  X  X  X
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//使用暴力破解法，首先计算出总重量一半的重量，然后从12个重量中挑出6个进行组合
//使用一个6重for循环来进行筛选，其中第一个筛选第一个位置上应该填充的西瓜，然后后面以此选择后面5个位置防止的西瓜，从直观上看似乎
//不一定能遍历所有的情况

//换一种思路，先让第一个选，然后后面接着选，这样似乎复杂度提高了，我们可以尝试两种方法的结果

void select_melon(int melon[], int half_weight) {
    for(int i = 0; i < 7; i++) {
        for(int j = i + 1; j < 8; j++) {
            for(int k = j + 1; k < 9; k++) {
                for(int l = k + 1; l < 10; l++) {
                    for(int m = l + 1; m < 11; m++) {
                        for(int n = m + 1; n < 12; n++) {
                            if(melon[i] + melon[j] + melon[k] + melon[l] + melon[m] + melon[n] == half_weight) {
                                printf("%d %d %d %d %d %d,", melon[i], melon[j], melon[k], melon[l], melon[m], melon[n]);
                                for(int p = 0; p < 12; p++) {
                                    if(p != i && p!= j && p!=k && p!= l && p!=m && p!= n) {
                                        printf("%d ", melon[p]);
                                    }
                                }
                                printf("\n");
                            }
                        }
                    }
                }
            }
        }
    }
}

void select_melon2(int melon[], int half_weight) {
    for(int i = 0; i < 12; i++) {
        for(int j = 0; j < 12; j++) {
            if(i != j) {
                for(int k = 0; k < 12; k++) {
                    if(k != i && k != j) {
                        for(int l = 0; l < 12; l++) {
                            if(l != i && l != j && l != k) {
                                for(int m = 0; m < 12; m++) {
                                    if(m != i && m != j && m != k && m != l) {
                                        for(int n = 0; n < 12; n++) {
                                            if(n != i && n != j && n != k && n != l && n != m) {
                                                if(melon[i] + melon[j] + melon[k] + melon[l] + melon[m] + melon[n] == half_weight) {
                                                    printf("%d %d %d %d %d %d\n", melon[i], melon[j], melon[k], melon[l], melon[m], melon[n]);
                                                    printf("%d, %d\n", half_weight, melon[i] + melon[j] + melon[k] + melon[l] + melon[m] + melon[n]);
                                                }
                                            } 
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

}

int main() {
    int melon[12] = {98, 93, 57, 64, 50, 82, 18, 34, 69, 56, 16, 61};
    // 0~11
    int half_weight = 0;
    for(int i = 0; i < 12; i++) {
        half_weight += melon[i];
    }
    half_weight /= 2;

    select_melon(melon, half_weight);
    return 1;
}