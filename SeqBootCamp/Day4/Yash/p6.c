#include <stdio.h>

// 1
// 2 4
// 7 11 16
// 22 29 37 46

void main()
{
    int n = 1;
    int increment = 1;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("%d ", n);
            n += increment;
            increment++;
        }
        printf("\n");
    }
}