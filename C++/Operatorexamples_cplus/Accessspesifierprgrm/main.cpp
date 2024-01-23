#include <iostream>

using namespace std;

class accessspecifier
{
protected:
    int a=10;

private :
    string Name = "VJsan" ;

public:
    int print()
    {
        int b;
       string word;
        b=a;
        cout << "THE GIVEN VALUE IS :" << b << endl;
        word = Name;
        cout << "The given name is : " << word << endl;
    }

};

int main()
{
    accessspecifier as;
    as . print();
    return 0;
}
