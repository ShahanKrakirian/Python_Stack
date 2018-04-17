#Stars 

#Part I 

# def draw_stars(numbers):
#     for i in range(0, len(numbers)):
#         print "*" * numbers[i]

# draw_stars([1,2,3,4,5])

#Part II

def draw_stars(stuff):
    for i in range(0, len(stuff)):
        if isinstance(stuff[i], int):
            print "*" * stuff[i]
        elif isinstance(stuff[i], str):
            print stuff[i][0].lower()*len(stuff[i])
        else:
            print "Wrong type, man."

draw_stars([1,2,3,'four', 'tenten'])