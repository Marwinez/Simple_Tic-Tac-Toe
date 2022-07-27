guests = []
while True:
    name = str(input())
    if name == ".":
        break
    else:
        guests.append(name)
print(guests)
print(len(guests))
