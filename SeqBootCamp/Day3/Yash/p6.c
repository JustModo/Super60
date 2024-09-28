// dec to bin
#include <stdio.h>

void main()
{
    int num = 58, i = 0;
    int bin[32];
    if (num == 0)
    {
        printf("0");
        return;
    }
    while (num > 0)
    {
        bin[i] = num % 2;
        num /= 2;
        i++;
    }
    for (int j = i - 1; j >= 0; j--)
    {

        printf("%d", bin[j]);
    }
}