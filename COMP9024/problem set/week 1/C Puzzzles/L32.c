#include <stdio.h>

void center(char ch, int count, int length)
{
    int blanks,i;
    blanks = length - count;
    for ( i = 0; i < blanks/2; i++)
    {
        printf(" ");
    }
    for ( i = 0; i < count; i++)
    {
        printf("%c", ch);
    }
}

int main()
{
    center('*', 5, 13);
    return 0;
}
