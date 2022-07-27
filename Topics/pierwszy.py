a = int(input())
b = int(input())

maks = 0
pierwszy = 0
dlugosc = 0
def nwd(x,y):
    print("poczatek")
    dzielnik = 0
    if x == y:
        print("rowne")
        dzielnik = x
    if x > y:
        for i in range(y, 1, -1):
            print("dziala 1")
            if x % i == 0 and y % i == 0:
                dzielnik = i
                break
    else:
        for i in range(x, 1, -1):
            print("dziala 2")
            if x % i == 0 and y % i == 0:
                print(i)
                dzielnik = i
                break
    print(dzielnik)
    if dzielnik > maks:
        maks = dzielnik
    return dzielnik


nwd(a, b)


