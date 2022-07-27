cafe_names = []
cafe_values = []
while True:
    user_input = str(input())
    if user_input == "MEOW":
        index = cafe_values.index(max(cafe_values))
        print(cafe_names[index])
        break
    cafe = user_input.split(" ")
    cafe_names.append(cafe[0])
    cafe_values.append(int(cafe[1]))
