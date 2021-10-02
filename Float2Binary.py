import numpy as np


class Float2Binary:
    def __init__(self, a, n_int=16, n_dec=16):
        self.a = a
        self.a_int = int(a)
        self.a_dec = a - int(a)
        self.n_int = n_int
        self.n_dec = n_dec
        self.b_int = np.zeros(self.n_int, dtype=int)
        self.b_dec = np.zeros(self.n_dec+1, dtype=int)
        self.integer_to_binary()
        self.decimal_to_binary()

    def __str__(self):
        x_string_1 = np.array2string(self.b_int, separator='')
        x_string_1 = x_string_1[1:-1]
        x_string_2 = np.array2string(self.b_dec, separator='')
        x_string_2 = x_string_2[1:-1]
        x_string = x_string_1 + '.' + x_string_2
        return x_string

    def integer_to_binary(self):
        for i in range(self.n_int - 1, -1, -1):
            x = 2 ** i
            if (self.a_int - x) >= 0:
                self.b_int[i] = 1
                self.a_int -= x
        self.b_int = self.b_int[::-1]

    def decimal_to_binary(self):
        for i in range(1, self.n_dec+1, 1):
            x = 2 ** (-1 * i)
            if (self.a_dec - x) >= 0:
                self.b_dec[i] = 1
                self.a_dec -= x
        self.b_dec = self.b_dec[1::]


if __name__ == "__main__":
    f2b = Float2Binary(375.814, 12, 12)
    print(f2b.b_int)
    print(f2b.b_dec)
    print(str(f2b))
