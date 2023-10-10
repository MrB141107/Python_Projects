import random
import art
import words

print(art.logo)
print('''
  O   
 /|\ 
 / \ ''')
print("Welcome to the game, savior!\nGuess the word correctly to save my life!🙏")
chosen_word = random.choice(words.word_list)
lives = 6
heart = "💙"
print(f"Total lives {heart * lives}")
display = list(range(len(chosen_word)))
for n in range(len(chosen_word)):
    display[n] = "_"
print(f"Hint: The word is {len(display)} letters long.")
print(art.stages[lives])
while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"{guess} already guessed.")
    else:
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                display[n] = chosen_word[n]
        if guess in chosen_word:
            print("Correct guess!😁")
            if lives != 6:
                lives += 1
                print("Life increased!😁")
                print(heart * lives)
            else:
                print("Already maximum lives!")
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} not in word. Life lost!😟")
            print(heart * lives)
        converted = ""
        for n in range(len(display)):
            converted = converted + display[n]
        print(converted)
        print(art.stages[lives])
        if lives == 0:
            print("You Lose!😭")
            print(f"{chosen_word} is the correct word!")
            exit(0)
print("Yay! Thanks you saved my life!😁\nYou Won!😎")
