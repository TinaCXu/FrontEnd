# str = input("Please input a long string: ")

# str = "Tina Love Bobby"
# new_str = str.split(" ")

# output_list = []

# i = len(new_str) -1
# while i >= 0:
#     output_list.append(new_str[i])
#     i -= 1

# a = [0,1,2]
# print(output_list)
# print(" ".join(output_list[i] for i in a))

def reverse_string():
    str = input("Please input a long string: ")
    #split the string into single word
    new_str = str.split(" ") 
    #reverse the list
    output_list = [] 
    i = len(new_str) -1
    while i >= 0:
        output_list.append(new_str[i])
        i -= 1
    #prepare list for generator expression
    i = 0
    a = []
    while i < len(output_list):
        a.append(i)
        i += 1
    #output
    print(" ".join(output_list[i] for i in a))

reverse_string()


# output_list=["Bobby","Love","Tina"]
# i = 0
# a = []
# while i < len(output_list):
    # a.append(i)
    # i += 1
# print(a)

