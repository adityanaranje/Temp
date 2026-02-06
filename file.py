input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as f:
    content = f.read()

with open(output_file, "w") as f:
    f.write(content)


x = 1
for i in range(-1):
    x = x + 2