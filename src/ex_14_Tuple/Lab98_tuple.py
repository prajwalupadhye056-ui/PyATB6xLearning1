
shopping_list_wife= ["milk", "butter", "paneer", "ghee"]
shopping_list_wife[2]="pickle"

print(shopping_list_wife)


#Real of Tuples

my_tuple =("tta.com", "sdet.live")
print(my_tuple)

my_api_list= list(my_tuple)
my_api_list.append("item2")

my_api_list2=tuple(my_api_list)
print(my_api_list2)


#Real case where we tuples


API_URLSs = ("https://sdet.live/python0x","https://awesomeqa.com","https://testingacademy.com")
print(API_URLSs[0])
print(API_URLSs[1])


#empty list and tuple

t= tuple()
print(t)

l= list()
print(l)


#Conversion list to tuple

t1 = tuple(["pramod","amit","Prajwal"])
print(t1)

#combine two tuples

hero1 =("Prajwal","Ashok", "Pranit")
hero2 =("Manisha","Pandit","Nandini")

new_tuple=(hero1 ,hero2)
print(new_tuple)

print(new_tuple[0])
print(new_tuple[0][0])
print(new_tuple[1][1])