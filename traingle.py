n = 5

for x in range(1, n + 1):
    print("\n" * (n + x), end= " ")
    for y in range(1, x + 1):
        print(y, end= " ")
    for y in range (x - 1, 0, -1):
        print(y,end=" ")
    print()