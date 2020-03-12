lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

listanew = list(set(lista))

for x in listanew:
    for y in listb:
        if (x == y):
            print (x)