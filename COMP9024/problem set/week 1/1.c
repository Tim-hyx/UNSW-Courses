#include <stdio.h>
int main()
{
	int start = 10000, finish = 99999;
	int a, b, c, d, e, i;
	for ( i = start; i <= finish; i++)
	{
		a = i % 10;
		b = i / 10 % 10;
		c = i / 100 % 10;
		d = i / 1000 % 10;
		e = i / 10000;
		if (4*i==10000*a+1000*b+100*c+10*d+e)
		{
			printf("%d", i);
		}
	}
	return 0;
}
