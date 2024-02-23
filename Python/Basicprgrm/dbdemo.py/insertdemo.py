from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into MySQL DB Demo")
win.geometry("300x300")

def Mydbconnection():
    con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sangari@2024",
    database="ai_sangari"
    )
    return con                                                                                               

def insertfun(self):
    Name=str(name.get())
    Tamil=int(mark1.get())
    English=int(mark2.get())
    Maths=int(mark3.get())
    Science=int(mark4.get())
    Social=int(mark5.get())
                                                
                                                    
    # e_con=Mydbconnection()
    # result=e_con.cursor()
                                                    
    statement="insert into Student_details (Name,Tamil,English,Maths,Science,Social) values(%s,%s,%s,%s,%s,%s);"
    valuepass=(Name,Tamil,English,Maths,Science,Social)
    result.execute(statement,valuepass)
    e_con.commit()
                                                    
    print(result.rowcount,"row insert")
        

class frameDBoperations:
    def __init__(self):
        frametop=Frame(win, bg="black",width=800, height=300, padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT",command=self.insert).pack(padx=10, pady=10)
        btnupdate=Button(frametop,text="UPDATE").pack(padx=10, pady=10)
        btndelete=Button(frametop,text="DELETE").pack(padx=10, pady=10)

    

Label(win,text="Student details",fg="black",font=("Arial",18)).grid(row=0,column=5)


lablename=Label(win,text="Student_Name")
lablename.grid(row=2,column=1)

name=Entry(win,width=10)
name.grid(row=2,column=2)

lableTamil=Label(win,text="Tamil")
lableTamil.grid(row=4,column=1)

mark1=Entry(win,width=10)
mark1.grid(row=4,column=2)

lableEnglish=Label(win,text="English")
lableEnglish.grid(row=6,column=1)

mark2=Entry(win,width=10)
mark2.grid(row=6,column=2)

lableMaths=Label(win,text="Maths")
lableMaths.grid(row=8,column=1)

mark3=Entry(win,width=10)
mark3.grid(row=8,column=2)

lableScience=Label(win,text="Science")
lableScience.grid(row=10,column=1)

mark4=Entry(win,width=10)
mark4.grid(row=10,column=2)

lableSocial=Label(win,text="Social")
lableSocial.grid(row=12,column=1)

mark5=Entry(win,width=10)
mark5.grid(row=12,column=2)

     

run=frameDBoperations()
win.mainloop()



# from tkinter import *
# import mysql.connector

# win=Tk()

# win.title("Insert into MySQL DB Demo")
# win.geometry("500x500")

# frameleft=Frame(win,bg="black",width=500,height=500,padx=30,pady=30)
# frameleft.pack(side=LEFT)

# frameright=Frame(win,bg="red",width=500,height=500)
# frameright.pack(side=RIGHT)

# lbl_Title_of_Operation=Label(frameleft,text="Insert into MySQL DB Demo")
# lbl_Title_of_Operation.grid(row=0,columnspan=5)

# lblName=Label(frameleft,text="Name")
# lblName.grid(row=2,colunm=1,padx=30,pady=30)


# win.mainloop()