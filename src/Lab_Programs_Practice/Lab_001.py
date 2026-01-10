# Read and write files in Python

with open("testdata.txt","w") as f:
    f.write("Hello Good Morning !!!")

with open("testdata.txt","r") as f:
    content=f.read()
    print(content)