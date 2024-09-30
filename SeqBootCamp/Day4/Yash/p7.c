#include <stdio.h>

// 1
// -1	2
// -3	5	-8
// 13	-21	34	-55
// :
// :
// N Rows 

void main()
{
    int a = 0;
    int b = 1;
    int c;
    int count = 0;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < i; j++)
        {
            c = a + b;
            count % 2 == 0
                ? printf("%d ", b)
                : printf("-%d ", b);
            a = b;
            b = c;
            count++;
        }
        printf("\n");
    }
}