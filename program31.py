#Reading a file----
file = open("me.txt",'r')
text = file.read()
print(text)
file.close()

#Reading a file----
file = open("me.txt","r+")
text= file.read()
print(text)
file.close()

#Reading a file of size----
file = open("me.txt","r")
text = file.read()
print(text)
size = len(text)
print('Size1 : ',text)
file.close()

#Reading a file of size----
file = open("me.txt","r")
text = file.read()
print(text)
size=len(text)
print(size)
file.close()
#Reading a file of size----
file = open("me.txt","r+")
text = file.read()
print(text)
size = len(text)
print('Size2 : ',size)
file.close()

#readlines a file----
file = open("me.txt","r+")
text = file.readlines()[0]
print(text)
file.close()

#readlines a file----
file = open("me.txt","r")
text = file.readlines()[2]
print(text)
file.close()
#readlines a file--using for loop--

file = open("me.txt",'r+')
for line in file:
    print(line)
file.close()

#readlines a file--using for loop--
file = open("me.txt","r+")
for line in file :
    print(line)
file.close()

#readlines a file--using for loop--
file = open('me.txt',"r+")
for line in file:
    print(line)
file.close()

#readlines a file--using for loop--
file = open("me.txt","r+")
for line in file :
    print(lene)
file.close()