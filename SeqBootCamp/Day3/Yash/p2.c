#include <stdio.h>
#include <string.h>

void main()
{
    char num[100];
    scanf("%s", num);
    // strrev(num);
    for (int i = 0; i < strlen(num); i++)
    {
        switch (num[i])
        {
        case '0':
            printf("Zero ");
            break;
        case '1':
            printf("One ");
            break;
        case '2':
            printf("Two ");
            break;
        case '3':
            printf("Three ");
            break;
        case '4':
            printf("Four ");
            break;
        case '5':
            printf("Five ");
            break;
        case '6':
            printf("Six ");
            break;
        case '7':
            printf("Seven ");
            break;
        case '8':
            printf("Eight ");
            break;
        case '9':
            printf("Nine ");
            break;
        default:
            printf("%c ", num[i]);
            break;
        }
    }
}