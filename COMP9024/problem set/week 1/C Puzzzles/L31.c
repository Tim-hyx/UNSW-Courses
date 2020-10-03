#include <stdio.h>

void starLine(int n)
{
	int i;
	for ( i = 0; i < n; i++)
	{
		printf("*");
	}
}

int main()
{
    starLine(8);
    return 0;
}
