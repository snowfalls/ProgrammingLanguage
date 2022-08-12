#include <stdio.h>
#include <string.h>

struct student{
    int age;
    int height;
    char name[20];
};

int main() {
    struct student dbc;
    dbc.age = 30;
    dbc.height = 185;
    strcpy(dbc.name , "dangbochao");

    printf("age:%d  height:%d name: %s\n", dbc.age, dbc.height, dbc.name);
}