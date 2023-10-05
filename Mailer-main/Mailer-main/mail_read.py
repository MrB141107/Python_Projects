#Logic Tested Ok


import imaplib
import email
from tkinter import *


class mail_read(object):
    def __init__(self,toplevel,email,passwd):
        self.toplevel = toplevel
        self.Email = email
        self.passwd = passwd
        self.arr = list()
        return None
    
    def mail_reads(self):

        window = Toplevel(self.toplevel)
        window.geometry("1000x800")
        window.title("Read Mails")
        photo = PhotoImage(file="Logo.png")
        window.iconphoto(False,photo)

      
    
        def mail_reading(self):
            Email = self.Email
            passwd = self.passwd

            server = imaplib.IMAP4_SSL("imap.gmail.com")

            server.login(Email,passwd)

            server.select('Inbox')

            _,msgnums = server.search(None,'ALL')

            for msgnum in msgnums[0].split() :
                _, mess = server.fetch(msgnum, '(RFC822)')
                data = email.message_from_bytes(mess[0][1])
                
              
                
                subject = data.get('Subject')
                content = []
                    
                for i in data.walk():
                    if data.get_content_type() == "text/plain" :
                        content.append(i.as_string())
                
                
                string = ""

                for i in content :
                    string += i
                if string == None :
                    string = "......"

                if subject != None:
                    text = subject+"\n"+string+"\n"+"\n"
                    self.arr.append(text)
            
            return None
        
        def cmd1():
            mail_reading(self)
            for i in self.arr:
                listbox.insert(0,i)
            return None
        
        l1 = Label(window,text="Veiw Mail",width=30,font=("Comic Sans MS",20,"bold"))
        l1.pack()

        scroll = Scrollbar(window)
        scroll.pack(side="right",fill="both")

        listbox = Listbox(window, width=150, height=40,font=("Arial",10,"bold"))
        listbox.config(yscrollcommand= scroll.set)
        listbox.pack()

        butt1 = Button(window,text="Refresh Mail",width=30,height=5,command=cmd1,font=("Comic Sans MS",20,"bold"),bg="green",fg="white")
        butt1.pack(side="left")

        window.mainloop()
        return None
    
"""
main = Tk()
email1 = "mailer.service.public@gmail.com"
passwd = "ozlhpygpbuzubkom"
m = mail_read(main,email1,passwd)
butt1 = Button(main,text = "press here",command=m.mail_reads)
butt1.pack()
main.mainloop()

"""

