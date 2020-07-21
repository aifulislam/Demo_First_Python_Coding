#xxargs and xxxargs---------
def students(id,name):
    print(id,name)
students(101,'\nAriful Islam')

#xxargs and xxxargs------------
def student(id,name,gpa):
    print(id,name,gpa)
student(101,'Nazim Uddin',4.50)

#xxargs and xxxargs------------
def students(*details):
    print(details)
students(101,'Ariful Islam',4.50)
#xxargs and xxxargs------------
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)
add(10,20,30,40,50)

#xxargs and xxxargs------------
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print('Sum : ',sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)
add(10,20,30,40,50)

def student(**details):
    print(details)

student(id=101,name='Ariful Islam',gpa='3.88')
student(id=102,name='Nazim Islam',gpa='3.88')
student(id=103,name='Nazim Islam',gpa='3.88')
student(id=104,name='Nazim Islam',gpa='3.88')
student(id=105,name='Nazim Islam',gpa='3.88')







