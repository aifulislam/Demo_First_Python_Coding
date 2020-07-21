#Magic methods---------
#__init__(self,name,color):
#__eq__(self, other):
#__str__(self):

class Bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color
    def __str__(self):
        return (f"Name : {self.name},Color : {self.color}")
    def display(self):
        print(f"Name : {self.name},Color : {self.color}")

Bike1 = Bike("Yamaha R15","Blue")
Bike2 = Bike("Yamaha RFZ","Red")
print(Bike1)
print(Bike2)
print(Bike1 == Bike2)

