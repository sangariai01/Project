from tkinter import*

win=Tk()
win.title("Concatination")
win.geometry("600x600+500+100")
win.config(bg="green")
win.state("zoomed")

def names():
    fn=str(name1.get())
    ln=str(name2.get())
    fullname=fn+" "+ln
    print(fullname)
    labeloutput1.config(text=fullname)

def Add():
    fn=int(name1.get())
    ln=int(name2.get())
    fullname=fn+ln
    print(fullname)
    labeloutput1.config(text=fullname)

def Sub():
    fn=int(name1.get())
    ln=int(name2.get())
    fullname=fn-ln
    print(fullname)
    labeloutput1.config(text=fullname)

def Multiple():
    fn=int(name1.get())
    ln=int(name2.get())
    fullname=fn*ln
    print(fullname)
    labeloutput1.config(text=fullname)

def Divid():
    fn=int(name1.get())
    ln=int(name2.get())
    fullname=fn/ln
    print(fullname)
    labeloutput1.config(text=fullname)
  
lableTitle=Label(win,text="Concatinate Function",fg="red",font=("Algerian",18))
lableTitle.grid(row=0,column=20,padx=150,pady=50)

labelmsg=Label(win,text="Enter the 1st name:",fg="blue",font=("Cooper Black",12))
labelmsg.grid(row=2,column=10,padx=10,pady=20)

name1=Entry(win,width=50,fg="red",font=("12"))
name1.grid(row=2,column=20,padx=10,pady=20)

labelmsg=Label(win,text="Enter the 2nd name:",fg="blue",font=("Cooper Black",12))
labelmsg.grid(row=4,column=10,padx=15,pady=20)

name2=Entry(win,width=50,fg="red",font=("12"))
name2.grid(row=4,column=20,padx=15,pady=20)

outputbox=Label(win,text="Output:",fg="blue",font=("Cooper Black",12))
outputbox.grid(row=6,column=10,padx=20,pady=20)

labeloutput1=Label(win,width=50,font=("12"))
labeloutput1.grid(row=6,column=20,padx=20,pady=20)


btncnct1=Button(win,text="Concatenate",command=names,fg="orange",font=("Cooper Black",12))
btncnct1.grid(row=20,column=5,padx=25,pady=50)

btncnct2=Button(win,text="Addition",command=Add,fg="orange",font=("Cooper Black",12))
btncnct2.grid(row=20,column=10,padx=25,pady=50)

btncnct3=Button(win,text="Subtraction",command=Sub,fg="orange",font=("Cooper Black",12))
btncnct3.grid(row=20,column=15,padx=25,pady=50)

btncnct4=Button(win,text="Multiplication",command=Multiple,fg="orange",font=("Cooper Black",12))
btncnct4.grid(row=20,column=20,padx=25,pady=50)

btncnct4=Button(win,text="Divition",command=Divid,fg="orange",font=("Cooper Black",12))
btncnct4.grid(row=20,column=25,padx=25,pady=50)


win.mainloop()  
