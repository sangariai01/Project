class google():
    def __init__(self):
        print("Welcome to google")
    def login(self,user_id,password):
        print("Your user_id is ",user_id,"and password is ",password)
       
#x=google()
#x.login(user_id=input("Enter the user id:"),password=input("Enter the password:"))

class microsoft(google):
    def __init__(self):
        print("Welcome to microsoft")
        super().__init__()
        super().login(user_id=input("Enter the user id:"),password=input("Enter the password:"))
    def signin(self,user_name,pswd):
        print("The given user name is",user_name,"and the password is",pswd)
y=microsoft()
y.signin(user_name=input("Enter the user name:"),pswd=input("Enter the pasword:"))

class user(google):
    def __init__(self):
        super().__init__()
        super().login(user_id=input("Enter the user id:"),password=input("Enter the password:"))
        pass
z=user()




