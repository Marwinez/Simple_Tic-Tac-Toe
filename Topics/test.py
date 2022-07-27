
slowo = ""
maks = 0
for _ in range(3):
    linia = input()
    kub = [0] * 255
    for j in list(linia):
        kub[ord(j)] += 1
    ile = 0
    for j in kub:
        if j != 0:
            ile += 1
    if ile > maks:
        maks = ile
        slowo = linia
print(slowo, maks)
print(kub)
