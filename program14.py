#List(Part-1)----------
subjects = ['C','c++','Java','Python','Php','swift']
print(subjects)
print('My First learning programming Language is : ',subjects[0])
print('My fabright programming language is : ',subjects[0]+ subjects[2]+subjects[4])
print(subjects[-1])

#Find your List--------
print('Find your List--------')
print("Programming_Language_2 : ")
Programming_Language = ['C','c++','Java','Python','Php','swift','Roby']
print(Programming_Language)
print('Using in--------------')
print('Php' in Programming_Language)
print('C' in Programming_Language)
print('Using not in--------------')
print('C' not in Programming_Language)

#Adding other subject---------
print('Adding other subject---------')
print(Programming_Language + ['Android',22,'OS'])
print(Programming_Language * 2)

#List(Part-2)----------
print('List(Part-2)----------')
Programming_Language_part_2 = ['C','c++','Java','Python','Php','swift','Roby']
#Lenth count------------
print('Lenth count------------')
print('lenth count :',len(Programming_Language_part_2))
#Using append()----------
print('Using append()----------')
Programming_Language_part_2.append('TOC')
print('Using append : ',Programming_Language_part_2)
#Using insert()----------
print('Using insert()----------')
Programming_Language_part_2.insert(1,'OS')
print(Programming_Language_part_2)
#Using removed()----------
print('Using removed()----------')
Programming_Language_part_2.remove('Php')
print(Programming_Language_part_2)
#Using Sortting()----------
print('Using Sortting()----------')
Programming_Language_part_2.sort()
print(Programming_Language_part_2)
#Using Pop()----------
print('Using Pop()----------')
Programming_Language_part_2.pop()
print(Programming_Language_part_2)
#Using clear()----------
'''
print('Using clear()----------')
Programming_Language_part_2.clear()
print(Programming_Language_part_2)
'''
#Using Copy()----------
print('Using Copy()----------')
mark = [20,10,30,50,40]
mark2 = mark.copy()
print(mark2)
#Using Index()----------
print('Using Index()----------')
mark1 = [20,10,30,50,40]
pos = mark1.index(2)
print(pos)
#Using Count()----------
print('Using count()----------')
cnt = [20,4,55,4,63,4,45,22]
pop = cnt.count(4)
print(pop)
