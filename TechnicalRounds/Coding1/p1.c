#include <stdio.h>

void main()
{
    int n = 100;
    int sum = 0;

    int series = 1;
    int incrementer = 1;
    int a[100];

    for (int i = 0; i < n; i++)
    {
        if (series % 2 == 0)
        {
            a[i] = -1 * series;
            sum += -1 * series;
        }
        else
        {
            a[i] = series;
            sum += series;
        }

        series += incrementer;
        incrementer += 2;
    }

    // for (int i = 0; i < n; i++)
    // {
    //     printf("%d ", a[i]);
    // }
    // printf("\nSum = %d\n", sum);

    int b[100];
    int count = 0;
    int sum1 = 0;

    for (int i = 0; i < n; i++)
    {
        int flag = 0;
        int temp = a[i];
        while (temp != 0)
        {
            int rem = temp % 10;
            if (rem == 0)
                flag = 1;
            temp /= 10;
        }
        if (flag == 1)
            b[count++] = a[i];
    }

    // for (int i = 0; i < count; i++)
    // {
    //     sum1 += b[i];
    //     printf("%d ", b[i]);
    // }

    // printf("\nSum is %d\n", sum1);

    int c[100];
    count = 0;
    int sum2 = 0;

    for (int i = 0; i < n; i++)
    {
        int flag = 0;
        int temp;
        if (a[i] > 0)
        {
            temp = a[i];
        }
        else
        {
            temp = a[i] * -1;
        }

        int prev = 100000;
        while (temp != 0)
        {
            int rem = temp % 10;
            if (rem >= prev)
            {
                flag = 1;
                break;
            }
            prev = rem;
            temp /= 10;
        }
        if (flag != 1)
        {
            sum2 += a[i];
            c[count++] = a[i];
        }
    }

    for (int i = 0; i < count; i++)
    {
        printf("%d ", c[i]);
    }
    printf("\nSum is %d", sum2);
}