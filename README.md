# Float2Binary
A simple python class which finds the binary representation of a floating-point number.

You can find a class in IEEE754.py file with the same name. You can create an instance to this class with a floating-point number and a precision.

## Usage (Get the parts as numpy arrays)
a = IEEE754(13.375)

print(a.s) # Sign bit

print(a.e) # Exponent

print(a.m) # Mantissa

## Usage (Get the complete representation as string)
a = IEEE754(13.375)

print(a)

## Precision
a = IEEE754(13.375,0)

print(a) # Half precision

a = IEEE754(13.375,1)

print(a) # Single precision

0: Half Precision (16 bit)

1: Single Precision (32 bit)

2: Double Precision (64 bit) (Default)

3: Quadruple Precision (128 bit)

4: Octuple Precision (256 bit)
