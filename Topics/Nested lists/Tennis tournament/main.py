n = int(input())
list_all = [input().split() for _ in range(0, n)]
list_win = [name_group[0] for name_group in list_all if name_group[1] == 'win']
print(list_win)
print(len(list_win))
