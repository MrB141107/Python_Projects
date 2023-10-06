import sqlite3
from tkinter import *



class User(object):
    def __init__(self,toplevel):
        self.toplevel = toplevel
    
    def user_db(self):

        conn = sqlite3.connect("Users.db")
        curr = conn.cursor()
        try:
            curr.execute("""CREATE TABLE User(User TEXT NOT NULL,Email TEXT NOT NULL,Passwd TEXT NOT NULL,PRIMARY KEY(Email))""")
            
        except:
            print("Table Created")

        window = Toplevel(self.toplevel)
        window.geometry("1000x800")
        window.title("User Management")
        photo = PhotoImage(file="Logo.png")
        window.iconphoto(False,photo)

        #add user

        def popup_entry():



            def entry():
                user = e1.get()
                email = e2.get()
                passwd = e3.get()
                try:
                    curr.execute(f"""INSERT INTO User(User,Email,Passwd) VALUES("{user:s}","{email:s}","{passwd:s}")""".format(user=user,email=email,passwd=passwd))
                    conn.commit()
                    label.config(text = "USER EMAIL Saved")
                except:
                    
                    label.config(text = "USER EMAIL ALREADY EXISTS")
                   
                return None
            

            
            popup = Toplevel(window)
            popup.title("Enter Details")
            popup.geometry("400x400")
          
            
            #add name

            Label(popup,text="Enter Name",font=("Comic San MS",13,"bold")).pack()
            e1 = Entry(popup,width=60)
            e1.pack()

            #add email
            Label(popup,text="Enter Email",font=("Comic San MS",13,"bold")).pack()
            e2 = Entry(popup,width=60,)
            e2.pack()

            #add password
            default = StringVar()
            default.set("Enter your App password ")
            Label(popup,text="Enter Password",font=("Comic San MS",13,"bold")).pack()
            e3 = Entry(popup,width=60,textvariable=default)
            e3.pack()

            label = Label(popup,text=" ")
            label.pack(pady=20)

            #save

            buttp1 = Button(popup,text="Save",height=5,width=30,command=entry,font=("Comic San MS",13,"bold"),fg="#423d01",bg="#fce805")
            buttp1.pack(side="bottom")

            popup.mainloop()

            return None

        butt1 = Button(window,text="Add user",height=10,width=50,command=popup_entry,font=("Roman",13,"bold"),bg="#01290f",fg="#03fc5a")
        butt1.pack(pady=20)




        #delete User

        def popup_delete():

            popup1 = Tk()
            popup1.title("Delete USER")
            popup1.geometry("400x400")
           
            
            def delete():
                
                try:
                    
                    user = clicked.get()
                    curr.execute(f"""Delete From User Where User = "{user:s}" """.format(user=user))
                    if clicked.get() == None :
                        label.config("Empty List")
                    else:
                        label.config(text="Deleted Sucessfully")
                    conn.commit()
                except :
                    label.config(text="No Changes Made")
                return None
            
            menu = curr.execute("""SELECT * FROM User""").fetchall()
            menu = [i[0] for i in menu]
            

            clicked = StringVar()
            clicked.set("Select User")

            try:
                drop = OptionMenu(popup1,clicked,*menu)
                drop.pack()
                drop.config(width=50)
            except:
                pass
            butt3 = Button(popup1,text="Delete User",command=delete,font=("Comic San MS",13,"bold"),fg="#423d01",bg="#fce805")
            butt3.pack()

            label = Label(popup1,text=" ")
            label.pack()

            popup1.mainloop()
            return None

        butt2 = Button(window,text="Delete User",height=10,width=50,command=popup_delete,font=("Roman",13,"bold"),bg="#290103",fg="#fc050d")
        butt2.pack(pady=20)



        #Change user


        def popup_change():

            popup3 = Tk()
            popup3.geometry("400x400")
            popup3.title("Change User")
       
            

            def change():
                
                f = open("current.status","r")
                inp = f.read().split(" ")
                f.close()
                print(inp)
                
                email = inp[0]
                passwd = inp[1]

                for i in Menu :
                    if(i[0] == clicked.get()) and i[1] != "Enter your App password":
                        email = i[1]
                        passwd = i[2] 
                        label.config(text="User Changed Successfully . Pls Restart App Now ")
                    

                f = open("current.status","w")
                stri = email+" "+passwd
                f.write(stri)
                f.close()          

                return None

            Menu = curr.execute("""SELECT * FROM User""").fetchall()
            menu = [i[0] for i in Menu]
            
            clicked = StringVar()
            clicked.set("Select User")

            try:
                drop1 = OptionMenu(popup3,clicked,*menu)
                drop1.pack()
                drop1.config(width=50)
            except:
                pass
            
            label = Label(popup3,text=" ")
            label.pack()
            butt5 = Button(popup3,text="Change User",command=change,font=("Comic San MS",13,"bold"),fg="#423d01",bg="#fce805")
            butt5.pack(pady=20)

            popup3.mainloop()
            return None
        
        butt4 = Button(window,text="Change User",height=10,width=50,command=popup_change,font=("Roman",13,"bold"),bg="#7b0dba",fg="#2b0640")
        butt4.pack(pady=20)
        window.mainloop()

        return None

"""

main = Tk()
email1 = "mailer.service.public@gmail.com"
passwd = "ozlhpygpbuzubkom"
m = User(main)
butt1 = Button(main,text = "press here",command=m.user_db)
butt1.pack()
main.mainloop()

"""
