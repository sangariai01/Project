class google():
    def __init__(self):
        print("Welcome to google")
    def map(self):
        print("Here you can find the location")
    def files(self):
        print("Here you can store all your datas")
#g=google()
#g.map()
#g.files()

class microsoft():
    def __init__(self):
        print("Welcome to microsoft office")
        super().__init__()
        super().map()
        super().files()      
    def word(self):
        print("Enter your word Document")
    def Excel(self):
        print("Welcome to excel")
#h=microsoft()
#h.word()
#h.Excel()

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













     