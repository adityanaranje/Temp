# Example 2: Test cases for calculate_average

def test_average_cases():
    avg1 = calculate_average([10, 20, 30])
    avg2 = calculate_average([])
    avg3 = calculate_average([5])

    print(avg1)  # Expected: 20
    print(avg2)  # Expected: 0
    print(avg3)  # Expected: 5


test_average_cases()
