#---------------------------------
# Find and Replace 

# words = "It's Thanksgiving day. It's my birthday, too!"
# print words.find('day')
# new_string = words.replace('day', 'month')

#---------------------------------
# Min and Max 

# def min_and_max(given_list):
#     print "Min:", min(given_list)
#     print "Max:", max(given_list)

#---------------------------------
# First and Last 

# def first_and_last(given_list):
#     first = given_list[0]
#     last = given_list[len(given_list)-1]
#     new_list = [first,last]
#     print "First:", first, "Last:", last
#     print new_list

#---------------------------------
# New List 

def new_list(given_list):
    given_list.sort()
    final_array = []
    #Create first half, append to final array.
    first_half = given_list[0:len(given_list)/2]
    final_array.append(first_half)

    #Add in rest to final array. 
    for i in range(len(given_list)/2, len(given_list)):
        final_array.append(given_list[i])
    print final_array

new_list([1,2,3,4,5,6,7,8,9,10])