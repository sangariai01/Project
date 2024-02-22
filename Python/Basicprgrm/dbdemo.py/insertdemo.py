from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into MySQL DB Demo")
win.geometry("300x300")

class frameDBoperations:
    def __init__(self):
        frametop=Frame(win, bg="black",width=800, height=300, padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT").pack(padx=10, pady=10)
        btnupdate=Button(frametop,text="UPDATE").pack(padx=10, pady=10)
        btndelete=Button(frametop,text="DELETE").pack(padx=10, pady=10)

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