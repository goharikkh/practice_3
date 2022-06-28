def get_median(data):
    data.sort()
    if len(data) % 2 != 0:
        return data[len(data) // 2]
    else:
        return (data[int(len(data) / 2)] + data[int(len(data) / 2 - 1)]) / 2


print(get_median([1, 2, 5, 4, 6, 8]))
