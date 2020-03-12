print ("hello tina")
number = input("Please enter your number: ")
number = int(number)
b = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = []
for i in range(len(a)):
    if (a[i] < number):
        print("less than number: ",a[i])
        b.append(a[i])
print (b)

for i in range(len(a)):
    if (a[i] < number):
        print("less than entered number: ",a[i])
        c.append(a[i])
print (c) 