#Type List

def type_list(given_list):
    my_sum = 0
    string = ''
    type_counter = 0
    for i in range(0, len(given_list)):
        if isinstance(given_list[i], str):
            string += given_list[i] + ' '
        elif isinstance(given_list[i], float) or isinstance(given_list[i], int):
            my_sum += given_list[i]

    if string != '':
        type_counter += 1
    if my_sum != 0:
        type_counter +=1

    if type_counter > 1:
        print "The list you entered has a salad of data types!"
        print "Sum:", my_sum
        print "String:", string
    elif type_counter == 1:
        if my_sum != 0:
            print "You gave me some numbers."
            print "Sum:", my_sum
        else:
            print "You gave me some strings."
            print "String:", string
    else:
        print "You're not cooperating."

type_list([1, 'two', 3, 4])
