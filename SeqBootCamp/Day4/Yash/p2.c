// 1	3	5	9	15	25	41	67	109	177	287	465	753	1219	1973	3193

#include <stdio.h>

void main()
{
    int a = 1;
    int b = 3;
    int n = 200;
    int series;
    printf("%d %d ", a, b);

    do
    {
        series = a + b + 1;
        printf("%d ", series);
        a = b;
        b = series;
    } while (n > series);
}