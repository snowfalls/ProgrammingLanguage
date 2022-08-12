//这是一个用来测试链表的程序
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct _node{
    int data;
    struct _node *next;
}node;

node *head = NULL, *tail = NULL;

int stoi(char str[]) {
    int res = 0, len = 0, p = 1;
    while(str[len] != '\0')len++;
    len--;
    while(len >= 0) {
        res += (str[len--] - '0') * p;
        p *= 10;
    }
    return res;
}

void add_node(int data) {

    node *new_tail = (node *)malloc(sizeof(node));
    new_tail->data = data;
    new_tail->next = NULL;
    if (head == NULL) {
        head = new_tail;
        tail = new_tail;
        return;
    }
    tail->next = new_tail;
    tail = new_tail;
}

void delete_node(int data) {
    node *tmp = head, *prev = NULL;
    while(tmp != NULL) {
        if(tmp->data == data) {
            if(prev != NULL)
                prev->next = tmp->next;
            else
                head = head->next;
        }
        prev = tmp;
        tmp = tmp->next;

    }
}

void print(node *head) {
    node *tmp = head;
    while(tmp != NULL) {
        printf("%d->", tmp->data);
        tmp = tmp->next;
    }
    printf("\n");
}

int main() {
    char str[10];
    int data;
    while(1) {
        scanf("%s", str);
        if(!strcmp(str, "add")) {
            scanf("%d", &data);
            add_node(data);
        }
        else if(!strcmp(str, "del")) {
            scanf("%d", &data);
            delete_node(data);
        }
        else if(!strcmp(str, "exit")) {
            break;
        }
        else if(!strcmp(str, "print")) {
            print(head);
        } 
        else {
            printf("wrong string\n");
            continue;
        }
    }
}