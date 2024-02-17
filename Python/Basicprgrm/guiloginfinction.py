from tkinter import *
app=Tk()
app.geometry("500x500")

def getvalue():
    print("Accepted")

Label(app,text="Registration form").grid(row=0,column=1)

name = Label(app, text="Name").grid(row=1,column=2)
age = Label(app, text="Age").grid(row=2,column=2)
gender = Label(app, text="Gender").grid(row=3,column=2)
phone = Label(app, text="phone").grid(row=4,column=2)
qualification = Label(app, text="Qualification").grid(row=5,column=2)

namevalue = StringVar
agevalue = StringVar
gendervalue = StringVar
phonevalue = StringVar
qualificationvalue = StringVar

nameentry = Entry(app, textvariable=namevalue).grid(row=1, column=3)
agevalue = Entry(app, textvariable=agevalue).grid(row=2, column=3)
gendervalue = Entry(app, textvariable=gendervalue).grid(row=3, column=3)
phonevalue  = Entry(app, textvariable=phonevalue).grid(row=4, column=3)
qualificationvalue  = Entry(app, textvariable=qualificationvalue).grid(row=5, column=3)                           

checkbtn = Checkbutton(text="Remember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

Button(text="Submit",command=getvalue).grid(row=7,column=3)

app.mainloop()