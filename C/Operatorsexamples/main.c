#include <stdio.h>


struct samplestruct
{
    int A;
    int B;
};

int main()
{
    struct samplestruct mystruct;
    mystruct.A=10;
    mystruct.B=5;
    int F=10;
    printf("The value of A is : %d\n",mystruct.A);
    printf("The value of B is : %d\n",mystruct.B);
    addtion(mystruct.A,mystruct.B);
    subtraction(mystruct.A,mystruct.B);
    multiplication(mystruct.A,mystruct.B);
    divition(mystruct.A,mystruct.B);
    modules(mystruct.A,mystruct.B);
    increment(mystruct.A);
    decrement(mystruct.A);
    assigning(mystruct.A,mystruct.B);
    compare(mystruct.A,mystruct.B);
    ifclauses(mystruct.A);
    whileclause(mystruct.A);
    dowhileprgrm(F);
    nestedprgrm(mystruct.A,mystruct.B,F);
    switchesprgrm(mystruct.B);
    forclauses(mystruct.A);
   //structureprgrm();
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

int dowhileprgrm(int F)
{
int I=15;
printf("*------DO WHILE CONDITION------*\n\n\t");
do{
printf("THE VALUE IS:%d\n\n\n",F);
F++;
 }while(F<I && F!=2);
  return 0;
}

int nestedprgrm(int A, int B, int F)
 {
 int c=15;
 int d=0;
 int e=0;
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










