squares = [1,4,9,16,25]
print(squares)
print(squares.pop()) #Remove and return item at index default (last element)

print(squares)

print(squares.pop(1))
print(squares)

squares.clear()
print(squares)

#index(element ,start,end)
#Returns the index of first occurrence of the element

numbers =[10,20,90, 20,30,40]
print(numbers.index(20))

print(numbers.count(20))

numbers.sort()
print(numbers)

numbers.sort(reverse= True)
print(numbers)


#Reverse()- reverses the list in the place

numbers.reverse()
print(numbers)

#max()/ min () /sum () - works for numerical lists
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#Slicing
print(numbers)
print(numbers[1:4]) #index 1 to 3
print(numbers[-1])

print("apple" in numbers)
print(20 in numbers)

#List Creation and Comprehension
#range(1,5) - list

l =list(range(1,5))
print(l)

#1,2,3,4 -O/P



#Nested list

matrix = [[1,2,3], [4,5,6],[7,8,9]]

print(matrix[1][2])

#del statement - Deletes an element by index or the whole list(keyword)
#delete will never return the element and pop() will return the element
del numbers[0]
print(numbers)