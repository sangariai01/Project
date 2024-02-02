#include <iostream>

using namespace std;

class functionoverloading
{

public:
   ifelseprgrm()
    {
        int a;
        cout << "Enter the a value " << endl;
        cin >> a;
        if(a<10)
        {
        cout << "The given number is : " << a << endl;
        }
    }
    ifelseprgrm(int a1)
    {
        if(a1<=10)
        { ++a1;
            cout << "The number is : " << a1 << endl;
        }
    }
};
int main()
{
    functionoverloading fol , fol1;
    fol.ifelseprgrm();
    int a1;
    cout << "Enter the a value " << endl;
    cin >> a1;
    fol1.ifelseprgrm(a1);

    return 0;
}

