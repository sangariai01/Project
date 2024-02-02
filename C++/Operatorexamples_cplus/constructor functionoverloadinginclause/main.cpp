#include <iostream>

using namespace std;

class constructprgrm
{
public:
    constructprgrm(int a)
    {
    if(a<5)
    {
        cout << "The given value is :" << a << endl;
    }
    }
    constructprgrm(int x , int y)
    {
        cout << "The added value is:" << x+y << endl;
    }
};
 class functoverprgm
 {
 public:
    int Name()
    {
        string name;
        cout << "Enter the name" << endl;
        cin >> name ;
        cout << "The given name is :" << name << endl;
    }

    int Name(string name1 , string name2)
    {
        cout << "Concatenate names are :" << name1 << name2 << endl;
    }
 };

int main()
{    int a;
     cout << "Enter the value :" << endl;
     cin >> a ;
    constructprgrm cp(a);
    int x,y;
    constructprgrm cp1(12,24);
    functoverprgm fop , fop1;
    fop . Name();
    string name1 , name2;
    fop1 . Name("VJ" , "San");
    return 0;
}
