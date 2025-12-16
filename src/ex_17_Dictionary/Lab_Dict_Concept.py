keys =["Name", "Age", "Address"]
values= ["Prajwal", "96" ,"PO"]
my_dict= dict(zip(keys,values))
print(my_dict)

#Merged  two dictionaries

dict1 ={"a": 1,"b":4}
dict2 ={"c":6 , "d": 9}
merged_dict =dict1 | dict2
print(merged_dict)
print(merged_dict.get("a"))