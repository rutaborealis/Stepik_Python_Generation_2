# 13.2
from fractions import Fraction
from math import *

# 13.2.1
numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
           '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
           '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
           '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']

for num in numbers:
    print(f"{num} = {Fraction(num)}")

# 13.2.2
s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 ' \
    '1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 ' \
    '0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'

numbers_fraction = [Fraction(i) for i in s.split()]

print(max(numbers_fraction) + min(numbers_fraction))

# 13.2.3
m, n = int(input()), int(input())

print(Fraction(m, n))

# 13.2.4
d1, d2 = input(), input()
f1 = Fraction(d1)
f2 = Fraction(d2)

print(f"{d1} + {d2} = {f1 + f2}")
print(f"{d1} - {d2} = {f1 - f2}")
print(f"{d1} * {d2} = {f1 * f2}")
print(f"{d1} / {d2} = {f1 / f2}")

# 13.2.5
n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += Fraction(1, i ** 2)

print(sum)

# 13.2.6
n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += Fraction(1, factorial(i))

print(sum)

# 13.2.7
n = int(input())

list_numerators = [i for i in range(1, n // 2 + 1)]
list_denominators = [i for i in range(n - 1, n // 2, -1)]
list_zip = list(zip(list_numerators, list_denominators))
out = [Fraction(x, y) for (x, y) in list_zip if Fraction(x, y).numerator + Fraction(x, y).denominator == n]

print(max(out))

# 13.2.8
n = int(input())

list_numerators = [i for i in range(1, n)]
list_denominators = [i for i in range(2, n + 1)]
out = []

for i in list_numerators:
    for j in list_denominators:
        if gcd(i, j) == 1 and Fraction(i, j) < 1:
            out.append(Fraction(i, j))

for i in sorted(out):
    print(i)
