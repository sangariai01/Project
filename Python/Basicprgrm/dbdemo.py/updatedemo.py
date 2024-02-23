from tkinter import *
import mysql.connector

win=Tk()

win.title("Update into MySQL DB Demo")
win.geometry("300x300")

def Mydbconnection(self):
        con=mysql.connector.connect(
        host="192.168.1.240",
        user="AIBATCH01",
        password="AI@123",
        database="ai_sangari"
        )
        return con 

class frameDBoperations:
    def __init__(self):
        frametop=Frame(win, bg="black",width=800, height=300, padx=10,pady=10)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="UPDATE",command=self.updatefun).pack(padx=10, pady=10)
        # btnupdate=Button(frametop,text="UPDATE").pack(padx=10, pady=10)
        # btndelete=Button(frametop,text="DELETE").pack(padx=10, pady=10)

                                                                                                
    def updatefun(self):
        neww=Tk()
        neww.title("Update Function")
        neww.geometry("500x500")   
        
        frameupdate=Frame(neww, bg="white",width=500, height=500, padx=30,pady=30)
        frameupdate.pack(side =LEFT)
        
        btninsert=Button(frameupdate,text="Submit",command=neww).grid(row=15,column=5)
              
        Label(frameupdate,text="Student details",fg="black",font=("Arial",18)).grid(row=0,column=5)


        lablename=Label(frameupdate,text="Student_Name")
        lablename.grid(row=2,column=1)

        name=Entry(frameupdate,width=10)
        name.grid(row=2,column=2)

        lableTamil=Label(frameupdate,text="Tamil")
        lableTamil.grid(row=4,column=1)

        mark1=Entry(frameupdate,width=10)
        mark1.grid(row=4,column=2)

        Name=name.get()
        Tamil=mark1.get()

        e_con=Mydbconnection(self)
        result=e_con.cursor()
                                                        
        statement="update Student_details set Name = (%s) where Sno = (%s) ;"
        valuepass=(Name,Tamil)
        result.execute(statement,valuepass)
        e_con.commit()
                                                        
        print(result.rowcount,"row updated")

        neww.mainloop()



run=frameDBoperations()
win.mainloop()