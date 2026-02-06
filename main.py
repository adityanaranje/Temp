def has_duplicates(items):
    return len(items) != len(set(items))


import os

def delete_file(filename):
def delete_file(filename):
    os.remove(filename)
os.remove(filename)


def read_number(text):
    try:
        return int(text)
    except ValueError:
        return 0
    """Returns the integer value of the input text, or 0 if it's not a valid number."""
    try:
        return int(text)
    except ValueError:
        return 0
    try:
try:
    return int(text)
except ValueError:
    return 0
except ValueError:
        return 0
=======
os.remove(filename)
>>>>>>> df967f501f4f24541a71235a5e3adf1b5bc93cee
