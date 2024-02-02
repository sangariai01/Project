#include <iostream>

using namespace std;

class biodata
{
public:
    string quotes = "Welcome";

    int details()
    {
        string name ="Sangari";
        cout << "My dear " << name << endl;

    }

};
class resume : public biodata
{

};

int main()
{
    resume rs;
    cout << rs . quotes << endl;
    rs . details();
    return 0;
}
