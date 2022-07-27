numbers = []
while True:
    num = input()
    if num == '.':
        print(sum(numbers) / len(numbers))
        break
    numbers.append(int(num))
