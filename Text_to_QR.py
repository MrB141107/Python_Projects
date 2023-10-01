import qrcode
print(f"Enter the text that you want to convert to QRcode : ")
text = str(input(""))
img = qrcode.make(text)
img.save('qrcode.jpg')
print("Your qrcode is save as 'qrcode.jpg'")
