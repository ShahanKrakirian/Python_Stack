# Car 

class Car(object):
    #Set attributes.
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel 
        self.mileage = mileage

        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        
    def display_all(self):
        print self
        print "Price:", self.price
        print "Speed:", self.speed 
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax


car_1 = Car(12000, 70, 'half', 1000000)
car_2 = Car(8000, 50, 'three-quarters', 150000)
car_3 = Car(50000, 80, 'empty', 2000)
car_4 = Car(25000, 75, 'quarter', 20000)
car_5 = Car(5000, 30, 'full', 200000)
car_6 = Car(2000, 50, 'almost empty', 20000)

car_1.display_all()
car_2.display_all()
car_3.display_all()
car_4.display_all()
car_5.display_all()
car_6.display_all()

