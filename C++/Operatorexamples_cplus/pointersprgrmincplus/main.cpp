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
    cout << "value of a                          : %p " << a << endl;
    cout << "address of a                        : %p " << &a << endl;
    cout << "value stored in the address of a    : %s " << *a << endl;
    cout << "-----------\n";

    float f ;
    cout << "Enter the value " << endl;
    cin >> f ;
    cout << "The given value is :" << f << endl;
    cout << " The address is : " << &f << endl;
    cout << "--------------------" << endl;

    float *b = &f;
    cout << "value of b                          : %p " << b << endl;
    cout << "address of b                        : %p " << &b << endl;
    cout << "value stored in the address of b    : %f " << *b << endl;
    cout << "--------------------" << endl;

    float **c = &b;
    cout << "value of c                          : %p "<<  c << endl;
    cout << "address of c                        : %p " << &c << endl;
    cout << "value stored in the address of c    : %f " << **c << endl;
    cout << "-----------\n";


    return 0;
}
