#Debugging------------
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return ('Sum : ',sum)

print(add(10,20))

#Lambda Functions---------
#lambda  parameter : expression
#(lambda x,y      : x*x + 2*x*y + y*y)
def calculate(a,b):
    return a*a + 2*a*b + b*b

print(calculate(2,3))

print('x,y : ',(lambda x,y : x*x + 2*x*y + y*y)(2,3))
print('a,b : ',(lambda a,b : a*a + 2*a*b + b*b)(4,3))
print('Lambda : ',(lambda a,b : a*a + 2*a*b + b*b)(2,3))

a = ('Lambda : ',(lambda a,b : a*a + 2*a*b + b*b)(2,3))
print(a)

a = (lambda a,b : a*b + 2*a*b +b*b)(2,3)
print("a + b : ",a)
#Lambda a-----
def cube(x):
    return x*x*x
a =(lambda x : x*x*x)(2)
print(a)

#Lambda Cube-----
a = (lambda x : x*x*x)(2)
print(a)

def cube(x):
    return x*x*x
print(2)
c = (lambda x : x*x*x)(2)
print("Cube :",c)

b = (lambda x : x*x*x)(6)
print("Cube : ",b)



