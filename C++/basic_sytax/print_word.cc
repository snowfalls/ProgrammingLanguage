#include <stdio.h>

int main() {
    FILE *fp = fopen("test.txt", "r");
    char ch, change_line = 0;
    while((ch = fgetc(fp)) != EOF) {
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            change_line = 0; 
            printf("%c", ch);
        }
        else if (change_line == 0){
            printf("\n");
            change_line = 1;
        }
    }
}