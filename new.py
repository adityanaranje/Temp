import os

def delete_file(filename):
    os.remove(filename)

b = 0
c = 1

if b != 0:
    a = c / b
else:
    # Handle the case where b is zero, e.g., raise a custom error or return a default value