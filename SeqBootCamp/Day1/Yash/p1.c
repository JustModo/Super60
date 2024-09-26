#include <stdio.h>

// 1,2,4,7,11,16

void main()
{
    int n, num = 1, i, sum = 0;
    scanf("%d", &n);
    for (i = 0; num < n - i; i++)
    {
        num += i;
        sum += num;
        printf("%d ", num);
    }
    printf("\nNumber of terms %d\n", i);
    printf("The sum is %d\n", sum);
}