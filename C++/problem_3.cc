// 3. 附加题：编程解决如下问题（50分）。 
// （1）已知平面上三个点：（7，1）、（4，6）、（5，8），判断这三点组成的三角形是何种三角形(锐角,直角,钝角)(10分)； 
// （2）对（1）问中的三角形，给出它的外接圆半径(20分)； 
// （3）已知平面上6个点的坐标为：（7，1）、（4，6）、（5，8）、（6，2）、（3，9）、（2，7），试求覆盖这6个点的覆盖圆最小半径(20分)。 
// （要求：点坐标数据在程序初始化中赋值完成，程序运行后直接输出结果，不进行数据输入；点坐标数据和题目要求完全一致，否则导致的结果不正确视为程序编写错误。） 


#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

// 这个看起来更像是一个数学问题

typedef struct location {
    int x;
    int y;
}loc;

int sq_distance(loc location1, loc location2) {
    int x = location2.x - location1.x;
    int y = location2.y - location1.y;
    return x*x + y*y; 
}

int main() {
    loc a = {1, 1}, b = {2, 2}, c = {3, 1};
    int edge[3];
    edge[0] = sq_distance(a, b);
    edge[1] = sq_distance(a, c);
    edge[2] = sq_distance(c, b);

    int index = 0, longest = edge[0];
    for(int i = 0; i < 3; i++) {
        if(edge[i] > longest) {
            index = i;
            longest = edge[index];
        }
        printf("%d  ", edge[i]);
    }


    int sum1 = 0;
    for(int i = 0; i < 3; i++) {
        if(i != index) {
            sum1 += edge[i];
        }
    }

    int sum2 = longest;
    if(sum2 > sum1) {
        printf("dunjiao\n");
    } else if(sum1 > sum2) {
        printf("ruijiao\n");
    } else {
        printf("zhijiao\n");
    }
}
