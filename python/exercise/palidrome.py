s = "aba"
s = "abccba"
s = "abacaba"
s = "acba"
#decide if  s is a palidrome.
is_palidrome = True #flag = False  or True

for i in range((len(s)//2)):
    if (s[i] != s[-1 - i]):
    # if (s[i] == s[len(s)-1-i]
        #n += 1    
        is_palidrome = False
        break 
if (is_palidrome):        
    print("s is a palidrome.")