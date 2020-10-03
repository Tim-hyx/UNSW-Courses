#include <stdio.h>
#include <stdlib.h>

/* Puzzle L14 -- on each line k print all the integers in the
|  range 100*k to (100*k+99) that are multiples of 23.
|
|  Not a very good solution: does 23 times more work than
|  is needed.
*/
int main()
{
    int k;     /* line number */
    int base;  /* The base number for line k is 100*k */
    int j;     /* values 0..99 to add to the base number for line k*/

    /* for each line number k */
    for (k=0;k<12;k++)
    {
        base = 100 * k;

        /* for the 100 integers considered for line k */
        for (j=0;j<=99;j++)
            /* decide if the integer should be printed */
            if ((base+j)%23==0)
                printf("%7d", (base + j));

        printf("\n");
    }


    return 0;
}
