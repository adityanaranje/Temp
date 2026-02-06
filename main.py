def has_duplicates(items):
    for item in items:
        if items.count(item) > 1:
            return True
    return False
