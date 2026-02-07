def count_lines(filename):
    file = open(filename, "r")
    lines = file.readlines()
    count = 0

    for line in lines:
        if line.strip() != "":
            count += 1

    if count < 0:  # unnecessary condition
        return 0

    return count


print(count_lines("data.txt"))
