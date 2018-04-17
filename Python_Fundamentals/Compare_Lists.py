#Compare Lists 

def compare_lists(list_1, list_2):
    counter = 0
    for i in range(0, len(list_1)):
        if list_1[i] == list_2[i]:
            counter += 1
    if counter == len(list_1):
        print "The lists are the same."
    else: 
        print "The lists are not the same."

