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

void starBlock(int rows, int cols,int linesize)
{
    int j;
    for (j = 0; j < rows; j++)
    {
        center('*', cols, linesize);
        printf("\n");
    }
}

void pyramid(int blocks)
{
    int b;
    int linesize = 2 * blocks - 1;
    for (b = 1; b < blocks; b++)
    {
        starBlock(b, 2 * b - 1,linesize);
    }
}

int main()
{
    pyramid(7);
    return 0;
}
