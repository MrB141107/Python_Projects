from random import randint
print("Welcome to Guessing the Number game...")
print("I'm thinking of a number between 1 to 100...")

chances = 0
if chances == 0 :
    d_level = input("\nSelect the difficulty level (easy/medium/hard) : ").lower()
    if str(d_level) == "easy":  
        chances += 10 
        print("You will get 10 chances to guess the number..")
    if str(d_level) == "medium" : 
        chances += 7
        print("You will get 7 chances to guess the number..")
    if str(d_level) == "hard":
        chances += 5
        print("You will get 5 chances to guess the number..")

number = randint(1,100)
while chances >= 0:
    answer = int(input("\nMake a guess :"))
    if chances == 0 : 
        print("Oops your chances over....Game over!!")
        chances=-1
    if answer > 100 or answer < 1: 
        print("Guess the number between 1 to 100..")
    elif answer > number: print("Guess a smaller number..")
    elif answer < number : print("Guess a larger number..")
    elif answer == number : 
        print("Correct answer!!...Booyaahhh....")
        chances=-1
    chances -=1