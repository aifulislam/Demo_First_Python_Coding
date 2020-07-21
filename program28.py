#List Comprehensions------------

num = [1,2,3,4,5]
result = [x*x for x in num]
print('Comprehensions list1 : ',result)

#Cube-------
num1 = [1,2,3,4,5]
result = [x*x*x for x in num1]
print('Comprehensions list2 : ',result)

# List Comprehensions------------
num2 = [1,2,3,4,5,6]
result = [x*x*x for x in num2]
print('Comprehensions list3 : ',result)

# List Comprehensions------------

num = [1,2,3,4,5,6]
result=list(filter(lambda x: x%2==0,num))
print('Comprehensions list3 : ',result)

#List Comprehensions of even------------

num = [1,2,3,4,5,6]

result = [x for x in num if x%2==0]
print('Comprehensions list of Even : ',result)
#result=list(filter(lambda x: x%2==0,num))

#List Comprehensions of odd------------
num = [1,2,3,4,5,6]
result=[x for x in num if x%2!=0]
print('Comprehensions list of odd : ',result)

#List Comprehensions of odd------------
num = [1,2,3,4,5,6]
result=[x*x for x in num if x%2!=0]
print('Comprehensions list of odd : ',result)
