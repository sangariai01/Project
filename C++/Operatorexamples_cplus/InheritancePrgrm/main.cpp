#include <iostream>

using namespace std;

class biodata
{
public:
    string quotes = "Welcome";

    int details()
    {
        string name ="Sangari";
        cout << "The name is :" << name << endl;

    }

};
class resume : public biodata
{

};

int main()
{
    resume rs;
    rs . details();
    return 0;
}
