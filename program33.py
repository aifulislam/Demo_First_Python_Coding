#Exception Handling (part-1)-----------

num2 = int(input("Enter any number : "))
result = 20/ num2
print(result)
print("Done")

#Exception Handling (part-1)-----------
tex= "Aiful"
print(tex[3])
print("Done")

#Exception Handling (part-1)-----------
list  = [20,0,10]
result = list[2] / list[0]
print(result)
print("Done")

#Exception Handling (part-1)-----------
try:
    list = [20,0,10]
    result = list[0] / list[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("It is not possible to print")
except IndexError:
    print("Index Error")
    print("Successful")

finally:
print("Successful")

#Exception Handling (part-1)-----------
try:
    list = [20,0,10]
    result = list[0] / list[5]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("zero division error")
finally:
    print("Succesfuly")

#Exception Handling (part-2)--------
try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    result = num1 / num2
    print(result)
    print("Done")
except (ValueError,ZeroDivisionError) :
    print("You have entered incorrect input")
finally:
    print("Thank!!!")

#Exception Handling (part-2)--------
def vote(age):
    if age < 18:
        raise ValueError("Invalid Error")
    return 'You are allowed to vote'
try:
    print('Arif',vote(19))
    print('Tamim',vote(17))
except ValueError as e:
    print(e)

#Exception Handling (part-2)--------
def vote(age):
    if age < 18:
        raise ValueError("Invalid Error")
    return "You are allowed to vote"
try:
    print('Arif',vote(19))
    print('Tamim',vote(17))
except ValueError as v:
    print(v)


