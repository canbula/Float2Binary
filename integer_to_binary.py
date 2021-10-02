import numpy as np


def integer_to_binary(a, n=16):
    b = np.zeros(n, dtype=int)
    for i in range(n-1, -1, -1):
        x = 2**i
        if (a - x) >= 1:
            b[i] = 1
            a -= x
    b = b[::-1]
    return b


'''
usage example including transform the output to string
'''
if __name__ == "__main__":
    x_integer = 375
    x_binary = integer_to_binary(x_integer, 10)
    x_string = np.array2string(x_binary, separator='')
    print("%d = %s" % (x_integer, x_string[1:-1]))
