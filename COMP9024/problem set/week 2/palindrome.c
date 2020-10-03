#include <stdbool.h>
#include <stdio.h>
#include <string.h>
bool isPalindrome(char A[], int len)
{
    len = strlen(A);
    int i;
    for (i = 0; i < len / 2; i++)
    {
        if (A[i] != A[len - i - 1])
        {
            return false;
        }
    }
    if (i >= len / 2)
    {
        return true;
    }
    return false;
}
int main()
{
    char word[10];
    int length;
    printf("Enter a word: ");
    scanf("%s", word);
    length = strlen(word);
    if (isPalindrome(word, length))
    {
        printf("yes\n");
    }
    else
    {
        printf("no\n");
    }

    return 0;
}
