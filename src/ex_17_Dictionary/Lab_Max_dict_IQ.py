#function that returns the maximum value from a dictionary

# {"a" :10 ,"b" : 20, "c" : 40}



def max_value_dict(dictionary):
     return max(dictionary.values())

#def min_value_dict(dictionary):
  #   return min(dictionary.values())

def max_key_dict(dictionary):
    return max(dictionary.keys())

#def min_key_dict(dictionary):
  #   return min(dictionary.keys())

print(max_value_dict({"a": 10,"b": 30, "c": 60}))
print(max_key_dict({"a": 10,"b": 30, "c": 60}))