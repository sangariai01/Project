#include<iostream>
using namespace std;
class myfirstclass
{
public :
    int a=5;

    void multiply()
    {
        int x,y;
        cin >> x >> y;
        cout << (x*y) << endl;

    }
};
int addition()
{
    int a,b,c;
    cin >> a >> b;
    c=a+b;
    cout << c << endl;
    return 0;
}
int main()
{
    addition();
    myfirstclass MFC;
    cout << MFC.a << endl;
    MFC.multiply();
    return 0;
}



