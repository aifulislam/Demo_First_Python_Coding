#Introducing Methods-----------
class Phone:
    Brand = ""
    Prise = ""
    Color = ""
    #Introducting Methods-----
    def set_value(self,Brand,Prise,Color):
        self.Brand = Brand
        self.Prise = Prise
        self.Color = Color

    def display(self):
        print(f"Brand : {self.Brand},Prise : {self.Prise},Color : {self.Color}")

Apple = Phone()
Apple.set_value("Apple",50000,"Golden")
Apple.display()

Samsang = Phone()
Samsang.set_value("Samsang",40000,"Golden Rose")
Samsang.display()

Xiomi = Phone()
Xiomi.set_value("Xiomi",30000,"Orange")
Samsang.display()

#Introducing Methods-----------
class Laptop:
    Brand = ""
    Praise = ""
    Color = ""

    def set_value(self,Brand,Praise,Color):
        self.Brand = Brand
        self.Praise = Praise
        self.Color = Color

    def display(self):
        print(f"Brand : {self.Brand},Prise : {self.Praise},Color :{self.Color}")

Apple  = Laptop()
Apple.set_value("Apple",50000,"Golden")
Apple.display()

Samsang = Laptop()
Samsang.set_value("Samsang",40000,"Orange")
Samsang.display()

HP = Laptop()
HP.set_value("HP",30000,"Black")
HP.display()

#Introducing Methods-----------
class Student:
    Roll = ""
    Class = ""
    GPA = ""
    def set_value(self,Roll,Class,GPA):
        self.Roll = Roll
        self.Class = Class
        self.GPA = GPA
    def disply(self):
        print(f"Roll : {self.Roll},Class : {self.Class},Gpa : {self.GPA}")

Arif = Student()
Arif.set_value(100,"MA",4.50)
Arif.disply()

Tamim = Student()
Tamim.set_value(101,"One",4.20)
Tamim.disply()

Nazim = Student()
Nazim.set_value(102,"MA",4.33)
Nazim.disply()

#Introducing Methods-----------
class Motorbyke:
    Model = ""
    Prise = ""
    CC = ""
    #Introducing Method------
    def set_value(self,Model,Prise,CC):
        self.Model = Model
        self.Prise = Prise
        self.CC = CC

    def display(self):
        print(f"Model : {self.Model},Prise : {self.Prise},CC :{self.CC}")
Hero = Motorbyke()
Hero.set_value("w3n4bb",150000,150)
Hero.display()

Yhama = Motorbyke()
Yhama.set_value("B3437vvi","200000","150+")
Yhama.display()

TT = Motorbyke()
TT.set_value("djf3i3o9",100000,125)
TT.display()


