input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as f:
    content = f.read()

with open(output_file, "w") as f:
    f.write(content)


x = 1
for i in range(5):
    x = x + 2

b = 1
c = 1  # or any other non-zero value
a = b / c

b = (b / c) * c if c != 0 else 0  # or any other default value