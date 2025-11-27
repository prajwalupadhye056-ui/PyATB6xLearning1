try:
    data =open("test.json").read()
except FileNotFoundError as f:
    print(f)
