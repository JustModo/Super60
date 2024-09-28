// 6	23	90	267	638	1311	2418	4115	6582	10023	14666	20763	28590	38447	50658
// Excel sheet it, 4 level deep subtraction

#include <stdio.h>

void main()
{
    int n = 6;
    int i = 17;
    int j = 50;
    int k = 60;
    int l = 24;
    int num = 5000;

    while (n < num)
    {
        printf("%d ", n);
        n += i;
        i += j;
        j += k;
        k += l;
    }
}