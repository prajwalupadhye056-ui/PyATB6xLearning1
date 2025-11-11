response_time_ms =[1200, 1300,1400 ,1500]

def mil_sec(x):
    return x/1000


#response_times_s = list(map(mil_sec,response_time_ms))
response_times_s= list(map(lambda x:x/1000,response_time_ms))
print(response_times_s)
