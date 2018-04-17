#Making and Reading from Dictionaries

my_dictionary = {
    "Name": "Shahan",
    "Age": 26,
    "Birthplace": "United States",
    "Language": "Armenian"
}

def dictionary_information(my_dict):
    for key,value in my_dictionary.iteritems():
        if isinstance(value, int):
            value = str(value)
        print key + ": " + value

dictionary_information(my_dictionary)