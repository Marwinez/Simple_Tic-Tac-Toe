result = 0
value = 0
while True:
    number = int(input())
    value += number
    result += number ** 2
    if value == 0:
        print(result)
        break
