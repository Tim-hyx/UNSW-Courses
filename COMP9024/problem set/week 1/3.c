#include <stdio.h>
#define MAX 10
void num(int n)
{
    if (n > 0)
    {
        printf("%d\n", n);
        while (n != 1)
        {
            if (n % 2 == 0)
            {
                n = n / 2;
            }
            else
            {
                n = 3 * n + 1;
            }
            printf("%d\n", n);
        }
    }
}
int main()
{

    int i, j;
    int Fib[MAX];
    Fib[0] = 1;
    Fib[1] = 1;
    for (j = 2; j < MAX; j++)
    {
        Fib[j] = Fib[j - 1] + Fib[j - 2];
    }

    for (i = 0; i < MAX; i++)
    {
        printf("Fib[%d]=%d\n", i + 1, Fib[i]);
        num(Fib[i]);
    }

    return 0;
}
