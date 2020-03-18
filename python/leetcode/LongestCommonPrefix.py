list = ["flower","flow","flight"]
#loop the strings in list
var = 0
idx = 0
choose = []
while list[var][idx] == list[var+1][idx] and var <= len(list)-2:
    var += 1
    if var == len(list)-1:
        choose.append((list[var][idx]))
        idx += 1
        var = 0

Output = ''.join(choose)
print(Output)
    
