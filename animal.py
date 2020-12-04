class Animal(object):
    """Makes Cute Animal"""
    is_alive = True
    health = "good"

    def __init__(self, name, age, has_hair):
        self.name = name
        self.age = age
        self.has_hair = has_hair

    def description(self):
        print("Animal name: " + self.name)
        print(self.age)
        print("Is he hairy? : " + str(self.has_hair))


hippo = Animal("Tommy", 34, False)
print(hippo.health)
sloth = Animal("Timmy", 3, True)
ocelot = Animal("Tammy", 6, True)
hippo.description()
