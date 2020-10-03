#include <stdio.h>
#include <string.h>
int main()
{
    char A[100];
    int i, len;
    printf("Enter a word: ");
    scanf("%s", A);
    len = strlen(A);
    for (i = 0; i < len / 2; i++)
    {
        if (A[i] != A[len - i - 1])
        {
            printf("no\n");
            break;
        }
    }
    if (i >= len / 2)
        printf("yes\n");

    return 0;
}
