"""
Author: Ninja-06
Date: 08-10-2023
Description: This script sends message/image on whatsapp.
Used pywhatkit library to automate messsage sending process.

"""
import pywhatkit as wthelp

print("Let's automate message/image sending on whatsapp !!")
print("Make sure that your QR code is scanned on whatsapp web so that script can send message/image from your behalf")

class automateWhatsapp:

    def __init__(self):

        """
        Takes a contact list to whom the sender wants to 
        send messages/images.  

        """      
        flag = True
        self.contact_list = []
        print('Enter contact number: ')

        while flag:
            contact_num = input()
            verify = input("Please verify if the contact number is correct Y/N : ")

            if (verify == 'Y'):
                self.contact_list.append(contact_num)
                flag = input('Do you want to add more contact numbers ? Y/N: ')
                flag = True if flag == 'Y' else False
            else:   
                print('enter contact number again.')
      
    def send_message(self):
        
        """
        Takes a message input from the sender and sends the message 
        to the contacts in the contact list.
        
        """
        message = input("Enter message you want to send..")
        for contact_num in self.contact_list:
            if len(message) == 0:
                message = input("Oops! you entered empty message please re-enter message")
            wthelp.sendwhatmsg_instantly(phone_no=contact_num, message=message, wait_time=12,tab_close=True)
            print(f'successfully sent message to contact number {contact_num}')

    def send_image(self):

        """
        Takes a image path as  input from the sender and sends the image 
        to the contacts in the contact list.
        """
        image_path = input("Enter the image path..")
        for contact_num in self.contact_list:
            wthelp.sendwhats_image(receiver=contact_num, img_path=image_path, wait_time=12, tab_close=True)
            print(f'successfully sent images to contact number {contact_num}')

if __name__ == '__main__':

    print("Enter 1 to send message to the user")
    print("Enter 2 to send image to the user")
    print("Enter 3 to send image and message to the user")
    user_input = int(input())

    if user_input > 3 or user_input <= 0:
       print('invalid option')
       exit()

    w = automateWhatsapp()
    if user_input == 1 or user_input == 3:
        w.send_message()  
    if user_input == 2 or user_input == 3:
        w.send_image() 