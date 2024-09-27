#include <stdio.h>

void main()
{
    double n;
    int a;
    scanf("%lf", &n);
    a = (int)n;
    printf("%d\n", a);
    printf("%lf\n", n - a);
}