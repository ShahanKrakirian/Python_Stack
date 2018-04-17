#-----------------------------
#Multiples

# #Part I 
# for i in range(0,1001,2):
#     print i

# #Part II
# for i in range(5,1000001):
#     if i % 5 == 0:
#         print i

#-----------------------------
#Sum List 

# def sum_list(given_list):
#     sum = 0
#     for i in range(0, len(given_list)):
#         sum += given_list[i]
#     print sum

#-----------------------------
#Average List 

def average_list(given_list):
    sum = 0
    for i in range(0, len(given_list)):
        sum += given_list[i]
    print sum/len(given_list)

