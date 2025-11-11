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

student_info3 = {
    "name" :"Suresh",
    "age" : "95",
    "address": {
    "home_address": "Baner",
    "office_address": "Sangli"
    }
}

student_List = [student_info1, student_info2, student_info3]
print(student_List)
print(student_List[2]["address"]["office_address"])