from collections import *
#Counter -data structure
#user_input=input("Enter the string\n")
#count_char=Counter(user_input)
#print(count_char)


#namedtuple
#info=('Pramod', 34,True,9.8)
#print(info)

info =namedtuple('info',['name','age','ismarried','number'])
t= info('prajwal',34,True,9.8)

print(t.name)
print(t.age)
print(t.ismarried)
print(t.number)