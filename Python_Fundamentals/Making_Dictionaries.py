#Making Dictionaries 

#Assuming equal size lists.
# def making_dictionaries(list_1, list_2):
#     my_dict = {}
#     for i in range(0, len(list_1)):
#         my_dict[list_1[i]] = list_2[i]
#     print my_dict

# making_dictionaries(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"],["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])

#Lists of potentially different sizes. 
def making_dictionaries(list_1, list_2):
    my_dict = {}
    if len(list_1) >= len(list_2):
        for i in range(0, len(list_2)):
            my_dict[list_1[i]] = list_2[i]
    else:
        for i in range(0, len(list_1)):
            my_dict[list_2[i]] = list_1[i]
    print my_dict

making_dictionaries(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"],["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas",'lion'])