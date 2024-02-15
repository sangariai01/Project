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
    labeloutput.config(text=fullname)
    
lableTitle=Label(win,text="Concatinate Function",fg="red",font=("Algerian",18))
lableTitle.grid(row=0,column=10,padx=150,pady=50)

labelmsg=Label(win,text="Enter the 1st name:",fg="blue",font=("Cooper Black",12))
labelmsg.grid(row=2,column=20,padx=25,pady=50)

name1=Entry(win,width=50,fg="red",font=("12"))
name1.grid(row=2,column=25,padx=25,pady=50)

labelmsg=Label(win,text="Enter the 2nd name:",fg="blue",font=("Cooper Black",12))
labelmsg.grid(row=6,column=20,padx=25,pady=50)

name2=Entry(win,width=50,fg="red",font=("12"))
name2.grid(row=6,column=25,padx=25,pady=50)

outputbox=Label(win,text="Output:",fg="blue",font=("Cooper Black",12))
outputbox.grid(row=10,column=20,padx=25,pady=50)

labeloutput=Label(win,width=50,font=("12"))
labeloutput.grid(row=10,column=25,padx=25,pady=50)

btncnct=Button(win,text="Concatenate",command=names,fg="orange",font=("Cooper Black",12))
btncnct.grid(row=10,column=10,padx=25,pady=50)

win.mainloop()  
