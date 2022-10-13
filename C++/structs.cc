#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct student {
    char name[20];
    int age;
    char sex[20];
    int score;
}stu;

//先写固定参数，下午写可变参数
int main(int argc, char *argv[]) {
    printf("how many students?");
    int number;
    scanf("%d", &number);

    stu *students = (stu *)malloc(number * sizeof(stu));

    for(int i = 0; i < number; i++) {
        scanf("%s%d%s%d", students[i].name, &students[i].age, students[i].sex, &students[i].score);
    }

    printf("输出学生信息:\n");
    for(int i = 0; i < number; i++) {
        // printf("This is the %d student:\n", i + 1);
        printf("name:%s\nage:%d\nsex:%s\nscore:%d\n", students[i].name, students[i].age, students[i].sex, students[i].score);
    } // the problem is that the printf type must be exact and shouldn't have any mis lead

    free(students);
    return 0;
}