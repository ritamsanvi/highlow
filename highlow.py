import random
print('high low game')
number= random.randint(1,9)
chances=0
print("Guess a number betweeen 1 and 9")

while chances < 5:
    guess= int(input("Enter your guess:"))

    if guess == number:
        print("you have won")
        break

    elif guess < number:
        print('your number was low')

    else :
        print("Your number was high")

    chances==1

    if not chances < 5 :
        print("you lost")
