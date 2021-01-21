introduction = open("open_by_Python", "r")
if introduction.readable():
    print(introduction.read())
else:
    print("you cant do that")