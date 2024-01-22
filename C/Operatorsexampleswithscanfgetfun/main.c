#include <stdio.h>

int main()
{
    int A,B;

    addtion(getA(),getB());
    subtraction(getA(),getB());
    multiplication(getA(),getB());
    modules(getA(),getB());
    divition(getA(),getB());
    increment(getA());
    decrement(getA());
    ifclauses(getA());
    compare(getA(),getB());
    whileclause(getA());
    dowhileprgrm(getA());
    switchesprgrm(getB());
    assigning(getA(),getB());
    forclauses(getA());
    nestedprgrm(getA(),getB());

return 0;
}
int getA()
{
    int A;
    printf("Enter the A value : \n\n\t");
    scanf("%d",&A);
    return A;

}

int getB()
{
    int B;
    printf("Enter the B value : \n\n\t");
    scanf("%d",&B);
    return B;

}

int addtion(int A, int B)
 {
 int C;
  printf("*------ADDTION------*\n\n\t");
  C=A+B;
  printf("Addition value is : %d\n\n\t",C);
  return 0;
}

int subtraction(int A, int B)
 {
 int C;
  printf("*------SUBTRACTION------*\n\n");
  C=A-B;
  printf("Subtraction value is : %d\n\n\t",C);
  return 0;
}
int multiplication(int A, int B)
 {

 int C;
  printf("*------MULTIPLICATION------*\n\n");
  C=A*B;
  printf(" Multiplication value is : %d\n\n\t",C);
  return 0;
}
int divition(int A, int B)
 {
 float C;
  printf("*------DIVITION------*\n\n");
  C=(float)A/B;
  printf("Divition value is : %f\n\n\t",C);
  return 0;
}
int modules(int A, int B)
 {
 int D;
  printf("*------MODULES------*\n\n");
  D=A%B;
  printf("Modules value is : %d\n\n\t",D);
  return 0;
}

int increment(int A)
 {
 printf("*------INCREMENT------*\n\n");
 ++A;
printf("Increment value is : %d\n\n\t",A);

  return 0;
}
int decrement(int A)
 {

 printf("*------DECREMENT------*\n\n");
 --A;
printf("Decrement value is : %d\n\n\t",A);
  return 0;
}
int assigning(int A, int B)
 {
  printf("*------ASSIGN------*\n\n");
  A+=B;//A=A+B
  printf("The value of A is : %d\n",A);
  B-=A;//B=B-A
  printf("The value of B is : %d\n",B);
  B*=A;//B=B*A
  printf("The value of B is : %d\n",B);
  B/=A;//B=B/A
  printf("The value of A is : %d\n",B);

  return 0;
}

int compare(int A, int B)
 {
  printf("*------COMPARISION------*\n\n\t");
  printf("COMPARISION value of A>B is : %d\n\n\t",A>B);
  printf("COMPARISION value of A<B is : %d\n\n\t",A<B);
  printf("COMPARISION value of A>=B is : %d\n\n\t",A>=B);
  printf("COMPARISION value of A<=B is : %d\n\n\t",A<=B);
  printf("COMPARISION value of A==B is : %d\n\n\t",A==B);
  printf("COMPARISION value of A!=B is : %d\n\n\t",A!=B);

  return 0;
}

int ifclauses(int A)
 {printf("*------IF CONDITION------*\n\n\t");
 if(A<15)
 {
printf("The value of A is :%d\n",A);

 }
  return 0;
}

int whileclause(int A)
 {
int I=20;
printf("*------WHILE CONDITION------*\n\n\t");
 while(A<=I)
 {
printf("THE VALUE IS:%d\n\n\n",A);
A++;

 }
  return 0;
}

int dowhileprgrm(int A)
{
int I=15;
printf("*------DO WHILE CONDITION------*\n\n\t");
do{
printf("THE VALUE IS:%d\n\n\n",A);
A++;
 }while(A<I && A!=2);
  return 0;
}

int nestedprgrm(int A, int B)
 {
 int c=15;
 int d=0;
 int e=0;
 int F=12;
 printf("*------NESTED IFELSE CONDITION------*\n\n\t");

 if(A<10 && A!=0)
 {
     if(B!=20){
      printf("Value  A is :%d\n\n",B);
     }
     else{
        printf("Value is null\n\n");
     }}
else if(c==15 || d==12)
     {if(e!=0){
         printf("The value of e is :%d\n\n",e);
     }
     else
     {
         printf("The value of c is :%d\n\n",c);
 }}
 else{
    printf("The value of F is :%d\n\n",F);
 }
  return 0;
 }

  int switchesprgrm(int B)
{
 printf("*------SWITCH CONDITION------*\n\n\t");
    printf(" The Value is : %d\n\n\t",B);
    switch(B)
    {
    case 1:
        printf("The name is: sanz\n\n\t");
        break;
        case 2:
        printf("The name is: sang\n\n\t");
        break;
        case 3:
        printf("The name is: sam\n\n\t");
        break;
        case 4:
        printf("The name is: san\n\n\t");
        break;
        case 5:
        printf("The name is: sangari\n\n\t");
        break;

    }
    return 0;
}


int forclauses(int A)
 {int a;
     printf("*------ FOR CONDITION------*\n\n\t");
 for(a=A;a<50;a=a+2)
 {
printf("The value of A is :%d\n",a);

 }
  return 0;
}
