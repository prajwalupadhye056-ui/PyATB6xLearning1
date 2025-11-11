student_info1 = {
    "name" : "Pramod",
    "age" : 67,
    "address" : {
            "home_address" :"ND",
            "office_address" : "ER"
    }

}

student_info2 = {
    "name" :"Amit",
    "age" : "63",
    "address": {
    "home_address": "NY",
    "office_address": "SY"
    }
}

student_List = [student_info1, student_info2]
print(student_List)
print(student_List[0])
print(student_List[0]["name"])
print(student_List[0]["address"]["office_address"])


