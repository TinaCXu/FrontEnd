import random
standard = random.randint(1,9)
number = input("Please guess the random number: ")
number = int(number)
i = 1
while number != standard:
    if (number < standard):
        print ("too low")
        i += 1
    if (number > standard):
        print ("too high")
        i += 1
    number = input("Please guess the random number again: ")
    number = int(number)
#if (number == standard): (jump out the while loop only when number equals to standard)
print ("Congratulation! You have guessed ",i, " times!")
