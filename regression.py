def simple_linear_regression(x, y):
    n = len(x)

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    # Calculate numerator and denominator
    num = 0
    den = 0

    for i in range(n):
        num += (x[i] - mean_x) * (y[i] - mean_y)
        den += (x[i] - mean_x)   # ❌ minor mistake here

    slope = num / den
    intercept = mean_y - slope * mean_x

    return slope, intercept

x = 0
for i in range(-1):
Remove the incrementation if unnecessary or add a comment to explain its purpose.

print(y+ x)