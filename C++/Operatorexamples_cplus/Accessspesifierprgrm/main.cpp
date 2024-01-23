#include <iostream>

using namespace std;

class accessspecifier
{
protected:
    int a=10;
public:
    int print()
    {
        int b;
        b=a;
        cout << "THE GIVEN VALUE IS :" << b << endl;
    }

};
class accsprdemo
{
    private :
    string Name;
    public:
        int demo(string word)
        {
             Name = word;
        cout << "The given name is : " << Name << endl;

        }
};

int main()
{
    accessspecifier as;
    as . print();
    accsprdemo asd;
    string word;
    asd . demo ("san");
    return 0;
}
