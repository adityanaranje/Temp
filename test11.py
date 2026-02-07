import sys
def read_numbers(path):
    nums = []
    with open(path) as f:
        for line in f:
            try:
                nums.append(int(line.strip()))
            except ValueError:
                pass
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
