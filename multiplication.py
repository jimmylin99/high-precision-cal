from utils import split_num, remove_suffix_zero


def mul_unsigned(a, b):
    int_a, dec_a = split_num(a)
    int_b, dec_b = split_num(b)

    dec_bits = len(dec_a) + len(dec_b)
    _a = (int_a + dec_a)[::-1]
    _b = (int_b + dec_b)[::-1]

    len_a = len(_a)
    len_b = len(_b)
    len_result = len_a + len_b
    _result = [0] * len_result

    for i in range(len_a):
        for j in range(len_b):
            k = i + j
            _result[k] += int(_a[i]) * int(_b[j])
    for i in range(len_result - 1):
        _result[i + 1] += _result[i] // 10
        _result[i] %= 10

    result = ''
    for i in range(len_result):
        if dec_bits != 0 and i == dec_bits:
            result = result + '.'
        result = result + str(_result[i])
    if len(int_a) + len(int_b) == 0:
        result = result + '.'
    result = result[::-1]
    result = remove_suffix_zero(result)

    return 'OK', result


def multiplication(a, b):
    neg_a = a[0] == '-'
    neg_b = b[0] == '-'
    if neg_a and neg_b:
        return mul_unsigned(a[1:], b[1:])
    elif neg_a:
        errcode, result = mul_unsigned(a[1:], b)
        result = '-' + result
    elif neg_b:
        errcode, result = mul_unsigned(a, b[1:])
        result = '-' + result
    else:
        return mul_unsigned(a, b)

    return errcode, result
