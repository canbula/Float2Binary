from integer_to_binary import *
from decimal_to_binary import *


def float_to_binary(a, n_int=16, n_dec=16):
    a_int = int(a)
    b_int = integer_to_binary(a_int, n_int)
    a_dec = a - a_int
    b_dec = decimal_to_binary(a_dec, n_dec)
    return b_int, b_dec


'''
usage example including transform the output to string
'''
if __name__ == "__main__":
    x_float = 375.814
    x_binary_int, x_binary_dec = float_to_binary(x_float, 10, 10)
    x_string_1 = np.array2string(x_binary_int, separator='')
    x_string_1 = x_string_1[1:-1]
    x_string_2 = np.array2string(x_binary_dec, separator='')
    x_string_2 = x_string_2[1:-1]
    x_string = x_string_1 + '.' + x_string_2
    print("%f = %s" % (x_float, x_string))
