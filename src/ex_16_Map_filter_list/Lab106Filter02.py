nums = [1,2,3 ,4,5,6]

def even_num(x):
    return x % 2 == 0

even_numbers = list(filter(even_num, nums))
print(even_numbers)



list_students= [50, 60 ,80]
def keep(x):
    if x > 50:
        return True

all_list_students = list(filter(keep, list_students))
print(all_list_students)