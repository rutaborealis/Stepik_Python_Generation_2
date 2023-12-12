# 13.3
# 13.3.1
z1, z2 = input(), input()
print(f"({z1}) + ({z2}) = {complex(z1) + complex(z2)}")
print(f"({z1}) - ({z2}) = {complex(z1) - complex(z2)}")
print(f"({z1}) * ({z2}) = {complex(z1) * complex(z2)}")

# 13.3.2
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j,
           1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

list_complex = [abs(i) for i in numbers]
maximum = max(list_complex)
out = [c for c in numbers if abs(c) == maximum]

print(out[0])
print(maximum)

# 13.3.3
n = int(input())
z1, z2 = complex(input()), complex(input())

s_z1 = complex(z1.real, -z1.imag)
s_z2 = complex(z2.real, -z2.imag)

print(z1 ** n + z2 ** n + s_z1 ** n + s_z2 ** (n + 1))
