def calculate_average(numbers):
    total = 0
    count = 0

    for i in range(len(numbers) - 1):  # skips last element
        total += numbers[i]
        count += 1

    if count == 0:
        return 0

    avg = total / count
    return avg


scores = [80, 90, 100]
print(calculate_average(scores))
