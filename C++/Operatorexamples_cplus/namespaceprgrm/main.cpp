#include <iostream>

using namespace std;

int main()
{
    string student;
        cout << " enter the string value " << endl;
        cin >> student;
        cout << " The given student name is :" << student << endl;
       fflush(stdin);
       cout << " enter the string value " << endl;
        getline(cin,student);
        cout << student << endl;
cout << "------------------------------" << endl;
        cout << " Enter the names :" << endl;
        string name1;
        string name2;
        string Names;
        cin >> name1;
        cin >> name2;
        cout << name1+" "+name2 << endl;
        Names = name1.append(name2);
        cout << "The name is :" << Names << endl;
        cout << name1 << endl;
         cout << name1.length() << endl;
          cout << name1.size() << endl;
cout << "------------------------------" << endl ;
        string value;
          cin >> value;
          value.push_back('v');
          cout << value << endl;
          value.insert(0, "san");
          cout << value << endl;
    return 0;
}
