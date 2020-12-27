from utils import split_num


def add_unsigned(a, b):
    int_a, dec_a = split_num(a)
    int_b, dec_b = split_num(b)

    # decimal part
    if len(dec_a) < len(dec_b):  # guarantee that len(dec_a) >= len(dec_b)
        dec_a, dec_b = dec_b, dec_a
    len_dec_min = len(dec_b)
    dec_result = dec_a[len_dec_min:]
    carry = 0
    for i in reversed(range(len_dec_min)):
        _r = int(dec_a[i]) + int(dec_b[i]) + carry  # consider carry bit
        carry, _c = divmod(_r, 10)
        dec_result = str(_c) + dec_result  # concatenation

    # integer part
    if len(int_a) < len(int_b):  # guarantee that len(int_a) >= len(int_b)
        int_a, int_b = int_b, int_a
    len_int_min = len(int_b)
    index_delta = len(int_a) - len(int_b)
    int_result = ''
    for i in reversed(range(len_int_min)):
        _r = int(int_a[index_delta + i]) + int(int_b[i]) + carry
        carry, _c = divmod(_r, 10)
        int_result = str(_c) + int_result
    for i in reversed(range(index_delta)):
        _r = int(int_a[i]) + carry
        carry, _c = divmod(_r, 10)
        int_result = str(_c) + int_result
    if carry != 0:
        int_result = str(carry) + int_result

    if dec_result != '':
        result = int_result + '.' + dec_result
    elif int_result != '':
        result = int_result
    else:
        return 'No Result', ''

    return 'OK', result


def addition(a, b):
    from subtraction import sub_unsigned
    neg_a = a[0] == '-'
    neg_b = b[0] == '-'
    if neg_a and neg_b:
        errcode, result = add_unsigned(a[1:], b[1:])
        result = '-' + result
    elif neg_a:
        return sub_unsigned(b, a)
    elif neg_b:
        return sub_unsigned(a, b)
    else:
        return add_unsigned(a, b)

    return errcode, result
