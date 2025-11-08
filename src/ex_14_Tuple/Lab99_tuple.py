cities= ("Paris","Pune","Patna","Srinagar")
print(len(cities))
print("Paris" in cities)
print("New Delhi" in cities)

#t= (56,12,50)
#t.append(20) #AttributeError: 'tuple' object has no attribute 'append'

ENV_API_URLS = tuple(["abc.com/get","xyz.com/post","qwe.com/put"])
print(ENV_API_URLS)

colors =("red ","blue", "green")
for c in colors:
    print(c)

numbers =(1,2) * 3
print(numbers)

numbers= "Pramod" * 3
print(numbers)


numbers = (1,2, 5,2,3,2)
print(len(numbers))

print(numbers.count(2))
print(numbers.index(5))


my_list = [1,2,3]
my_tuple =tuple(my_list)
print(my_tuple) #(1, 2 ,3)

back_to_list= list(my_tuple)
print(max(back_to_list)) # [1, 2 ,3]


my_list= [2,6,3]
print(my_list[0:2])
print(my_list[-1])