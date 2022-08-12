// 各种排序
#include <stdio.h>
#include <malloc.h>
#include <string.h>

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

void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void bubble_sort(int *arr, int size) {
    for(int i = size; i > 0; i--) {
        for(int j = 1; j < i; j++) {
            if(arr[j] < arr[j - 1]) {
                swap(arr[j], arr[j - 1]);
            }
        }
    }
}

// 这个方法并不高效，但是是自己实现的，官方的版本更高效一些
void quick_sort(int *arr, int left, int right) {
    if(left >= right) return;
    int or_left = left, or_right = right;

    int mid = (left + right) / 2;
    int tmp = arr[mid];
    while(left < right) {
        while(arr[left] < tmp) left++;
        while(arr[right] > tmp) right--;
        swap(arr[left++], arr[right--]);
    }
    quick_sort(arr, or_left, mid);
    quick_sort(arr, mid + 1, or_right);
}

void oswap(int v[], int i, int j) {
    int tmp = v[i];
    v[i] = v[j];
    v[j] = tmp;
}

// 官方实现的版本
// 基本思路是将中间位置的那个数换到left然后拍完序后再把left换回正确的位置
void qsort(int v[], int left, int right) {
    int i, last;
    void oswap(int v[], int i, int j);

    if (left >= right)  //如果左边都大于右边了，这意味着比价已经结束了
        return;
    oswap(v, left, (left + right) / 2);
    last = left;
    for (i = left + 1; i <= right; i++)
        if (v[i] < v[left])
            oswap(v, ++last, i);
    oswap(v, left, last);
    qsort(v, left, last - 1);
    qsort(v, last + 1, right);
}

void merge(int r[], int s[], int left, int mid, int right) {
    int i, j, k;
    i = left;
    j = mid + 1;
    k = left;
    while((i <= mid) && (j <= right)) {
        if(r[i] <= r[j]) {
            s[k++] = r[i++];
        } else {
            s[k++] = r[j++];
        }
    }
    while(i <= mid) {
        s[k++] = r[i++];
    }
    while(j <= right) {
        s[k++] = r[j++];
    }
}

void merge_sort(int r[], int s[], int left, int right) {
    int mid;
    // int *t = (int *)malloc(sizeof(int) * (right - left + 1));
    int t[20];
    if(left == right) {
        s[left] = r[right];
    } else {
        mid = (left + right) / 2;
        merge_sort(r, t, left, mid);
        merge_sort(r, t, mid + 1, right);
        merge(t, s, left, mid, right);
    }   
}

int main(int argc, char *argv[]) {
    if(argc == 1) {
        printf("no number is inputed");
        return -1;
    }

    int *arr = (int *)malloc(sizeof(int) *  (argc - 1));
    int *sorted_arr = (int *)malloc(sizeof(int) * (argc - 1));
    for(int i = 1; i < argc; i++) {
        arr[i - 1] = stoi(argv[i]);
    }
    memcpy(sorted_arr, arr, sizeof(int) * (argc - 1));
    printf("\nsorted array:\n");
    // bubble_sort(sorted_arr, argc - 1);
    // quick_sort(sorted_arr, 0, argc - 2);
    merge_sort(arr, sorted_arr, 0, argc -2);
    for(int i = 0; i < argc - 1; i++) {
        printf("%d ", sorted_arr[i]);
    }
    printf("\n");

    free(arr);
    free(sorted_arr);
}
