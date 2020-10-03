#include <stdio.h>
#include <stdlib.h>

/* Puzzle L11 -- print the ODD integers from 1 to n, five per line.
|
|  End the last line with a single "\n" regardless of how many
|  integers are on it.
*/
int main()
{
    int j;
    const int n = 53;  /* change this to whatever you want */
    int count = 0;
    for (j = 1; j <= n; j += 2)
    {
        printf("%3d", j);
        count++;
        if (count % 5 == 0)
        {
            printf("\n");
        }
    }

    /* Last line logic */
    if (count % 5 != 0)
    {
        printf("\n");
    }
    /* system("pause"); */  /* un-comment if needed */
    return 0;
}
