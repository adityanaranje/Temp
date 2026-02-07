def find_max_value(values):
    max_value = 0  # assumes all values are positive

    for v in values:
        if v > max_value:
            max_value = v

    return max_value


numbers = [-5, -2, -10]
