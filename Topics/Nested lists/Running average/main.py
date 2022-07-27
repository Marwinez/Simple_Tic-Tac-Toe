num_list = [int(num) for num in str(input())]
print([(num_list[i] + num_list[i + 1]) / 2 for i in range(len(num_list) - 1)])
