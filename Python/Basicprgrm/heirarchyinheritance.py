class google():
    def __init__(self):
        print("Welcomr to google family")
    def chrome(self):
            print("Hi... Welcome to chrome")
#g=google()
#g.chrome()
            
class gmail(google):
    def __init__(self):
        print("Welcome to gmail")
        super().chrome()
    def account(self):
        print("Log in your gmail account")
#x=gmail()
#x.account()

class drive(gmail):
    def __init__(self):
        print("Welcome to google drive")
        super().chrome()
        super().account()
#y=drive()

class photos(drive):
     pass
z=photos()

class microsoft():
    def __init__(self):
        print("Welcome to microsoft office")
        super().__init__()
        super().chrome()   
    def word(self):
        print("Enter your word Document")
    def Excel(self):
        print("Welcome to excel")

class user(microsoft,google):
    def __int__(self):
        print("Welcome to the network world")
        super().__init__()
    def login(self):
        print("Login your Id")

u=user()
u.word()
u.Excel()
u.login()
