#include<stdio.h>

int main()
{
    int a;
    printf(" The given year is : \n");
    scanf("%d",&a);
    if(a%4 ==0)
    {
        printf(" The given year is leap year /n/t");
    }
    else
    {
        printf("The given year is not leapyear /n/t");
    }
    return 0;
}