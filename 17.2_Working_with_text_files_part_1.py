# 17.2
import random
from functools import reduce

# 17.2.1
s = input()
file = open(s, encoding='utf-8')

for line in file:
    print(line.strip())

file.close()

# 17.2.2
s = input()
file = open(s, encoding='utf-8')
arr = file.readlines()
print(arr[-2].strip())
file.close()

# 17.2.3
file = open('lines.txt', encoding='utf-8')
arr = file.readlines()
print(random.choice(arr).strip())
file.close()

# 17.2.4
file = open('numbers.txt', encoding='utf-8')
arr = file.readlines()
result = reduce(lambda x, y: int(x) + int(y), arr, 0)
print(result)
file.close()

# 17.2.5
file = open('nums.txt', encoding='utf-8')
lines = list(map(str.strip, file.readlines()))
p = list(filter(lambda num: num.isdigit(), lines))
result = reduce(lambda x, y: int(x) + int(y), p, 0)
print(result)
file.close()

# 17.2.6
file = open('prices.txt', encoding='utf-8')
lines = list(map(str.strip, file.readlines()))
arr = [a.split() for a in lines]
summary = 0

for elem in arr:
    summary += int(elem[1]) * int(elem[2])

print(summary)

file.close()