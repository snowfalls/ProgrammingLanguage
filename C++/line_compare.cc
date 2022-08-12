/*打印两个文本中第一个不同的行*/

#include <stdio.h>
#include <string.h>

int main() {
    FILE *fp_f = fopen("first.txt", "r");
    FILE *fp_s = fopen("second.txt", "r");
    char line[1000], line2[1000];
    char *l_f, *l_s;
    do {
        l_f = fgets(line, 1000, fp_f);
        l_s = fgets(line2, 1000, fp_s);
    } while(l_f && l_s && !strcmp(line, line2));
    if(!strcmp(line, line2)) {
        printf("identical txt");
    } else if (l_f == NULL || l_s == NULL) {
        printf("one of the txt is shorter");
    } else {
        printf("%s\n", line);
        printf("%s", line2);
    }
}