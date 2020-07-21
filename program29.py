#Zip Function---------

roll = [100,101,102,103,105,106]
name = ["Arif","Tamim","Nazim",'Ayon','Rajon','Nahid']
print(list(zip(name,roll,'ABCDEF')))

#Zip Function---------
roll = [101,102,103,104,105]
name = ['Arif','Tamim','Ayon','Rajon','Nahid']
class1 = ['MA',1,11,7,2,1]
print(list(zip(name,class1,roll)))

#Zip Function---------
roll = [101,102,103,104,105]
name = ['Arif','Tamim','Ayon','Rajon','Nahid']
address = ['Monirampur','Rajgonj','Kasappur','Kasappur','Kasappur']
a = list(zip(name,roll,address))
print(a)
