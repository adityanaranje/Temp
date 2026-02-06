def has_duplicates(items):
    return len(items) != len(set(items))


import os

def delete_file(filename):
    os.system(f"rm {filename}")
