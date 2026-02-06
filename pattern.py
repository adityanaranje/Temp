n = 5

for i in range(1, n + 1): 
    x = 0     # outer loop → rows
    for j in range(i):    
        x + 1     # inner loop → stars
        print("*", end="")
    print()

print(x)