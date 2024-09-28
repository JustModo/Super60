// 1	-4	15	-34	61	-96	139	-190	249	-316	391	-474	565	-664	771	-886
//  3 11 19

#include <stdio.h>

void main()
{
    int series = 1;
    int incrementer = 3;
    int num = 500;

    for (int i = 0; series < num; i++)
    {
        i % 2 == 0 ? printf("%d ", series) : printf("-%d ", series);
        series += incrementer;
        incrementer += 8;
    }
}