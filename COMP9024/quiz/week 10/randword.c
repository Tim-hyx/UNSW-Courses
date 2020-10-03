#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //  ./randword 6 2
    //  argv[0]=./randword    argv[1]=6    argv[2]=2
    srand(atoi(argv[2])); //converts str to int
    for (int i = 0; i < atoi(argv[1]); i++)
    {
        int randword = rand() % 26;
        printf("%c", 'a' + randword);
    }
    return 0;
}