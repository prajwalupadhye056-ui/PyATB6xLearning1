#SET
# Collection Unique elements
#{} =Parenthesis

my_list={5,6,2,5,8,9,7,6}
print(my_list)

#list to set
list1 =[45.63,89.62,56.21]
set1 = set(list1)
print(set1)

#tuple to set
t= ("TheTestingAcademy", "for", "TheTestingAcademy")
print(t)
print(set(t))


#mixed
mixed= {56.32,"Prajwal","rajesh","True",1,"False",0, 56,21}
print(mixed)

for item in mixed:
    print (item)


mixed.add(10)
mixed.remove("Prajwal")
print(mixed)



#empty set
empty =set()
print(type(empty))

