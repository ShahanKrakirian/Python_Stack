# Animal 

# Animal Class

class Animal(object):

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self): 
        print "Walking! I'm tired, minus 1 health."
        self.health -= 1
        return self 
    
    def run(self):
        print "Running! I always fall for the ball trick. Minus 5 health."
        self.health -= 5
        return self 
    
    def display_health(self):
        print "Health:", self.health
        return self 

# Jojo = Animal('Jojo', 100)
# Jojo.walk().walk().walk().run().run().display_health() #Works 

# Dog Class 

class Dog(Animal):
    
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        print "Oooh yeah, that's the spot! +5 Health!"
        self.health += 5
        return self

# Jojo = Dog('Jojo', 100)
# print Jojo.health
# Jojo.walk().walk().walk().run().run().pet().display_health() #Works 

class Dragon(Animal):

    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170

    def fly(self):
        print "I'm scared of heights... why am I a dragon... Minus 10 health."
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
        return self
   

# dragon = Dragon("George", 100)
# dragon.display_health() #Works 

new_animal = Animal('dude', 200)
# new_animal.fly() #Doesn't work, as expected 
# new_animal.pet() #Doesn't work, as expected 
new_animal.display_health() #Doesn't include "I am a dragon"

Jojo = Dog("Jojo", 100)
# Jojo.fly() #Doesn't work, as expected