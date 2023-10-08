#Import necessary tkinter modules
import tkinter as tk
import tkinter.font as tkfont
from tkinter import *

#Create a tkinter root window
root = tk.Tk()

root.title("Text Encryptor-Decryptor")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

#Create a canvas to add widgets
canvas = tk.Canvas(root,height = 500, width=400, bg="LightBlue")
canvas.pack()
bold_font = tkfont.Font(family="Helvetica",size=12,weight="bold")

#Create a label widget for user instructions
label1 = tk.Label(root,text= "Enter the Text",width=20,bg="LightBlue")
label1.config(font=bold_font)
canvas.create_window(200,100,window=label1)

#Create an entry widget for user input
user_text = tk.Entry(root)
canvas.create_window(200,150,window=user_text)

#Create a label for selecting the operation
label2=tk.Label(root,text="Choose an Operation",width=25,bg="LightBlue")
label2.config(font=bold_font)
canvas.create_window(200,200,window=label2)

#tkinter IntVar to store selected operation choice
v = tk.IntVar()

#Function to handle the choice of encryption or decryption
def choice():
    x = v.get()
    if(x==1):
        encryption()
    elif(x==2):
        decryption()

#Create radio buttons
label3=tk.Radiobutton(root, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="light yellow")
label3.config(font=bold_font)
canvas.create_window(100,250,window=label3)
label4=tk.Radiobutton(root, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="light yellow")
label4.config(font=bold_font)
canvas.create_window(300,250,window=label4)

def encryption():
    plain_text = user_text.get() #get input from user
    cipher_text = ""
    key = 3 #set encryption key

    #Loop through each character in plain text
    for i in range(len(plain_text)):
        letter = plain_text[i]
        if(letter.isupper()):

            #Encrypt uppercase letters using the key and modulo 26 to wrap around the alphabet
            cipher_text+=chr((ord(letter)+key-65)%26+65)
        else:
            #Encrypt lowercase letters using the key and modulo 26 to wrap around the alphabet
            cipher_text+=chr((ord(letter)+key-97)%26+97)

    #Display the cipher text
    label5 =tk.Label(root,text=cipher_text,width=20,bg="light yellow")
    label5.config(font=bold_font)
    canvas.create_window(200,350,window=label5)

def decryption():
    cipher_text = user_text.get() #get input from user
    plain_text = ""
    key = 3 #set encryption key

    #Loop through each character in plain text
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
        if(letter.isupper()):

            #Decrypt uppercase letters using the key and modulo 26 to wrap around the alphabet
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
            #Decrypt lowercase letters using the key and modulo 26 to wrap around the alphabet
            plain_text+=chr((ord(letter)-key-97)%26+97)
            
    #Display the plain text
    label6 =tk.Label(root,text=plain_text,width=20,bg="light yellow")
    label6.config(font=bold_font)
    canvas.create_window(200,350,window=label6)

#Create a label to display the converted text
label7 =tk.Label(root,text="Converted Text ",width=20,bg="LightBlue")
label7.config(font=bold_font)
canvas.create_window(200,300,window=label7)

#Start main event loop
root.mainloop()
