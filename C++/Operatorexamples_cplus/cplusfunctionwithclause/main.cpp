#include <iostream>

using namespace std;

class OperatorFunctions
{
public:
    void addition()
    {
        int a , b;
            cin >> a >> b;
            cout << "Added value is :" <<(a+b) << endl;
    }
    void subtraction ()
    {
        int c , d;
            cin >> c >> d;
            cout << "Subtrated value is :" << (c-d) << endl;
    }

     void multiplication ()
    {
        int x , y;
            cin >> x >> y;
            cout << "Multiplication value is :" << (x*y) << endl;
    }

    void division();
    void modulas();
};

void OperatorFunctions :: division()
{
    int x , y;
            cin >> x >> y;
            cout << "Division value is :" << (x/y) << endl;
}

void OperatorFunctions :: modulas()
{
    int x , y;
            cin >> x >> y;
            cout << "Modulas value is :" << (x%y) << endl;
}

int main()
{
    OperatorFunctions OF;
    OF . addition();
    OF . subtraction();
    OF . multiplication ();
    OF . division ();
    OF . modulas();

    return 0;
}
