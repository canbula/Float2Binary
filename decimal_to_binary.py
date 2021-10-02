import numpy as np


def decimal_to_binary(a, n=16):
    b = np.zeros(n, dtype=int)
    for i in range(1, n, 1):
        x = 2**(-1*i)
        if (a - x) >= 0:
            b[i] = 1
            a -= x
    b = b[1::]
    return b


'''
usage example including transform the output to string
'''
if __name__ == "__main__":
    x_decimal = 0.814
    x_binary = decimal_to_binary(x_decimal, 10)
    x_string = np.array2string(x_binary, separator='')
    print("%f = %s" % (x_decimal, x_string[1:-1]))
