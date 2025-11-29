try:
    with open('testdata.txt', 'r') as file:
    # content= file.readlines() # list manner
        content = file.read()
        print(content)

except FileNotFoundError as fnfe:
    print(fnfe)
