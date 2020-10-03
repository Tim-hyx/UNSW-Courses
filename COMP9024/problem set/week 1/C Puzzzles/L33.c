#include <stdio.h>

void starLine(int n)
{
	int i;
	for ( i = 0; i < n; i++)
	{
		printf("*");
	}
	printf("\n");
}

void starBlock(int rows, int cols)
{
	int j;
	for ( j = 0; j < rows; j++)
	{
		starLine(cols);
	}
}

int main()
{
    starBlock(5, 7);
    return 0;
}
