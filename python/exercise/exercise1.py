#User Input
name = input("Give your name: ")
age = input("Give your age: ")
times = input("How many times printed out: ")
# trun the age string into int
age = int(age)
# calculate
laps = 100 - age
year = 2020 + laps
#Output
for _ in range(int(times)):
    print("Your name is "+ name)
    print("You will turn 100 years old in ", year)