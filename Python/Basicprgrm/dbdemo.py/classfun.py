import os
from tkinter import *
from tkinter import ttk
import mysql.connector
from subclassfun import DBManipulate

win=Tk()
win.title("Student Management System")
win.geometry("500x500")
# win.wm_iconbitmap('classfuns.ico')
dbcon=DBManipulate()

def quit():
    win.destroy()
    
def new():
    import tkinter as tk

    win=tk.Tk()
    win.title("New tab")
    win.geometry("300x300")
    win.mainloop()
    
def about():
    import tkinter as tk

    win=tk.Tk()
    win.title("New tab")
    win.geometry("300x300")
    
    info=("""Microsoft Windows
          Version 6.3((Build 9600)
          2013 Microsoft Corporation.All rights reservved.
          
          The Windows 8.1 Pro operating system and its user interface are
          protected by traademark and other pending existing intellectual propertty
          righhts in the United States""")  
    abt=tk.Label(win,text=info)
    abt.pack()
    win.mainloop()
    

menubar=Menu(win)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
filemenu.add_command(label="New",underline=0,command=new,accelerator="Ctrl+N")
filemenu.add_command(label="Open",underline=0,accelerator="Ctrl+O")
filemenu.add_command(label="Save",underline=0,accelerator="Ctrl+S")
filemenu.add_command(label="Save as",underline=0)
filemenu.add_separator()
filemenu.add_command(label="Page setup",underline=0)
filemenu.add_command(label="Print",underline=0,accelerator="Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=0,command=quit,accelerator="Ctrl+E")

editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu,underline=0)
editmenu.add_command(label="Undo",underline=0,accelerator="Ctrl+Z")
editmenu.add_separator()
editmenu.add_command(label="Cut",underline=0,accelerator="Ctrl+X")
editmenu.add_command(label="Copy",underline=0,accelerator="Ctrl+C")
editmenu.add_command(label="Paste",underline=0,accelerator="Ctrl+V")
editmenu.add_command(label="Delete",underline=0,accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Find",underline=0,accelerator="Ctrl+F")
editmenu.add_command(label="Find Next",underline=0,accelerator="F3")
editmenu.add_command(label="Replace",underline=0,accelerator="Ctrl+H")
editmenu.add_command(label="Go To",underline=0,accelerator="Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All",underline=0,accelerator="Ctrl+A")
editmenu.add_command(label="Time/Date",underline=0,accelerator="F5")

formatmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu,underline=0)
formatmenu.add_command(label="Word Wrap",underline=0)
formatmenu.add_command(label="Font",underline=0)
                       
viewmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu,underline=0)
viewmenu.add_command(label="Status Bar",underline=0)

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)
helpmenu.add_command(label="View Help",underline=0)
helpmenu.add_command(label="About Notepad",command=about,underline=0)

win.config(menu=menubar)

# imgdir=os.path.join(os.path.dirname(__file__),'img')
# getTitleImage=PhotoImage('titleimage',file=os.path.join(imgdir,'poster.gif'))

titleImageFrame=Frame(win, bg="black")
titleImageFrame.pack(padx=10,fill="x")

tablist=ttk.Notebook(win)
tablist.pack(padx=10, pady=5)

tabInsert=ttk.Frame(tablist, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
tabInsert.pack()

tabUpdate=ttk.Frame(tablist, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
tabUpdate.pack()

tabDelete=ttk.Frame(tablist, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
tabDelete.pack()

tablist.add(tabInsert,text="Insert")
tablist.add(tabUpdate,text="Update")
tablist.add(tabDelete,text="Delete")

titledisplayframeintab=Frame(tabInsert,width=win.winfo_screenwidth(), height=win.winfo_screenheight())
titledisplayframeintab.pack()

lbl_insertTitle=Label(titledisplayframeintab, text="Inserting Student Details")
lbl_insertTitle.grid(pady=10,row=0, columnspan=10)

lablename=Label(titledisplayframeintab,text="Student_Name")
lablename.grid(row=2,column=1)

name=Entry(titledisplayframeintab,width=10)
name.grid(row=2,column=2)

lableTamil=Label(titledisplayframeintab,text="Tamil")
lableTamil.grid(row=4,column=1)

mark1=Entry(titledisplayframeintab,width=10)
mark1.grid(row=4,column=2)

lableEnglish=Label(titledisplayframeintab,text="English")
lableEnglish.grid(row=6,column=1)

mark2=Entry(titledisplayframeintab,width=10)
mark2.grid(row=6,column=2)

lableMaths=Label(titledisplayframeintab,text="Maths")
lableMaths.grid(row=8,column=1)

mark3=Entry(titledisplayframeintab,width=10)
mark3.grid(row=8,column=2)

lableScience=Label(titledisplayframeintab,text="Science")
lableScience.grid(row=10,column=1)

mark4=Entry(titledisplayframeintab,width=10)
mark4.grid(row=10,column=2)

lableSocial=Label(titledisplayframeintab,text="Social")
lableSocial.grid(row=12,column=1)

mark5=Entry(titledisplayframeintab,width=10)
mark5.grid(row=12,column=2)

btninsert=Button(titledisplayframeintab,text="Submit").grid(row=15,column=5)

Name=name.get()
Tamil=mark1.get()
English=mark2.get()
Maths=mark3.get()
Science=mark4.get()
Social=mark5.get()
                                                                                                   
result=dbcon.cursor()
                                                        
statement="insert into Student_details (Name,Tamil,English,Maths,Science,Social) values(%s,%d,%d,%d,%d,%d);"
valuepass=(Name,Tamil,English,Maths,Science,Social)
result.execute(statement,valuepass)
dbcon.commit()
                                                        
print(result.rowcount,"row insert")

titledisplayframeintab=Frame(tabUpdate,width=win.winfo_screenwidth(), height=win.winfo_screenheight())
titledisplayframeintab.pack()

lbl_updateTitle=Label(titledisplayframeintab, text="Updating Student Details")
lbl_updateTitle.grid(pady=10,row=0, columnspan=10)

lablename=Label(titledisplayframeintab,text="Student_Name")
lablename.grid(row=2,column=1)

name=Entry(titledisplayframeintab,width=10)
name.grid(row=2,column=2)

lableTamil=Label(titledisplayframeintab,text="Condition")
lableTamil.grid(row=4,column=1)

mark1=Entry(titledisplayframeintab,width=10)
mark1.grid(row=4,column=2)

btnupdate=Button(titledisplayframeintab,text="Submit").grid(row=15,column=5)

Name=name.get()
Tamil=mark1.get()

result=dbcon.cursor()
                                                        
statement="update Student_details set Name = (%s) where Sno = (%s) ;"
valuepass=(Name,Tamil)
result.execute(statement,valuepass)
dbcon.commit()

print(result.rowcount,"row updated")

btnupdate=Button(titledisplayframeintab,text="Submit").grid(row=15,column=5)

Name=name.get()
Tamil=mark1.get()

titledisplayframeintab=Frame(tabDelete,width=win.winfo_screenwidth(), height=win.winfo_screenheight())
titledisplayframeintab.pack()

lbl_updateTitle=Label(titledisplayframeintab, text="Deleting Student Details")

lablename=Label(titledisplayframeintab,text="Student_Name")
lablename.grid(row=2,column=1)

name=Entry(titledisplayframeintab,width=10)
name.grid(row=2,column=2)

btndelete=Button(titledisplayframeintab,text="Submit").grid(row=15,column=5)

Name=name.get()

result=dbcon.cursor()
                                                        
statement=" delete from Student_details where Name=(%s);"
valuepass=(Name,)
result.execute(statement,valuepass)
dbcon.commit()

print(result.rowcount,"row deleted")

msg=dbcon.Mydbconnection()
lblConMsg=Label(titledisplayframeintab, text=msg)
lblConMsg.grid(row=8,column=2, pady=20)

win.mainloop()
