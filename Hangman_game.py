#Creating Hangman game
import random
word_list=[ "table", "river", "shadow", "clock", "window"]
chosen_word=random.choice(word_list)
display=[]
for let in chosen_word:
    display+="_"
print(display)

lives=6
game_over=False
while not game_over:
    guess=input("Enter your guess: ")
    for position in range (len(chosen_word)):
        letter= chosen_word[position]
        if guess==letter:
            display[position]=letter
    print(display)

    if guess not in chosen_word:
        lives-=1
        print(f"{guess} is not in word.\nYou have {lives} lives left")

        if lives==0:
            game_over=True
            print(f"You lost.\nThe word is {chosen_word}")

    if "_" not in display:
        game_over=True
        print("You win!")
