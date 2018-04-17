# Store 

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products 
        self.location = location
        self.owner = owner 

    def add_product(self, new_product):
        print "Adding", new_product, "to the product list."
        self.products.append(new_product)
        return self 

    def remove_product(self, remove_name):
        print "Removing", remove_name, "from the product list."
        self.products.remove(remove_name)
        return self 

    def inventory(self):
        print "Products:", self.products
        print "Location:", self.location
        print "Owner:", self.owner 

rei = Store(['basketball', 'soccer', 'climbing shoes', 'rope', 'road bike'], 'Burbank', 'All of us')
rei.remove_product('road bike').add_product('climbing location book').inventory()