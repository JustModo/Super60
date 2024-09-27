#include <stdio.h>

// 1, 5, 13, 29, 49, 77, ... N

void main()
{
    int series = 1;
    int n = 500;
    int temp;

    for (int i = 1; series <= n; i++)
    {
        printf("%d ", series);
        temp = 4 * i;
        if (temp % 12 == 0)
            continue;
        series += temp;
    }
}