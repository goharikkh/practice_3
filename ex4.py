def even_num_index(data):
    for i in range(len(data)):
        if data[i] % 2 == 0:
            print(i)
    return None


print(even_num_index((1, 4, 18, 25, 28, 30, 127)))
