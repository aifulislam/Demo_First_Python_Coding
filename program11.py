#Inner If Statement--------

if 6>4:
    if 6>3:
        if 7>2:
         print('Hi')

if 6<9:
    if 4<6:
        if 5<6:
            if 9<8:
                print('Hi')
            else:
                print('hello')

#Lage number find of three numbers-----
num1 = 90
num2 = 80
num3 = 50
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
if num2>num1:
    if num2>num3:
        print(num2)
    else:
        print(num3)
#Lage number find of three numbers-----
num4 = 50
num5 = 70
num6 = 60
if num4>num5:
    if num4>num6:
        print(num4)
    else:
        print(num6)

else:
    if num5>num6:
        print(num5)
    else:
        print(num6)
#Ternary Operator-----
num7 = 50
num8 = 60
'''
if num7>num8:
    print(num7)
else:
    print(num8)
'''
max = num7 if num7>num8 else num8
print('Max = ',max)
#Logical operator-----and--or--not---
#Find Large Number---using-and-------
'''
num10 = 70
num11 = 80
num12 = 90
if num10>num11 and num10>num12 :
    print(num10)
elif num11>num10 and num11>num12:
    print(num11)
else:
    print(num12)
'''
num10 = 90
num11 = 80
num12 = 60
if num10>num11 and num10>num12:
    print(num10)
elif num11>num10 and num11>num12:
    print(num11)
else:
    print(num12)
#Logical operator-----and--or--not---
#Find Vowel(a,e,i,o,u)---using-or-------
ch='a'
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' \
    or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print('Vowel')
else:
    print('Consonant')
#Logical operator-----and-------
# Letter Grade Program-----GPA--
mark = 55
if mark>=80 and mark<=100:
    print('A+')
elif mark>=70 and mark<=79:
    print('A')
elif mark>=60 and mark<=69:
    print('A-')
elif mark>=50 and mark<=59:
    print('B')
elif mark>=40 and mark<=49:
    print('C')
elif mark>=33 and mark<=39:
    print('D')
else:
    print('F')
