#Introduction to Function-----------
'''
Kinds of Function :
1 : Library Function (It has created Exam : print(),input() etc and
2 : User Defined Function ()
'''
def add(x,y):
    sum = x+y
    print('Add : ',sum)
def addition(x,y,z):
    sum = x+y+z
    print('Addition :',sum)
def sub(x,y):
    sum = x+y
    print('Submition : ',sum)
def mult(x,y):
    sum = x*y
    print('Multi : ',sum)
def divi(x,y):
    sum = x/y
    print('Divition : ',sum)
def massage():
    print('No parameter')


add(10,20)

addition(10,20,30)
sub(40,10)

mult(10,5)

divi(40,10)

massage()

#Returning Value from function--------
def add(x,y):
    sum = x+y
    return sum

def abb(x,y):
    if x>y:
        return x
    else:
        return y

def subm(x,y):
    sum = x - y
    return sum

def mult(x,y):
    sum = x*y
    return sum

def divi(x,y):
    sum = x/y
    return sum

def large(x,y):
    if x>y :
        return x
    else:
        return y

result = add(10,20)
print('Result :',result)

submition = subm(40,30)
print('Submition :',submition)

oppo = abb(40,52)
print('oppo :',oppo)

multivition  = mult(10,10)
print('multivition :',multivition)

divition = divi(40,4)
print('Divition :',divition)

print('Large Number : ',large(100,200))


