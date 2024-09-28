// 1 5	14	28	47	71	100	134	173	217	266	320	379	443	512	586
// 4 9 14 19 24 29

#include <stdio.h>

void main()
{
    int series = 1;
    int incrementer = 4;
    int num = 1000;
    for (int i = 0; series < num; i++)
    {
        printf("%d ", series);
        series += incrementer;
        incrementer += 5;
    }
}