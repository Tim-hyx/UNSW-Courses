#include <stdio.h>

void center(char ch, int count, int length)
{
    int blanks, i;
    blanks = length - count;
    for (i = 0; i < blanks / 2; i++)
    {
        printf(" ");
    }
    for (i = 0; i < count; i++)
    {
        printf("%c", ch);
    }
}

void triangle(char ch, int rows)
{
    int j;
    for ( j = 1; j <= rows; j++)
    {
        center(ch, 2 * j - 1, 2 * rows - 1);
        printf("\n");
    }
}

int main()
{
    triangle('*', 5);
    return 0;
}
