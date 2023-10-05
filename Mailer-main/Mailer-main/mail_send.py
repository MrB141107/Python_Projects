#Logic Tested Ok


import smtplib
from tkinter import *
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from tkinter.filedialog import askopenfilename
from email import encoders
import os
import pandas as pd


class mail_send(object):

    def __init__(self,toplevel,email,passwd):
        self.sender_mail = email
        self.passwd = passwd
        self.toplevel = toplevel
        return None


    def send_mails(self):
        sender_mail = self.sender_mail
        passwd = self.passwd
        file_data = []
        mailing_list = list()

        window = Toplevel(self.toplevel)
        photo = PhotoImage(file="Logo.png")
        window.iconphoto(False,photo)
        

        def send_mail():

            server = smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(sender_mail,passwd)
            
            recv =  e1.get()
            mailing_list.append(recv)
            content = t1.get("1.0","2000.0")

            for i in mailing_list:
                msg = MIMEMultipart()
                msg['Subject'] = s1.get()
                msg['From'] = sender_mail+".cc"
                msg['To'] = i+".cc"
                text = MIMEText(content,'plain')
                if len(file_data) != 0: 
                    file = MIMEBase('application','octet-stream')
                    file.set_payload(open(file_data[0],'rb').read())
                    encoders.encode_base64(file)
                    file.add_header('Content-Disposition', 'attachment', filename= os.path.basename(file_data[0]))
                    msg.attach(file)
                else :
                    pass
                    
                msg.attach(text)
                server.sendmail(sender_mail,i,msg.as_string())

            server.close()
            print("Sent")
            return None




        def file_read():
            
            if len(file_data) == 0 :
                file_data.append(askopenfilename())
            else :
                file_data[0] = (askopenfilename())
            return None

         #select csv

        def csv_select():
            csv = askopenfilename()
            df = pd.read_csv(csv)
            lis = df["email"].tolist()
            for i in lis :
                mailing_list.append(i)
            return None




        # Main Loop


        window.title("Mail")
        window.geometry("1000x800")


        default_email = StringVar()
        default_subject = StringVar()


        default_email.set(sender_mail)
        default_subject.set("Enter Subject Here")



        #recieve mail

        Label(window,text="Enter email",font=("Comic Sans MS",15,"bold")).pack(pady=10)
        e1 = Entry(window,width=60,textvariable=default_email,font=("Arial",12,"bold"))
        e1.pack()

       

        i2 = Button(window,command=csv_select,text="Pick email List (set col = email)",font=("Comic Sans MS",10,"bold"),bg="#00eb05",width=50)
        i2.pack()

        label_err = Label(window,text = " ")
        label_err.pack()

        #mailnumber

        Label(window,text="Enter Number of mails",font=("Comic Sans MS",15,"bold")).pack()
        sp = Spinbox(window,from_=1,to=10,width=30,font=("Arial",12,"bold"))
        sp.pack()

        #subjectBox

        Label(window,text="Enter Subject",font=("Comic Sans MS",15,"bold")).pack()
        s1 = Entry(window,width=60,textvariable=default_subject,font=("Arial",12,"bold"))
        s1.pack()

        #TextBox

        Label(window,text="Enter content",font=("Comic Sans MS",15,"bold")).pack()
        t1= Text(window,height=25,width=120,fg="#1a53ff",bg="#e6ffff",font=("Arial",12,"bold"))
        t1.pack()

        #file


        i1 = Button(window,text="Pick file",command=file_read,font=("Comic Sans MS",10,"bold"),bg="#00eb05",width=20)
        i1.pack(side = "right")


        #button Funtion

        def looper():
            for i in range(int(sp.get())):
                send_mail()

        text1 = Button(window,text="Send Now!!!",width=50,bg="#60eb15",command=looper,font=("Comic Sans MS",20,"bold")).pack()

        window.mainloop()

        return None
    
"""
main = Tk()
email1 = "mailer.service.public@gmail.com"
passwd = "ozlhpygpbuzubkom"
m = mail_send(main,email1,passwd)
butt1 = Button(main,text = "press here",command=m.send_mails)
butt1.pack()
main.mainloop()

"""