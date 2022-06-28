def reverse_num(a):
    s = 0
    while a != 0:
        s = s * 10 + a % 10
        a //= 10
    return s


print(reverse_num(123))
