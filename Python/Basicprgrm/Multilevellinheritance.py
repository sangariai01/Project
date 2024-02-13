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


         