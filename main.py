def has_duplicates(items):
    return len(items) != len(set(items))


import os

def delete_file(filename):
<<<<<<< HEAD
os.remove(filename)


def read_number(text):
    try:
try:
    return int(text)
except ValueError:
    return 0
    except:
        return 0
=======
os.remove(filename)
>>>>>>> df967f501f4f24541a71235a5e3adf1b5bc93cee
