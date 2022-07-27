number = str(input())
old_list = [int(num) for num in number]
new_list = []
result = 0
for num in old_list:
    result += num
    new_list.append(result)
print(new_list)
