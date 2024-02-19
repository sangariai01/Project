from tkinter import *

app=Tk()
app.title("Marklist")
app.geometry("500x500+200+300")
app.config(bg="white")

def insertfun():
    pass

def updatefun():
    pass

def deletefun():
    pass

def resetfun():
    pass

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

lableTotal=Label(app,text="Total")
lableTotal.grid(row=14,column=1)

total=Entry(app,width=10)
total.grid(row=14,column=2)

button1=Button(text="Insert",command=insertfun).grid(row=16,column=3)
button2=Button(text="Update",command=updatefun).grid(row=16,column=4)
button3=Button(text="Delete",command=deletefun).grid(row=16,column=5)
button4=Button(text="Reset",command=resetfun).grid(row=16,column=6)
button5=Button(text="Submit",command=submitfun).grid(row=16,column=7)

app.mainloop()
