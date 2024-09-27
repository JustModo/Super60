// #include <stdio.h>

// void main()
// {
//     int i = 1, c = 0, d = 0;
//     while (1)
//     {
//         d++;
//         int n = i * 7;
//         if (n % 2 == 1 && n % 3 == 1 && n % 4 == 1 && n % 5 == 1 && n % 6 == 1)
//         {
//             c++;
//             if (c != 3)
//                 printf("%d\n", n);
//         }
//         if (c == 4)
//             break;
//         i++;
//     }
//     printf("Iterations: %d", d);
// }

#include <stdio.h>

void main()
{
    int i = 43, c = 1, d = 0;
    while (c <= 4)
    {
        int n = i * 7;

        if ()
            printf("%d\n", n);
        c++;

        i += 60;
        d++;
    }
    printf("Iteration- %d", d);
}