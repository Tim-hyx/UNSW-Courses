#include <stdio.h>
#include <stdlib.h>

/* Puzzle L12 -- print the ODD integers from start down to finish
|  seven per line.
|  End the last line with "\n", even if the line has fewer than
|  seven numbers on it.
|
*/
int main()
{
    int j;
    int start = 147, finish = 53;
    int count = 0;

    for (j = start; j >= finish; j -= 2)
    {
        printf("%4d", j);
        count++;
        if (count % 7 == 0)
        {
            printf("\n");
        }
    }

    /* Last Line Logic */
    if (count % 7 != 0) printf("\n");


    return 0;
}
