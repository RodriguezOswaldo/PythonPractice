
class Parent:

    def __init__(self, last_name, eye_color):
        print('Parent Constructor was Called')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print('Last name: ' + self.last_name)
        print('Eye Color: ' + self.eye_color)

class Child(Parent):

    def __init__(self, last_name, eye_color, number_of_toys ):
        print('Child Constructor was Called')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print('Last name: ' + self.last_name)
        print('Eye Color: ' + self.eye_color)
        print('No. Of Toys: ' + str(self.number_of_toys))


Oswaldo_Rdrgz = Parent("Rodriguez", "Brown")
Arthur_Rdrgz = Child('Rodriguez', 'Brown', 23)
Arthur_Rdrgz.show_info()
# print(Oswaldo_Rdrgz.last_name)
# print(Arthur_Rdrgz.number_of_toys)
# print(Arthur_Rdrgz.eye_color)