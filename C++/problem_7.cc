// 实现对以上12个西瓜，拟实现“三堆均分”（每堆4个，三堆重量相等）。考虑到上述西瓜总重量不能为3所整除，这里另有几个西瓜，重量分别为：70，71，72，73，74，75可供挑选，
// 从12个西瓜中替换掉其中一个，是否可以实现“三堆均分”？如果可以，设计程序实现，要求打印输出均分的各种可能方案； 
// （a）输入：数据输入由程序完成，执行程序后不需要任何数据输入； 
// （b）输出：输出结果为以下格式，X分别代表一个西瓜重量的数字，A、B、C、D、E分别代表替换原来西瓜的新重量数字70、71、72、73、74、75，如下 ： 
// No1（A  replaces  X）：X  X  X  X，X  X  X  X，X  X  X  X
// No2（B  replaces  X）：X  X  X  X，X  X  X  X，X  X  X  X
// 98，93，57，64，50，82，18，34，69，56，16，61

// 思路：
// 暴力破解法
// 1. 将每个位置的西瓜用不同的重量替换一次
// 2. 筛选出总重量能被3整除的
// 3. 计算得出除以3之后的重量，然后尝试拼凑该重量的西瓜
// 4. 同样使用暴力破解法，但是需要两轮操作，第一轮找到4个刚好能拼凑的然后再找第二轮
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_div(int melon[]) {
    int total = 0;
    for(int i = 0; i < 12; i++) {
        total += melon[i];
    }
    int div = total / 3;
    if (total == (div * 3)) {
        return div;
    } else {
        return -1;
    }
}

// If length == 12， this is the first time, else is the second time
int** choose_four(int melon[], int length, int weight) {
    int count = 0;
    int selected[100][4];
    for(int i = 0; i < length - 3; i++) {
        for(int j = i + 1; j < length - 2; j++) {
            for(int k = j + 1; k < length - 1; k++) {
                for(int l = k + 1; l < length; l++) {
                    if(melon[i] + melon[j] + melon[k] + melon[l] == weight) {
                        selected[count][0] = i;
                        selected[count][1] = j;
                        selected[count][2] = k;
                        selected[count++][3] = l;
                    }
                }
            }
        }
    }
    int **selected_melon = (int **)malloc(sizeof(int *) * count);
    for(int i = 0; i < count; i++) {
        selected_melon[i] = (int *)malloc(sizeof(int) * 5);
        selected_melon[i][0] = selected[i][0];
        selected_melon[i][1] = selected[i][1];
        selected_melon[i][2] = selected[i][2];
        selected_melon[i][3] = selected[i][3];
    }
    if (count == 0) {
        return NULL;
    }

    selected[0][4] = count;
    return selected_melon;
}

int main() {
    int orgin_melon[12] = {98, 93, 57, 64, 50, 82, 18, 34, 69, 56, 16, 61};
    int new_melon[6] = {70, 71, 72, 73, 74, 75};

    int tmp_melon[12];
    int rest_melon[8];
    int **res_melon, **rres_melon,res_num, rres_num, weight;
    for(int i = 0; i < 6; i++) {
        for(int j = 0; j < 12; j++) {
            memcpy(tmp_melon, orgin_melon, sizeof(int) * 12);
            tmp_melon[j] = new_melon[i];
            weight = check_div(tmp_melon);
            if(weight != -1) {
                res_melon = choose_four(tmp_melon, 12, weight);
                if(res_melon != NULL) {
                    res_num = res_melon[0][4];
                }
                for(int k = 0; k < res_num; k++) {
                    int index = 0;
                    for(int t = 0; t < 12; t++) {
                        if(t != res_melon[k][0] && t != res_melon[k][1] && t != res_melon[k][2] && t != res_melon[k][3]) {
                            rest_melon[index++] = tmp_melon[t];
                        }
                    }
                    rres_melon = choose_four(rest_melon, 8, weight);
                    if(rres_melon != NULL) {
                        rres_num = rres_melon[0][4];
                    }
                    if (rres_num != 0) {
                        for(int m = 0; m < rres_num; m++) {
                            printf("%d %d %d %d, %d %d %d %d replace:%d %d\n", 
                            tmp_melon[res_melon[k][0]],  tmp_melon[res_melon[k][1]],  tmp_melon[res_melon[k][2]],  tmp_melon[res_melon[k][3]],
                            rest_melon[rres_melon[m][0]], rest_melon[rres_melon[m][1]], rest_melon[rres_melon[m][2]], rest_melon[rres_melon[m][3]], 
                            i, j);
                        }
                    }
                }
            }
        }
    }
    return 0;
}