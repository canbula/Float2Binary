import numpy as np


class IEEE754:
    def __init__(self, x, precision=1):
        self.precision = precision
        self.s = 0 if x >= 0 else 1
        x = abs(x)
        self.x = x
        self.i = self.integer2binary(int(x))
        self.d = self.decimal2binary(x-int(x))
        self.e = self.integer2binary((self.i.size-1)+127)

    def __str__(self):
        n = self.precision*32
        r = np.zeros(n, dtype=int)
        i_d = np.append(self.i[1::], self.d)
        print(str(self.s)
              + np.array2string(self.e, separator='')
              + np.array2string(i_d, separator=''))
        r[0] = self.s
        r[1+(8 - self.e.size):9:] = self.e
        r[32-i_d.size::] = i_d
        return np.array2string(r, separator='')

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
        n = 23 if self.precision == 1 else 52
        i = 0
        while x > 0 and i < n:
            x = x * 2
            b = np.append(b, np.array([int(x)]))
            x -= int(x)
            i += 1
        return b


a = IEEE754(123.51512)
print(a)
