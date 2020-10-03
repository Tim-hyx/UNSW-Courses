#include <stdio.h>
#include <stdlib.h>

/* Puzzle D11 -- add up all the integers in an array of integers */

long addArray(int size, int arr[])
{
    int i;
    int sum = 0;
    for ( i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    return sum;
}

void printArray(int size, int arr[])
{
    const int N = 10;
    int j;

    for (j = 0; j < size; j++)
    {
        if (j % N == N - 1)
            printf("%4d\n", arr[j]);
        else
            printf("%4d ", arr[j]);
    }
}

#define SIZE 10
int main()
{
    int x[SIZE] = { -1, 1, -2, 2, -3, 3, -4, 4, -5, 5 };

    printArray(SIZE, x);
    printf("\n");
    printf("sum = %ld\n", addArray(SIZE, x));

    return 0;
}
