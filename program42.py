#Types Of Inheritance--------
# 1- Hierarchical Inheritance
# 2- Multi-Level Inheritance
class A:
    def display1(self):
        print("I am inside A class")

class B(A):
    def display2(self):
        print("I am inside B class")

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")

ob1 = C()
ob1.display3()

#Types Of Inheritance--------
# 3- Multiple Inheritance

class A:
    def display(self):
        print("Is is A class")
class B:
    def display(self):
        print("It is B class")
# 3- Multiple Inheritance
class C(B,A):
        pass

ob1 = C()
ob1.display()


#Types Of Inheritance--------
# 1- Hierarchical Inheritance
# 2- Multi-Level Inheritance
# 3- Multiple Inheritance

class A:
    def display(self):
        print("It is A class")
#Multi-Level----
class B:
    def display(self):
        print("It is B class")
#Multiple----
class C(B,A):
    pass

ob1 = C()
ob1.display()
