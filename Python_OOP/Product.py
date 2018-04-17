#Product 

class Product(object):
    def __init__(self, price, item_name, weight, brand, status = 'for sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status 

    def sell(self):
        self.status = 'sold'
        return self
    
    def add_tax(self, tax):
        print "Adding Sales Tax"
        if tax > 0 and tax < 1: 
            self.price = self.price + (self.price * tax)
        else: 
            print "Input tax in decimal form."
        return self

    def return_item(self, reason):
        if reason == 'defective':
            self.price = 0
            self.status = 'defective'
        if reason == 'like new':
            self.status = 'for sale'
        if reason == 'opened':
            self.status = 'used'
            self.price = self.price * .80
        return self 

    def display_info(self):
        print "Item Name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status 

stuff = Product(100, 'Speakers', 3, 'Bose')
stuff.add_tax(.10).sell().return_item('like new').display_info()
