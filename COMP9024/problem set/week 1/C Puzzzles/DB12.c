#include <stdio.h>
#include <stdlib.h>

/* Puzzle D11 -- add up all the integers in an array of integers */

long addArray(int size, int arr[])
{
    int j;
    long sum = 0;

    for ( j = 0; j < size; j++)
    {
        if (arr[j]%2!=0)
        {
            sum += arr[j];
        }
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
    int x[SIZE] = { 0, 2, 1, -3, -5, 2, 4, 6, 9, 60 };

    printArray(SIZE, x);
    printf("\n");
    printf("sum = %ld\n", addArray(SIZE, x));

    return 0;
}
