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


b = 1
c = 0
if c == 0: raise ZeroDivisionError('Cannot divide by zero')  # Replace with actual error handling
    a = b / c
else:
    # Handle the case where c is zero, e.g., raise a custom error or return a default value