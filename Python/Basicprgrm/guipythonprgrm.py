from tkinter import*

win=Tk()
win.title("Concatinate Function")
win.geometry("600x600+500+100")
win.state("zoomed")

def names():
    fn=str(name1.get())
    ln=str(name2.get())
    fullname=fn+" "+ln
    labeloutput.config(text=fullname)
    
lableTitle=Label(win,text="Concatinate Function")
lableTitle.grid(row=0,column=10,padx=50,pady=50)

labelmsg=Label(win,text="Enter the 1st name:")
labelmsg.grid(row=1,column=20)

name1=Entry(win,width=50)
name1.grid(row=1,column=25)

labelmsg=Label(win,text="Enter the 2nd name:")
labelmsg.grid(row=2,column=20)

name2=Entry(win,width=50)
name2.grid(row=2,column=25)

outputbox=Label(win,text="Output:")
outputbox.grid(row=3,column=20)

labeloutput=Label(win,width=50)
labeloutput.grid(row=3,column=25)

btncnct=Button(win,text="Concatenate",command=names)
btncnct.grid(row=4,column=10)

win.mainloop()  
