def exit_program():
    print('Exit the program')
    exit(0)


def split_num(a):
    neg_a = a[0] == '-'
    index_decimal_point_a = len(a)
    for i in range(len(a)):
        if a[i] == '.':
            index_decimal_point_a = i
            break
    int_a = a[1:index_decimal_point_a] if neg_a else a[:index_decimal_point_a]
    dec_a = a[index_decimal_point_a + 1:]

    return int_a, dec_a


def remove_prefix_zero(a):
    if len(a) == 0:
        return a
    if a[0] == '-':
        return '-' + remove_prefix_zero(a[1:])
    i = 0
    while i < len(a) and a[i] == '0':
        i += 1
    if i == len(a):
        return '0'
    if a[i] == '.':
        return '0' + a[i:]
    return a[i:]


def remove_suffix_zero(a):
    if len(a) == 0:
        return a
    i = 0
    while i < len(a):
        if a[i] == '.':
            break
        i += 1
    if i == len(a):  # no decimal part
        return a
    i = len(a) - 1
    while i >= 0 and a[i] == '0':
        i -= 1
    if a[i] == '.':  # no need for checking i >= 0
        return a[:i+1] + '0'
    return a[:i+1]
