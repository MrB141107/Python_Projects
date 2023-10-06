#Logic Tested Ok


from tkinter import *


class setup_repair(object):
    def __init__(self):
      
        return None
    
    def setup(self):
        win = Tk()
        win.geometry("400x400")
        win.title("Setup/Repair")
        Label(win,text="Enter Your Email",width=50,font=("Roman",15,"bold")).pack()
        e1 = Entry(win,width=50)
        e1.pack()
        Label(win,text="Enter Your App Password",width=50,font=("Roman",15,"bold")).pack()
        e2 = Entry(win,width=50)
        e2.pack()

        def save():
            f = open("current.status" ,"w")
            str = ""
            str += e1.get()
            str += " "
            str += e2.get()
            f.write(str)
            f.close()
            return None
        
        Button(win,text="Save",width=30,height=5,command=save,font=("Roman",15,"bold"),fg="green",bg="white").pack()
        win.mainloop()

        return None






