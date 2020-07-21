#List as input from user------------
n = input('Enter any letter : ')
list = n.split()
sum = 0
for num in list:
    sum = sum + int (num)
print(sum)

#List as input from user------------
n = input('Enter any number : ')
list = n.split()
sum = 0
for num in list:
    sum = sum + int(num)
print(sum)

#List as input from user------------
n = input('Enter any number : ')
list = n.split()
sum = 0
for num in list:
    sum = sum  + int(num)
print(sum)

#List as input from user------------
numberOfLetters = 0
numberOfDigits = 0
numberOfWords = 0
text = input("Enter a text of number : ")
for x in text:
    x = x.lower()
    if x >= 'a' and x<='z':
        numberOfLetters = numberOfLetters + 1

    elif x >= '0' and x<='9':
        numberOfDigits = numberOfDigits +1

    elif x == ' ':
        numberOfWords = numberOfWords +1

print("numberOfLetters : ",numberOfLetters)
print("numberOfDigits : ",numberOfDigits)
print("numberOfWords : ",numberOfWords + 1)

#List as input from user------------
numberOfLetters = 0
numberOfDigits = 0
numberOfWords = 0
text = input('Enter press any sentence : ')
sum = 0
for x in text:
    x = x.lower()
    if x>='a' and x<='z':
        numberOfLetters = numberOfLetters + 1
    elif x>='0' and x<='9':
        numberOfDigits = numberOfDigits + 1
    elif x==' ':
        numberOfWords = numberOfWords + 1

print('numberOfLetters : ',numberOfLetters)
print('numberOfDigits : ',numberOfDigits)
print('numberOfWords : ',numberOfWords + 1)

# List as input from user------------
numberOfLetters = 0
numberOfDigits = 0
numberOfWords = 0
text = input('Enter press any sentence : ')
sum = 0
for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numberOfLetters = numberOfLetters + 1
    elif x >= '0' and x <= '9':
        numberOfDigits = numberOfDigits + 1
    elif x == ' ':
        numberOfWords = numberOfWords + 1

print('numberOfLetters : ', numberOfLetters)
print('numberOfDigits : ', numberOfDigits)
print('numberOfWords : ', numberOfWords + 1)

