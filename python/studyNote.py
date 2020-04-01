a = 21
b = 10
c = 0
print (a ** c)
print (a // b)
print (a % b)
print (a / b)

#Python logical operators
print (a and b)
print (c and b)
print (a or b)
print (c or b)
print (not(c or b))

i = 2
j = 2
print(i % j)
print(i % j == 0)
print (not(i % j))

#If Loop
var = 100 
if ( var  == 100 ): 
    print ("变量 var 的值为100")
else:
    print ("Good bye!")

#range & len
fruits = ['banana', 'apple',  'mango']
print (len(fruits)) #3
print (range(len(fruits))) #range(0,3)
range(3)
range(0,1,2)

#Python3 iterators and generators
list=[1,2,3,4]
it = iter(list)
print(next(it)) #next(iterator[, default]) #out put =1
print(next(it)) #function 2 times, iter mannually, using for loop

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)