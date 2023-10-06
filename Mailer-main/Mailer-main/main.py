from tkinter import *
import os

def run():
    main = Tk()
    main.geometry("1000x800")
    main.title("Mailer")
    photo = PhotoImage(file="Logo.png")
    main.iconphoto(False,photo)

    
    f = open("current.status","r")
    creds = f.read().split(" ")
    email = creds[0]
    passwd = creds[1]
    print(email)
    print(passwd)
    f.close()
    
   # email = "mailer.service.public@gmail"
   # passwd = "ozlhpygpbuzubkom"

    #user stettings 

    from User import User
    u = User(main)
    butt1 = Button(main,text="User Settings",height=10,width=50,font=("Roman",13,"bold"),bg="#f59207",fg="#db3c18",command=u.user_db)
    butt1.pack(pady=20)

    #Send Mail
    from mail_send import mail_send
    m = mail_send(main,email,passwd)

    butt2 = Button(main,text="Send Mail",height=10,width=50,font=("Roman",13,"bold"),bg = "#10b328",fg="#056e25",command=m.send_mails)
    butt2.pack(pady=20)

#Read mail
    from mail_read import mail_read
    m = mail_read(main,email,passwd)
    butt3 = Button(main,text="Read",height=10,width=50,font=("Roman",13,"bold") ,bg = "#0dd6c2",fg="#0e078f",command=m.mail_reads)
    butt3.pack(pady=20)

    main.mainloop()

    return None



key = 0
if os.path.isfile("current.status") == False :
    
    from setup_repair import setup_repair
    setup_repair().setup()
    key = 1

try :
    
    f = open("current.status","r")
    listing = f.read().split(" ")
    a,b = listing[0],listing[1]
    f.close()
    run()
    

except:
    if key == 0 :
        from setup_repair import setup_repair
        setup_repair().setup()



