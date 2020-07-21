#map function-----
def squre(x):
    return x*x

num=[1,2,3,4,5,6,7]
result=list(map(squre,num))
print("map : ",result)

#map() function----------
def squre(x):
    return x*x

num=[1,2,3,4,5,]
result=list(map(squre,num))
print('Squre : ',result)

#map function-----
def squre(x):
    return x*x

num = [1,2,3,4,5,6,7,8,9]
result=list(map(squre,num))
print(result)

#map function-----
def qube(x):
    return x*x*x

num = [1,2,3,4,5,6,7,8,9]
result=list(map(qube,num))
print('Qube : ',result)

#map() cube----------
def cube(x):
    return x*x*x
num = [1,2,3,4,5]
result = list(map(cube,num))
print(result)

#map() function----------
def cube(x):
    return x*x*x
num = [1,2,3,4,5]
result = list(map(cube,num))
print(result)

#Filter function-----Even---
num=[1,2,3,4,5,6,7,8,9]
result = list(filter(lambda x : x%2==0,num))
print(result)

#Filter function-----Odd---
num = [1,2,3,4,5,6,7]
result = list(filter(lambda x : x%2!=0,num))
print(result)

#Filter function-----Even---
num = [1,2,3,4,5]
result = list(filter(lambda x: x%2==0,num))
print(result)

#Filter function-----Even---
add = [1,2,3,4,5,6]
result = list(filter(lambda a: a%2==0,add))
print("Even : ",result)

#Filter function-----Odd---
pop = [1,2,3,4,5,6]
result = list(filter(lambda b: b%2!=0,pop))
print("Odd : ",result)

#Filter function-----Odd---
rom = [1,2,3,4,5,6,7]
result = list(filter(lambda m: m%2!=0,rom))
print(result)
