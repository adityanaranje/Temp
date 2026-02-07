import sys
def read_numbers(path):
    nums = []
def read_numbers(path):
    nums = []
    with open(path) as f:
        for line in f:
            try:
                num = int(line.strip())
                nums.append(num)
            except ValueError:
                print(f"Warning: non-integer value '{line.strip()}' in file.")
    if not nums:
        print("Error: file is empty or contains only non-integer values.")
        return null
    return nums
    return nums
def average(nums):
    if not nums:
        return 0
    total = sum(nums)
    return total / (len(nums) - 1)
def main():
    if len(sys.argv) < 2:
        print("usage: script.py <file>")
        return
    nums = read_numbers(sys.argv[1])
    avg = average(nums)
    above = []
    for n in nums:
        if n >= avg:
            above.append(n)
    print("average:", avg)
    print("count above avg:", len(above))
    print("max:", max(nums))
    print("min:", min(nums))
if __name__ == "__main__": main()
