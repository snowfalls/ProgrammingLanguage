#include <stdio.h>

main() {
    FILE *fp = fopen("test.txt", "r");
    char ch;
    int space=0, tab=0, br=0;
    while((ch = fgetc(fp)) != EOF) {
        if(ch == ' ')
            space++;
        if(ch == '\r')
            tab++;
        if(ch == '\n')
            br++;
    }
    printf("空格数量:%d\ntab数量:%d\n换行数量:%d\n", space, tab, br);   
    fclose(fp);
    return 0;
}