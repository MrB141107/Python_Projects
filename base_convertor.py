import os
import time
def decimal_to_binary(n):
    p=bin=0;
    while(n>0):
        rem=int(n%2)
        bin+=rem*int(10**p)
        p+=1
        n=int(n/2)
    return bin

def binary_to_decimal(n):
    p=dec=0
    while(n>0):
        rem=int(n%10)
        dec+=rem*int(2**p)
        p+=1
        n=int(n/10)
    return dec

def decimal_to_octal(n):
    p=oct=0
    while(n>0):
        rem=int(n%8)
        oct+=rem*int(10**p)
        p+=1
        n=int(n/8)
    return oct

def octal_to_decimal(n):
    p=dec=0
    while(n>0):
        rem=int(n%10)
        dec+=rem*int(8**p)
        p+=1
        n=int(n/10)
    return dec

def binary_to_octal(n):
    return decimal_to_octal(binary_to_decimal(n))

def octal_to_binary(n):
    return decimal_to_binary(octal_to_decimal(n))

def hexadecimal_to_decimal(s):
    rev=s[::-1]
    p=dec=rem=0
    for c in rev:
        if(c=="A"):rem=10
        elif(c=="B"):rem=11
        elif(c=="C"):rem=12
        elif(c=="D"):rem=13
        elif(c=="E"):rem=14
        elif(c=="F"):rem=15
        else:
            rem=int(c)
        dec+=rem*int(16**p)
        p+=1
    return dec

def decimal_to_hexadecimal(n):
    h="0123456789ABCDEF"
    hex=""
    while(n>0):
        rem=int(n%16)
        hex+=h[rem]
        n=int(n/16)
    return hex[::-1]

def hexadecimal_to_binary(s):
    return decimal_to_binary(hexadecimal_to_decimal(s))

def binary_to_hexadecimal(n):
    return decimal_to_hexadecimal(binary_to_decimal(n))

def hexadecimal_to_octal(s):
    return decimal_to_octal(hexadecimal_to_decimal(s))

def octal_to_hexadecimal(n):
    return decimal_to_hexadecimal(octal_to_decimal(n))

os.system("cls")
print("WELCOME TO THE BASE CONVERTOR......\n")
time.sleep(0.5)
while(True):
    source=input("Enter source base : ")
    dest=input("Enter destination base : ")
    source=source.lower()
    dest=dest.lower()
    if(source=="decimal" and dest=="binary"):
        s=int(input("Enter a decimal number : "))
        print("Binary number is :",decimal_to_binary(s))
    elif(source=="decimal" and dest=="octal"):
        s=int(input("Enter a decimal number : "))
        print("Octal number is :",decimal_to_octal(s))
    elif(source=="decimal" and dest=="hexadecimal"):
        s=int(input("Enter a decimal number : "))
        print("Hexadecimal number is :",decimal_to_hexadecimal(s))
    elif(source=="binary" and dest=="decimal"):
        s=int(input("Enter a binary number : "))
        print("Decimal number is :",binary_to_decimal(s))
    elif(source=="binary" and dest=="octal"):
        s=int(input("Enter a binary number : "))
        print("Octal number is :",binary_to_octal(s))
    elif(source=="binary" and dest=="hexadecimal"):
        s=int(input("Enter a binary number : "))
        print("Hexadecimal number is :",binary_to_hexadecimal(s))
    elif(source=="octal" and dest=="decimal"):
        s=int(input("Enter a octal number : "))
        print("Decimal number is :",octal_to_decimal(s))
    elif(source=="octal" and dest=="binary"):
        s=int(input("Enter a octal number : "))
        print("Binary number is :",octal_to_binary(s))
    elif(source=="octal" and dest=="hexadecimal"):
        s=int(input("Enter a octal number : "))
        print("Hexadecimal number is :",octal_to_hexadecimal(s))
    elif(source=="hexadecimal" and dest=="decimal"):
        s=input("Enter a hexadecimal number : ")
        print("Decimal number is :",hexadecimal_to_decimal(s))
    elif(source=="hexadecimal" and dest=="binary"):
        s=input("Enter a hexadecimal number : ")
        print("Binary number is :",hexadecimal_to_binary(s))
    elif(source=="hexadecimal" and dest=="octal"):
        s=input("Enter a hexadecimal number : ")
        print("Octal number is :",hexadecimal_to_octal(s))
    print("\n")
    z=input("Would you like to continue? ")
    if(z=="n" or z=="N"):
        print("Bye!!!","Hope to see you again....",sep="\n",end="\n")
        break
    