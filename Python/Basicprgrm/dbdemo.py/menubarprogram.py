import tkinter as tk

win=tk.Tk()
win.title("Notepad")
win.geometry("500x500")

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
    

menubar=tk.Menu(win)

filemenu=tk.Menu(menubar,tearoff=0)
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

editmenu=tk.Menu(menubar,tearoff=0)
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

formatmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu,underline=0)
formatmenu.add_command(label="Word Wrap",underline=0)
formatmenu.add_command(label="Font",underline=0)
                       
viewmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu,underline=0)
viewmenu.add_command(label="Status Bar",underline=0)

helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)
helpmenu.add_command(label="View Help",underline=0)
helpmenu.add_command(label="About Notepad",command=about,underline=0)
                      
win.config(menu=menubar)
win.mainloop()