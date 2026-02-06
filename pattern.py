n = 5

for i in range(1, n + 1):      # outer loop → rows
    for j in range(i):         # inner loop → stars
        print("*", end="")
    print()
