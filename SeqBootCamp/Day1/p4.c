#include <stdio.h>

void main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i < n; i += 4)
    {
        if ((i - 1) % 8 == 0)
            printf("%d ", i);
        else
            printf("-%d ", i);
    }
}
