// 6	-8	10	-14	20	-30	46	-72	114	-182	292	-470	758	-1224	1978	-3198
// 2 4 8

#include <stdio.h>

void main()
{
    int a = 6;
    int b = 8;
    int c = 10;
    int n = 500;
    int series = 0;
    int i = 0;
    printf("%d -%d ", a, b);
    for (int i = 0; c < n; i++)
    {

        series = (b - a) + (c - b);
        i % 2 == 0 ? printf("%d ", c) : printf("-%d ", c);
        a = b;
        b = c;
        c = b + series;
    }
}