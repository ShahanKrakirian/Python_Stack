#Find_Characters 

def find_characters(word_list, character):
    new_list = []
    for i in range(0, len(word_list)):
        if word_list[i].find(character) != -1: 
            new_list.append(word_list[i])
    print new_list

find_characters(['dude', 'hey', 'you', 'are', 'cool'], 'u')