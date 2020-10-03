#include "IntStack.h"
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    StackInit();
    printf("Enter a number: ");
    scanf("%d", &n);
    while (n > 0)
    {
        StackPush(n % 2);
        n = n / 2;
    }
    int popnum;
    while (!StackIsEmpty())
    {
        popnum = StackPop();
        printf("%d", popnum);
    }
    return 0;
}
