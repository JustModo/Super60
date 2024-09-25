#include <stdio.h>

void main()
{
    int n, sum = 0;
    scanf("%d", &n);
    for (int i = 1;; i++)
    {
        int num = i * 3;
        if (num > n)
            break;
        if (num % 15 == 0)
            continue;
        printf("%d\n", num);
    }
}
