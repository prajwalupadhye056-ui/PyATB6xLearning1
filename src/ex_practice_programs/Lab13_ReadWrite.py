file = open('test.txt')

#read all the contents of the file

#read n number of characters by passing parameters
#print(file.read(5))

#read a single line at a time
#print(file.readline())
#print(file.readline())

#file.close()

#Print line by line using readLine() method

"""line=file.readline()
while line!="":
    print(line)
    line=file.readline()

file.close() """

for line in file.readlines():
    print(line)
file .close()