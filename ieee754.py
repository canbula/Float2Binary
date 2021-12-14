import numpy as np


class IEEE754:
    def __init__(self, x, precision=2):
        self.precision = precision
        length_list = [16, 32, 64, 128, 256]
        exponent_list = [5, 8, 11, 15, 19]
        mantissa_list = [10, 23, 52, 112, 236]
        bias_list = [15, 127, 1023, 16383, 262143]
        self.length = length_list[precision]
        self.exponent = exponent_list[precision]
        self.mantissa = mantissa_list[precision]
        self.bias = bias_list[precision]
        self.s = 0 if x >= 0 else 1
        x = abs(x)
        self.x = x
        self.i = self.integer2binary(int(x))
        self.d = self.decimal2binary(x-int(x))
        self.e = self.integer2binary((self.i.size-1)+self.bias)
        self.m = np.append(self.i[1::], self.d)
        self.h = ''

    def __str__(self):
        r = np.zeros(self.length, dtype=int)
        i_d = np.append(self.i[1::], self.d)
        r[0] = self.s
        r[1+(self.exponent - self.e.size):(self.exponent + 1):] = self.e
        r[(1 + self.exponent):(1 + self.exponent + i_d.size):] = i_d[0:self.mantissa]
        s = np.array2string(r, separator='')
        return s[1:-1].replace("\n", "").replace(" ", "")

    @staticmethod
    def integer2binary(x):
        b = np.empty((0,), dtype=int)
        while x > 1:
            b = np.append(b, np.array([x % 2]))
            x = int(x/2)
        b = np.append(b, np.array([x]))
        b = b[::-1]
        return b

    def decimal2binary(self, x):
        b = np.empty((0,), dtype=int)
        i = 0
        while x > 0 and i < self.mantissa:
            x = x * 2
            b = np.append(b, np.array([int(x)]))
            x -= int(x)
            i += 1
        return b

    def str2hex(self):
        s = str(self)
        for i in range(0, len(s), 4):
            ss = s[i:i+4]
            si = 0
            for j in range(4):
                si += int(ss[j]) * (2**(3-j))
            sh = hex(si)
            self.h += sh[2]
        return self.h


if __name__ == "__main__":
    for p in range(5):
        a = IEEE754(13.375, p)
        print("x = %f | b = %s | h = %s" % (13.375, a, a.str2hex()))
