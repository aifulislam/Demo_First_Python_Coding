#Introducing and Constructor Methods-----------
class Phone:
    Brand = ""
    Prise = ""
    Color = ""
    #Constructor Methods-----
    def __init__(self,Brand,Prise,Color):
        self.Brand = Brand
        self.Prise = Prise
        self.Color = Color

    def display(self):
        print(f"Brand : {self.Brand},Prise : {self.Prise},Color : {self.Color}")

Apple = Phone("Apple",50000,"Golden")
Apple.display()

Samsang = Phone("Samsang",40000,"Golden Rose")
Samsang.display()

Xiomi = Phone("Xiomi",30000,"Orange")
Samsang.display()

#Introducing and Constructor Methods-----------
class Motorbyke:
    Model = ""
    Prise = ""
    CC = ""
    #Constructor------
    def __init__(self,Model,Prise,CC):
        self.Model = Model
        self.Prise = Prise
        self.CC = CC

    def display(self):
        print(f"Model : {self.Model},Prise : {self.Prise},CC :{self.CC}")

Hero = Motorbyke("w3n4bb",150000,150)
Hero.display()

Yhama = Motorbyke("B3437vvi","200000","150+")
Yhama.display()

TT = Motorbyke("djf3i3o9",100000,125)
TT.display()




