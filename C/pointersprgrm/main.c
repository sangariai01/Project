#include <stdio.h>
#include <stdlib.h>
/*
int main()
{
    int a = 5; int b;
    printf("%d \n",a);
    printf("print the address : %d  %d\n" , &a ,&b);
    printf("print the size : %d\n" , sizeof(a));

    int *p=&a;
    printf("value of p                          : %d \t\n", p);
    printf("address of p                        : %d \t\n", &p);
    printf("value stored in the address of p    : %d \t\n", *p);
    printf("-----------\n");*/


  /*  char s[10] ="san";
    printf("%s \n",s);

 char *p=&s;
    printf("value of p                          : %s \t\n", p);
    printf("address of p                        : %s \t\n", &p);
    printf("value stored in the address of p    : %s \t\n", *p);
    printf("-----------\n");
char **q=&p;
    printf("value of p                          : %s \t\n", q);
    printf("address of p                        : %s \t\n", &q);
    printf("value stored in the address of p    : %s \t\n", *q);
    printf("-----------\n");


    return 0;
}   */

int main()
{
    int a=10, b=20;
    printf("value of a      : %d \t\n", a);
    printf("Address of a    : %d \n", &a);
    printf("-----------\n");
    printf("value of b      : %d \t\n", b);
    printf("address of B    : %d \n", &b);
    printf("-----------\n");

    int *p=&a;
    printf("value of p                          : %d \t\n", p);
    printf("address of p                        : %d \t\n", &p);
    printf("value stored in the address of p    : %d \t\n", *p);
    printf("-----------\n");

    int **q=&p;
    printf("value of q                                              : %d \t\n", q);
    printf("address of q                                            : %d \t\n", &q);
    printf("value stored in the address of q to the address of p    : %d \t\n", **q);

    int ***r=&q;
    printf("value of r                                                                  : %d \t\n", r);
    printf("address of r                                                                : %d \t\n", &r);
    printf("value stored in the address of r to the address of q in the address of p    : %d \t\n", ***r);

    void *s=&a;
    printf("value of s                                                                  : %d \t\n", s);
    printf("address of s                                                                : %d \t\n", &s);
    printf("value stored  in the address of s in the address of r to the address of q in the address of p    : %d \t\n", *(int*)s);

    return 0;
}


