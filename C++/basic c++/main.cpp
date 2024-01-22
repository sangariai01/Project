#include <iostream>

using namespace std;

int main()
{
    int a , b,op,Total;
    cout << "Enter the value\n";
    cin >> a >> b;
    cout << "Enter the operator\n";
    cin >> op;
    switch(op)
    {
    case 1:
        Total = a+b;
        cout << " The added value is : \n" << Total ;
        break;
    case 2 :
        Total = a-b;
        cout << " The Subtract value is : \n" << Total ;
        break;
    case 3:
        Total = a*b;
        cout << " The multiply value is : \n" << Total ;
        break;
    case 4:
        Total = a/b;
        cout << " The didvided value is : \n" << Total ;
        break;
    case 5:
        Total = a%b;
        cout << " The modulas value is : \n" << Total ;
        break;
    case 6:
        ++a;
        cout << " The Preincrement value is : \n" << a ;
        break;
    case 7:
        a++;
        cout << " The Postincrement value is : \n" << a ;
        break;
    case 8:
        --b;
        cout << " The Predecrement value is : \n" << b ;
        break;
    case 9:
        b--;
        cout << " The Postdecrement value is : \n" << b ;
        break;
    case 10:
        a+=b;
        cout << " The Assigned value is : \n" << a ;
        b-=a;
        cout << " The Assigned value is : \n" << b ;
        a*=b;
        cout << " The Assigned value is : \n" << a ;
        b/=a;
        cout << " The Assigned value is : \n" << b ;
        break;
    }
    return 0;
}
