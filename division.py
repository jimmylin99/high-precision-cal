from utils import split_num, remove_suffix_zero, remove_prefix_zero


def greater_or_equal(a, b):
    from subtraction import sub_unsigned
    _, result = sub_unsigned(a, b)
    if result[0] == '-':
        return False
    return True


def is_zero(x):
    x = remove_prefix_zero(remove_suffix_zero(x))
    int_x, dec_x = split_num(x)
    if int_x == '0':
        return dec_x in ['0', '']
    if int_x == '':
        return dec_x == '0'
    return False


def div_unsigned(a, b, precision):
    from subtraction import sub_unsigned
    if is_zero(b):
        return 'Error: Divide by 0', ''
    int_a, dec_a = split_num(a)
    int_b, dec_b = split_num(b)

    # digits for decimal point to move left
    net_dec_delta = len(dec_a) - len(dec_b)

    _a = int_a + dec_a
    _b = int_b + dec_b

    len_a = len(_a)

    len_result = len_a + precision - net_dec_delta
    if len_result <= 0:
        return 'OK', '0.' + '0' * precision
    _result = [0] * len_result
    div = ''
    for i in range(len_result):
        if i < len_a:
            div = div + _a[i]
        else:
            div = div + '0'
        while greater_or_equal(div, _b):
            _result[i] += 1
            _, div = sub_unsigned(div, _b)
    result = ''
    if len_result < precision:
        result = '0.' + '0' * (precision - len_result)
    for i in range(len_result):
        if len_result - i == precision:
            result = result + '.'
        result = result + str(_result[i])

    return 'OK', result


def division(a, b, precision):
    neg_a = a[0] == '-'
    neg_b = b[0] == '-'
    if neg_a and neg_b:
        return div_unsigned(a[1:], b[1:], precision)
    elif neg_a:
        errcode, result = div_unsigned(a[1:], b, precision)
        result = '-' + result
    elif neg_b:
        errcode, result = div_unsigned(a, b[1:], precision)
        result = '-' + result
    else:
        return div_unsigned(a, b, precision)

    return errcode, result
