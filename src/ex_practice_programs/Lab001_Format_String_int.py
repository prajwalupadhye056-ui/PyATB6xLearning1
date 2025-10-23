#concatnate with string and integer
b ,c , d = 23, 53.6, 89
print("{}{}".format("The Value is :", b))

#concantenate with two strings
a= "This is done"
b= 'This is already executed'

print(a)
print(b)

print(a + "" +b)

#List -It is data type that allows multiple values and can be with different data types

values =[5,"Rahul", 63.23,"Great"]
print(values[0])
print(values[2])
print(values[3])
print(values[-1]) # Great

print(values[1:3]) #Rahul #63.23 #Inserting


values.insert(2, "Prajwal")
print(values)

values.append("End") #Appending to the end of the string
print(values)

values[1]= "RAHUL" #Updating
print(values)

del values[0] #Deleting
print(values)

