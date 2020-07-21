#Magic methods---------
#__init__(self,name,color):
#__eq__(self, other):
#__str__(self):

class Phone:
    def __init__(self,name,color,prise):
        self.name = name
        self.color = color
        self.prise = prise

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color and self.prise == other.prise

    def __str__(self):
        return (f"Name : {self.name},Color : {self.color},Prise : {self.prise}")

    def display(self):
        print(f"Name : {self.name},Color : {self.color},Prise : {self.prise}")


Phone1 = Phone("Apple","White",50000)
Phone2 = Phone("Samsang","Black","40000")
Phone3 = Phone("Xiomi","Red",'30000')

print(Phone1)
print(Phone2)
print(Phone3)
print(Phone1 == Phone2)