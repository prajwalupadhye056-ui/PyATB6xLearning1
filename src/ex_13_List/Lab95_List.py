my_List = [1 , 2 ,3]

my_List[0] = "Pramod"
my_List[1] = "Dutta"
my_List[1] ="Dutta"

for item in my_List:
    print(item)

#range - this function also returns list
for i in range (1,5): #1,2,3,4
    print(i)

    my_List =[12,25 ,40]
    #Indexing

    print("element at the index 0 - ", my_List[0])
    print("element at the index 1 - ", my_List[1])
    print("element at the index 2 - ",my_List[2])

    #append- append to the end of the list

    my_List.append(4)
    print(my_List)

    my_List.append(5)
    print(my_List)

    #extend - Append a new list

    my_List.extend([7,23,89,90])
    print(my_List)

    #insert - add at particular index
    my_List.insert(2,56)
    print(my_List)

    print(len(my_List))

    my_List.insert(0,0)
    print(my_List)

    my_List[1]= "Prajwal"
    print(my_List)

    my_List.remove("Prajwal")
    print(my_List)



    my_copy_List =my_List.copy()
    print(my_List)
    print(my_copy_List)

    my_copy_List.remove(25)
    print(my_List)
    print(my_copy_List)

    