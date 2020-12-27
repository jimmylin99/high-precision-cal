from utils import split_num


def div_unsigned(a, b, precision):
    int_a, dec_a = split_num(a)
    int_b, dec_b = split_num(b)

    _a = (int_a + dec_a)[::-1]
    _b = (int_b + dec_b)[::-1]

    len_a = len(_a)


def division(a, b, precision):
    neg_a = a[0] = '-'
    neg_b = b[0] = '-'
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
