#include <iostream>

using namespace std;

class constructor
{

public:
   constructor()
    {
        int a;
         cin >> a;
         cout << "Print the value " << a << endl;
    }

    constructor(int a , int b)
    {
         cout << "added value is : " <<(a+b) << endl;
    }
    constructor(int x , int y , int z)
    {

         cout << "Multiple value is : " << (x*y*z) << endl;
    }
};

int main()
{
 constructor cns;
 int a,b;
 constructor cns1(2 , 10);
 int x,y,z;
 constructor cns2(2,3,4);
    return 0;
}
