def sum_of_min_max(data):
    max_ = min_ = data[0]
    for i in data:
        if i > max_:
            max_ = i
        elif i < min_:
            min_ = i
    return min_ + max_


print(sum_of_min_max([1, 2, 3, 5]))
