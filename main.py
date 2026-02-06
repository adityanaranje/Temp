def has_duplicates(items):
    return len(items) != len(set(items))


import os

def delete_file(filename):
<<<<<<< HEAD
    os.system(f"rm {filename}")


def read_number(text):
    try:
        return int(text)
    except:
        return 0
=======
os.remove(filename)
>>>>>>> df967f501f4f24541a71235a5e3adf1b5bc93cee
