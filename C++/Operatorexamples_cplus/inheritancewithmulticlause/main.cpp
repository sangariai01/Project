#include <iostream>

using namespace std;

class details
{

private :
    int Id;
    string name ;
public :
     void list ()
     {
         cout << " Print the name :" << endl;
         cin >>  name ;
         cout << " Print the Id:" << endl;
         cin >> Id ;
     }
       string show_name()
   {
       return name;
   }
     int show_Id()
    {
        return Id;
    }

};

class information : public details
{
private :
    string location;
    int age;
public :
   void info()
   {
    cout << "Enter the location :" << endl;
    cin >> location ;
    cout << "Enter the age :" << endl;
    cin >> age ;
   }
   string show_location()
   {
       return location;
   }
   int ade_details()
   {
       return age;
   }
};
int main()
{
    information i;
    i . list();
    i . info ();
    cout << "The name is :" <<i . show_name() << endl;
    cout << "The Id is :" <<i . show_Id() << endl;
    cout << "The location is :" <<i . show_location() << endl;
    cout << "The age is :" <<i . ade_details() << endl;
   return 0;
}
