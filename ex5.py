def reverse_string(str1):
    res = ''
    for char in str1:
        res = char + res
    return res


print(reverse_string('Goharik'))
