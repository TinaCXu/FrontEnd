#Use Input
number = input("Give your number: ")
#turn it into int
number = int(number)
#odd or even
if (number % 2 == 0):
    print("It is an even number.")
else:
    print("It is an odd number.")
if (number % 4 == 0):
    print("it is the multipe of 4")
#
num = input("Please enter number1: ")
check = input("Please enter number2: ")
num = int(num)
check = int(check)
if (check % num == 0):
    print("number2 could devide evenly into number1.")
else:
    print("number2 could not devide evenly into number1.")