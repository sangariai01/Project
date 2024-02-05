#include <iostream>

using namespace std;

int main()
{
    string project;
    cout << " Enter the string value " << endl;
    cin >> project ;
    cout << "The address of the given string is : " << &project << endl;
    cout << "--------------------" << endl;


    string *a = &project;
<<<<<<< HEAD
    cout << "value of a                          : %p \t\n" << a;
    cout << "address of a                        : %p \t\n", *a);
    cout << "value stored in the address of a    : %s \t\n", *a);
    cout << "-----------\n");
=======
    cout << "value of a                          : %p " << a << endl;
    cout << "address of a                        : %p " << &a << endl;
    cout << "value stored in the address of a    : %s " << *a << endl;
    cout << "-----------\n";
>>>>>>> 993dce076c83f38aa89f67dd042ec52e682432eb

    float f ;
    cout << "Enter the value " << endl;
    cin >> f ;
    cout << "The given value is :" << f << endl;
    cout << " The address is : " << &f << endl;
    cout << "--------------------" << endl;

    float *b = &f;
<<<<<<< HEAD
    printf("value of b                          : %p \t\n", b);
    printf("address of b                        : %p \t\n", *b);
    printf("value stored in the address of b    : %f \t\n", *b);
    printf("-----------\n");

    float **c = &b;
    printf("value of c                          : %p \t\n", c);
    printf("address of c                        : %p \t\n", *c);
    printf("value stored in the address of c    : %f \t\n", **c);
    printf("-----------\n");
=======
    cout << "value of b                          : %p " << b << endl;
    cout << "address of b                        : %p " << &b << endl;
    cout << "value stored in the address of b    : %f " << *b << endl;
    cout << "--------------------" << endl;

    float **c = &b;
    cout << "value of c                          : %p "<<  c << endl;
    cout << "address of c                        : %p " << &c << endl;
    cout << "value stored in the address of c    : %f " << **c << endl;
    cout << "-----------\n";
>>>>>>> 993dce076c83f38aa89f67dd042ec52e682432eb


    return 0;
}
