a, b, h = int(input().strip()), int(input().strip()), int(input().strip())
if h < a:
    print("Deficiency")
elif h > b:
    print("Excess")
else:
    print("Normal")
