# Bike

class Bike(object):
    #Set attributes
    def __init__(self, price, max_speed):

        self.price = price 
        self.max_speed = max_speed
        self.miles = 0

    #Shows price, max_speed, and miles
    def displayInfo(self):
        print "Price:", self.price 
        print "Max_Speed:", self.max_speed
        print "Miles:", self.miles
        return self

    #Increase miles by 10
    def ride(self):
        print "Currently at:", self.miles
        self.miles += 10
        print "Riding ten miles."
        return self

    #Unride the bike?
    def reverse(self):
        print "Currently at:", self.miles
        if self.miles > 0:
            self.miles -= 5
        print "Reversing five miles."
        return self
    
# fixie = Bike(200, 15)
# specialized = Bike(5000000, 25)
# critical = Bike(500, 20)

# fixie.ride().ride().ride().reverse()
# fixie.displayInfo()
# specialized.ride().ride().reverse().reverse
# specialized.displayInfo()
# critical.reverse().reverse().reverse()
# critical.displayInfo()



bike1 = Bike(29837498237, 5)
print bike1.ride().displayInfo().ride()