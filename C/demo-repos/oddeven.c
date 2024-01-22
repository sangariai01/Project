#include <stdio.h>
 int oddevenprgrm()
 {
    int a;
    printf("The given number is:");
    scanf("%d",&a);
    if(a%2==0)
    {
        printf("The number is even\n");
    }
    else
    {
      printf("The number is odd\n");
    }
    return 0;
 }
