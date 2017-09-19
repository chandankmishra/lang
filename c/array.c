#include <stdio.h>

#define MAX 5

void insert (int *, int pos, int num);
void del (int *, int pos);
void reverse (int *);
void display (int *);
void search (int *, int num);

void
display (int *arr)
{
    int i = 0;

    for (i = 0; i < MAX; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n\n");
}

void
insert (int *arr, int pos, int num)
{
    int i = 0;

    for (i = MAX-1; i >= pos; i--) {
        arr[i] = arr[i-1];
    }
    arr[i] = num;
}

void
del (int *arr, int pos)
{
    int i = 0;

    for (i = pos; i < MAX; i++) {
        arr[i-1] = arr[i];
    }
    arr[i-1] = 0;
}

void
reverse (int *arr)
{
    int i = 0, tmp = 0;

    for (i = 0; i < MAX/2; i++) {
        tmp = arr[i];
        arr[i] = arr[MAX-1-i];
        arr[MAX-1-i] = tmp;
    } 
}

void
selection_sort (int *arr)
{
    int i, j = 0;
    int tmp = 0;

    for (i =0; i < MAX; i++) {
        for (j = i+1; j < MAX; j++) {
            if (arr[i] > arr[j]) {
                tmp = arr[i]; 
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
}

void
bubble_sort2 (int *arr)
{
    int i, j, k, tmp = 0;

    for (i =0, k = MAX-1; i < MAX-1; i++, k--) {
        for (j = 0; j < k; j++) {
            if (arr[j] > arr[j+1]) {
                tmp = arr[j]; 
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }
}

void
bubble_sort1 (int *arr)
{
    int i, j, tmp = 0;

    for (i =0; i < (MAX-1); i++) {
        for (j = 0; j < MAX-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                tmp = arr[j]; 
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }
}
void
search (int *arr, int num)
{
    int i = 0;

    for (i = 0; i < MAX; i++) {
        if (arr[i] == num) {
            printf("Number %d found at location %d\n", num, i+1);
            break;
        }
    }
    if (i == MAX) {
        printf("Number %d not found\n", num);
    }
}

int main (void)
{
    int arr[MAX] = {0};

    printf("Elements of Array: \n");
    display(arr);
    insert(arr, 1, 11); 
    insert(arr, 2, 12); 
    insert(arr, 3, 13); 
    insert(arr, 4, 14); 
    insert(arr, 5, 15); 
    printf("Elements of Array: \n");
    display(arr);

    del(arr, 5);
    del(arr, 2);
    printf("After deletion : \n");
    display(arr);

    insert(arr, 2, 222); 
    insert(arr, 5, 555); 
    printf("After insertion: \n");
    display(arr);

    reverse(arr);
    printf("After reversing : \n");
    display(arr);

    search(arr, 222);
    search(arr, 666);

    //selection_sort(arr);
    //bubble_sort1(arr);
    bubble_sort2(arr);
    printf("After sorting : \n");
    display(arr);

}
