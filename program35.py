#Introduction to OOP - class and object----
class Student:
    Roll = ""
    Class = ""
    GPA = ""

Arif = Student()
print(isinstance(Arif,Student))
Arif.Roll = '101'
Arif.Class = 'MA'
Arif.GPA = '4.20'
print(f"Roll : {Arif.Roll},Class : {Arif.Class},GPA : {Arif.GPA}")

Tamim = Student()
Tamim.Roll = '102'
Tamim.Class = 'One'
Tamim.GPA = 'None'
print(f"Roll : {Tamim.Roll},Class : {Tamim.Class},GPA : {Tamim.GPA}")

Nazim = Student()
Nazim.Roll = "103"
Nazim.Class = "MA"
Nazim.GPA = "4.56"
print(f"Roll : {Nazim.Roll},Class : {Nazim.Class},GPA : {Nazim.GPA}")

#Introduction to OOP - class and object----
class Student:
    Roll = ""
    Class = ""
    GPA = ""

Arif = Student()
print(isinstance(Arif,Student))
Arif.Roll = "100"
Arif.Class = "MA"
Arif.GPA = "4.50"
print(f"Roll : {Arif.Roll},Class : {Arif.Class},Gpa : {Arif.GPA}")

Tamim = Student()
Tamim.Roll = "101"
Tamim.Class = "One"
Tamim.GPA = "None"
print(f"Rool : {Tamim.Roll},Class : {Tamim.Class},Gpa : {Tamim.GPA}")

Nazim = Student()
Nazim.Roll = "102"
Nazim.Class = "MA"
Nazim.GPA = "4.33"
print(f"Rool : {Nazim.Roll},Class : {Nazim.Class},Gpa : {Nazim.GPA}")

#Introduction to OOP - class and object----
class Laptop:
    Brand = ""
    Praise = ""
    Color = ""

Apple  = Laptop()
print(isinstance(Apple,Laptop))
Apple.Brand = "Apple"
Apple.Praise = "100000"
Apple.Color = "Golden"
print(f"Brand : {Apple.Brand},Prise : {Apple.Praise},Color :{Apple.Color}")

Samsang = Laptop()
Samsang.Brand = "Samsang"
Samsang.Praise = "60000"
Samsang.Color = "Black"
print(f"Brand : {Samsang.Brand},Prise : {Samsang.Praise},Color : {Samsang.Color}")

HP = Laptop()
HP.Brand = "HP"
HP.Praise = "60000"
HP.Color = "Black"
print(f"Brand : {HP.Brand},Prise : {HP.Praise},Color : {HP.Color}")


