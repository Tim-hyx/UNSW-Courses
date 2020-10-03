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

void pyramid(int blocks)
{
	int b;
	for ( b = 1; b < blocks; b++)
	{
		starBlock(b, 2 * b - 1);
	}
}

int main()
{
	pyramid(7);
	return 0;
}
