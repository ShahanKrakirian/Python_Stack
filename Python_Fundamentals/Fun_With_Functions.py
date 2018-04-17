#---------------------------
#Odd/Even

# def odd_even():
#     for i in range(1,2001):
#         # Even 
#         if i % 2 == 0: 
#             print "Number is:", i, "This is an even number."
#         else: 
#             print "Number is:", i, "This is an odd number."

# odd_even()

#---------------------------
#Multiply

def multiply(my_list, number):
    return list(map((lambda x: x*number), my_list))

# print multiply([1,2,3,4,5],2)
# Gives [2,4,6,8,10]

#Hacker Challenge

def layered_multiples(my_list, number):
    working_list = multiply(my_list, number)
    final_list = []
    for i in range(0, len(working_list)):
        print working_list
        print "Working with the value:", working_list[i]
        current_list = []
        for j in range(0, working_list[i]):
            current_list.append(1)
        print "Adding this list:", current_list, "to:", final_list
        final_list.append(current_list)
    return final_list

print(layered_multiples([1,2,3],2))
