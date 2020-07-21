#A practical example of inheritance-------
class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method of shape class : ")

class Triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("I am area method of Triangle class : ",area)

class Rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("I am area method of Rectangle class : ",area)

class Addiction(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Addiction : ",area)
t1 = Triangle(10,20)
t1.area()

t2 = Rectangle(10,20)
t2.area()

t3 = Addiction(100,200)
t3.area()

#A practical example of inheritance-------
class shape:
    def __init__(self,dim1,dim2):
        self.dim1 =  dim1
        self.dim2 =  dim2

    def area(self):
        print("It is a Shape class : ")

class Triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle : ",area)

class Rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle : ",area)

class Addiction(shape):
    def area(self):
        area = self.dim1 + self.dim2
        print("Addiction : ",area)

class Subtrauction(shape):
    def area(self):
        area = self.dim1 - self.dim2
        print("Subtruction : ",area)

class Multification(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Multification : ",area)

class Division(shape):
    def area(self):
        area = self.dim1 / self.dim2
        print("Division : ",area)

t1 = Triangle(10,20)
t1.area()

r1 = Rectangle(10,20)
r1.area()

add1 = Addiction(100,200)
add1.area()

sub = Subtrauction(200,100)
sub.area()

mul = Multification(10,10)
mul.area()

div = Division(200,10)
div.area()


