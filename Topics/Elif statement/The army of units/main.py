num = int(input())
if num < 1:
    print("no army")
elif num in range(1, 10):
    print("few")
elif num in range(10, 50):
    print("pack")
elif num in range(50, 500):
    print("horde")
elif num in range(500, 1000):
    print("swarm")
else:
    print("legion")
