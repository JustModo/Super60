// 1 2 4 6 7 10 10 14
#include <stdio.h>

void main()
{
    int series1 = 1;
    int series2 = 2;
    printf("1 2 ");
    for (int i = 0; series1 <= 100; i++)
    {
        printf("%d ", series1 += 3);
        printf("%d ", series2 += 4);
    }
}