def tup_to_num(data):
    s = 0
    for i in data:
        s = s * 10 + i
    return s


print(tup_to_num((1, 2, 3)))
