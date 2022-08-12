#include<stdio.h>
#include<malloc.h>

#define WIDTH 50
#define HEIGHT 50


bool **screen_buffer;

int init_screen_buffer() {
    screen_buffer = (bool**)malloc(HEIGHT * sizeof(bool *));
    for (int i = 0 ; i < HEIGHT; i++) {
        screen_buffer[i] = (bool*)malloc(WIDTH * sizeof(bool));
    }
    for(int i = 0;i < HEIGHT; i++) {
        for(int j = 0; j < WIDTH; j++) {
            if(i == 0 || i == HEIGHT-1) {
                screen_buffer[i][j] = 1;
            }
            else if(j == 0 || j == WIDTH - 1){
                screen_buffer[i][j] = 1;
            }
            else {
                screen_buffer[i][j] = 0;
            }
        }
    }
    return 0;
}

int show_buffer() {
    for(int i = 0; i < HEIGHT; i++) {
        for(int j = 0; j < WIDTH; j++) {
            if (screen_buffer[i][j] == 1) {
                printf("#");
            }
            else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    init_screen_buffer();
    show_buffer();
}