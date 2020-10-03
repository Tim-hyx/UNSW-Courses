// Integer Stack ADO tester ... COMP9024 20T2
#include "IntStack.h"
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i, n;
    char str[BUFSIZ];

    StackInit();

    printf("Enter a positive number: ");
    scanf("%s", str);
    if ((n = atoi(str)) > 0)
    { // convert to int and test if positive
        for (i = 0; i < n; i++)
        {
            printf("Enter a number: ");
            scanf("%s", str);
            StackPush(atoi(str));
        }
    }

    /* NEEDS TO BE COMPLETED */
    int popnum;
    while (!StackIsEmpty())
    {
        popnum = StackPop();
        printf("%d\n", popnum);
    }
    
    return 0;
}