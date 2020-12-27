from utils import split_num


def sub_unsigned(a, b):
    int_a, dec_a = split_num(a)
    int_b, dec_b = split_num(b)

    # decimal part
    len_dec_a = len(dec_a)
    len_dec_b = len(dec_b)
    len_dec_min = min(len_dec_a, len_dec_b)
    len_dec_max = max(len_dec_a, len_dec_b)
    if len_dec_a < len_dec_b:
        dec_a = dec_a + '0' * (len_dec_max - len_dec_min)
    else:
        dec_b = dec_b + '0' * (len_dec_max - len_dec_min)
    dec_result = ''
    borrow = 0
    for i in reversed(range(len_dec_max)):
        _r = int(dec_a[i]) - int(dec_b[i]) - borrow  # consider borrow bit
        borrow = 1 if _r < 0 else 0
        _c = (_r + 10) % 10
        dec_result = str(_c) + dec_result  # concatenation

    # integer part
    len_int_a = len(int_a)
    len_int_b = len(int_b)
    len_int_min = min(len_int_a, len_int_b)
    len_int_max = max(len_int_a, len_int_b)
    if len_int_a < len_int_b:
        int_a = '0' * (len_int_max - len_int_min) + int_a
    else:
        int_b = '0' * (len_int_max - len_int_min) + int_b
    int_result = ''
    for i in reversed(range(len_int_max)):
        _r = int(int_a[i]) - int(int_b[i]) - borrow
        borrow = 1 if _r < 0 else 0
        _c = (_r + 10) % 10
        int_result = str(_c) + int_result
    if borrow != 0:
        errcode, result = sub_unsigned(b, a)
        result = '-' + result
        return errcode, result

    if dec_result != '':
        result = int_result + '.' + dec_result
    elif int_result != '':
        result = int_result
    else:
        return 'No Result', ''

    return 'OK', result


def subtraction(a, b):
    from addition import add_unsigned
    neg_a = a[0] == '-'
    neg_b = b[0] == '-'
    if neg_a and neg_b:
        return sub_unsigned(b[1:], a[1:])
    elif neg_a:
        errcode, result = add_unsigned(a[1:], b)
        result = '-' + result
    elif neg_b:
        return add_unsigned(a, b[1:])
    else:
        return sub_unsigned(a, b)

    return errcode, result
