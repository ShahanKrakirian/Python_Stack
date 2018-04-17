# Dictionary in, Tuple out

my_dict = {
    "Armenia": "Three Months",
    "Australia": "Ten Months",
    "Brazil": "One Month",
    "Peru": "One Month",
    "Lebanon": "One Month"
}

def return_tuple(my_dict):
    final_list = []
    for keys,values in my_dict.iteritems():
        current_tuple = ()
        current_tuple += (keys, values)
        final_list.append(current_tuple)
    print final_list

return_tuple(my_dict)