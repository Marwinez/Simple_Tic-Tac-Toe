money = int(input())
chicken_cost = 23
goat_cost = 678
pig_cost = 1296
cow_cost = 3848
sheep_cost = 6769
animal = ""
animal_cost = 0
count = 0
if money >= sheep_cost:
    animal = "sheep"
    count = money // sheep_cost
elif money >= cow_cost:
    animal = "cow"
    count = money // cow_cost
elif money >= pig_cost:
    animal = "pig"
    count = money // pig_cost
elif money >= goat_cost:
    animal = "goat"
    count = money // goat_cost
elif money >= chicken_cost:
    animal = "chicken"
    count = money //chicken_cost

if count > 1 and animal != "sheep":
    animal += "s"
    print(count, animal)
elif count == 1 or animal == "sheep":
    print(count, animal)
else:
    print("None")
