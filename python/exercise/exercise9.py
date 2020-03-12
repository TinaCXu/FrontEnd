import random
standard = random.randint(1,9)
number = input("Please guess the random number: ")
number = int(number)
i = 1
if (number < standard):
    print ("too low")
    i += 1
number = input("Please guess the random number again: ")
number = int(number)
if (number > standard):
    print ("too high")
    i += 1
number = input("Please guess the random number again: ")
number = int(number)
if (number == standard):
    print ("Congratulation! You have guessed ",i, " times!")
