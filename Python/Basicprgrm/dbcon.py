from tkinter import *
import mysql.connector

app=Tk()
app.title("Marklist")
app.geometry("500x500+200+300")
app.config(bg="white")

def Mydbconnection():
    con=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_sangari"
    )
    return con
dbcon=Mydbconnection()
print("Connected",dbcon)

def insertfun():
    Name=str(name.get())
    Tamil=int(mark1.get())
    English=int(mark2.get())
    Maths=int(mark3.get())
    Science=int(mark4.get())
    Social=int(mark5.get())
   
    
    e_con=Mydbconnection()
    result=e_con.cursor()
    
    statement="insert into Student_details (Name,Tamil,English,Maths,Science,Social) values(%s,%s,%s,%s,%s,%s);"
    valuepass=(Name,Tamil,English,Maths,Science,Social)
    result.execute(statement,valuepass)
    e_con.commit()
    
    print(result.rowcount,"row inserted")
    
def updatefun():
    Name=str(name.get())
    Tamil=int(mark1.get())
    # English=int(mark2.get())
    # Maths=int(mark3.get())
    # Science=int(mark4.get())
    # Social=int(mark5.get())
   
    
    e_con=Mydbconnection()
    result=e_con.cursor()
    
    statement="update Student_details set Name = (%s) where Sno = (%s) ;"
    valuepass=(Name,Tamil)
    result.execute(statement,valuepass)
    e_con.commit()
    
    print(result.rowcount,"Value Updated")

def deletefun():  
    Name=str(name.get())
    # Tamil=int(mark1.get())
    # English=int(mark2.get())
    # Maths=int(mark3.get())
    # Science=int(mark4.get())
    # Social=int(mark5.get())
   
    
    e_con=Mydbconnection()
    result=e_con.cursor()
    
    statement=" delete from Student_details where Name=(%s);"
    valuepass=(Name,)
    result.execute(statement,valuepass)
    e_con.commit()
    
    print(result.rowcount,"row deleted")

def alterfun():
    Name=str(name.get())
    # Tamil=int(mark1.get())
    # English=int(mark2.get())
    # Maths=int(mark3.get())
    # Science=int(mark4.get())
    # Social=int(mark5.get())
   
    e_con=Mydbconnection()
    result=e_con.cursor()
    
    statement="alter table Student_details drop column " + str(Name)+ ";"
    # valuepass=(Name,)
    result.execute(statement)
    e_con.commit()
    print(statement)
    
    print(result.rowcount,"Value Updated")

def submitfun():
    pass


Label(app,text="Student details",fg="black",font=("Arial",18)).grid(row=0,column=5)


lablename=Label(app,text="Student_Name")
lablename.grid(row=2,column=1)

name=Entry(app,width=10)
name.grid(row=2,column=2)

lableTamil=Label(app,text="Tamil")
lableTamil.grid(row=4,column=1)

mark1=Entry(app,width=10)
mark1.grid(row=4,column=2)

lableEnglish=Label(app,text="English")
lableEnglish.grid(row=6,column=1)

mark2=Entry(app,width=10)
mark2.grid(row=6,column=2)

lableMaths=Label(app,text="Maths")
lableMaths.grid(row=8,column=1)

mark3=Entry(app,width=10)
mark3.grid(row=8,column=2)

lableScience=Label(app,text="Science")
lableScience.grid(row=10,column=1)

mark4=Entry(app,width=10)
mark4.grid(row=10,column=2)

lableSocial=Label(app,text="Social")
lableSocial.grid(row=12,column=1)

mark5=Entry(app,width=10)
mark5.grid(row=12,column=2)

# lableTotal=Label(app,text="Total")
# lableTotal.grid(row=14,column=1)

# total=Entry(app,width=10)
# total.grid(row=14,column=2)

button1=Button(text="Insert",command=insertfun).grid(row=16,column=3)
button2=Button(text="Update",command=updatefun).grid(row=16,column=4)
button3=Button(text="Delete",command=deletefun).grid(row=16,column=5)
button4=Button(text="ALTER",command=alterfun).grid(row=16,column=6)
button5=Button(text="Submit",command=submitfun).grid(row=16,column=7)

app.mainloop()
