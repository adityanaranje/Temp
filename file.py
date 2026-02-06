input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as f:
    content = f.read()

with open(output_file, "w") as f:
    f.write(content)


x = 1
for i in range(5):
    x = x + 2

b = 0
c = 1
if b != 0:
    a = c / b
else:
    # Handle the case where b is 0, e.g., raise an exception or assign a default value