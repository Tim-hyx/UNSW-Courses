#include <stdio.h>
#include <stdlib.h>

/* Puzzle L13 -- print integers from 1 to n that are not multiples of 3 or 5
|  Print 10 integers per line.
|  End the last line with "\n", even if the line has fewer than
|  ten numbers on it.
|
*/
int main()
{
    int j;
    int count = 0;
    int n = 100;

    /* Generate Integers */
    for (j=1;j<=100;j++)
    {
        /* Test if the integer should be printed */
        if (j%3!=0 && j%5!=0)
        {
            printf("%3d", j);
            count++;
            if (count%10==0)
            {
                printf("\n");
            }
        }
    }

    /* Last Line Logic */
    if (count%10!=0) printf("\n");

    return 0;
}
