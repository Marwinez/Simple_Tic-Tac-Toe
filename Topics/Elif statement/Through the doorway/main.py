a = int(input().strip())
b = int(input().strip())
c = int(input().strip())
x = int(input().strip())
y = int(input().strip())
dim_ab = a * b
dim_bc = b * c
dim_ca = c * a
door_size = x * y
if door_size >= dim_ab:
    print("The box can be carried")
elif door_size >= dim_bc:
    print("The box can be carried")
elif door_size >= dim_ca:
    print("The box can be carried")
else:
    print("The box cannot be carried")
