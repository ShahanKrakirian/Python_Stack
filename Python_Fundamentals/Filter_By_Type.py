#Filter By Type 

def filter_by_type(value):
    if isinstance(value, int):
        if value >= 100:
            print "That's a big number!"
        else: 
            print "That's a small number"
    elif isinstance(value, str):
        if len(value) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    elif isinstance(value, list):
        if len(value) >= 10:
            print "Big list!"
        else: 
            print "Short list."

filter_by_type(['name','address','phone number','social security number'])