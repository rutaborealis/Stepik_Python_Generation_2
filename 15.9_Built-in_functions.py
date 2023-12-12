# 15.9
from decimal import *
import string

# 15.9.1
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    result = any(map(lambda elem: True if elem in command else False, ignore))
    return result


print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))

# 15.9.2
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for (country, capital, populat) in zip(countries, capitals, population):
    print(f'{capital} is the capital of {country}, population equal {populat} people.')

# 15.9.3
abscissas = [Decimal(x) for x in input().split()]
ordinates = [Decimal(y) for y in input().split()]
applicates = [Decimal(z) for z in input().split()]

list_coordinates = zip(abscissas, ordinates, applicates)

result = all(map(lambda elem: elem[0] ** 2 + elem[1] ** 2 + elem[2] ** 2 <= 4, list_coordinates))
print(result)

# 15.9.4
ip_input = [i for i in input().split('.')]
result = all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, ip_input))
print(result)

# 15.9.5
a, b = int(input()), int(input())

arr = [str(i) for i in range(a, b + 1)]

def func(elem):
    digit = int(elem)
    for i in list(elem):
        if digit % int(i) != 0:
            return False
    return True

result_1 = list(filter(lambda elem: all(map(lambda x: '0' not in x, elem)), arr))
result_2 = [int(i) for i in filter(func, result_1)]

print(*result_2)

# 15.9.6
password = input()

result = all([any(map(lambda x: x in string.digits, password)),
             any(map(lambda x: x in string.ascii_uppercase, password)),
             any(map(lambda x: x in string.ascii_lowercase, password)),
             len(password) >= 7])
if result:
    print('YES')
else:
    print('NO')

# 15.9.7
lst = []
n = int(input())
for _ in range(n):
    k = int(input())
    arr_class = [input().split() for _ in range(k)]
    any(map(lambda x: x[1] == '5', arr_class))
    lst.append(any(map(lambda x: x[1] == '5', arr_class)))

result = all(lst)

if result:
    print('YES')
else:
    print('NO')
