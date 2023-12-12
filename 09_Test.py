# 9 Test
# 9.1
set1 = {'p', 'a', 't', 'f'}
set2 = {'a', 't', 'f'}

print(set1 - set2)

# 9.2
n = int(input())
m = int(input())
k = int(input())
p = int(input())

print(n - m - k + p)

# 9.3
# 1
numbers = [int(i) for i in input().split()]
result = []
count = 0

for i in numbers:
    if i not in result:
        result.append(i)
    else:
        count += 1

print(count)

# 2
arr = [int(i) for i in input().split()]
set1 = set(arr)
print(len(arr) - len(set1))

# 9.4
cities = [input() for _ in range(int(input()))]
new_city = input()

if new_city not in cities:
    print('OK')
else:
    print('REPEAT')

# 9.5
m, n = int(input()), int(input())
set1 = {input() for _ in range(m)}
set2 = [input() for _ in range(n)]

for book in set2:
    if book in set1:
        print('YES')
    else:
        print('NO')

# 9.6
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}

result = list(set1.intersection(set2))
result.sort(reverse=True)

if result:
    print(*result)
else:
    print('BAD DAY')

# 9.7
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}

if set1 == set2:
    print('YES')
else:
    print('NO')

# 9.8
m, n = int(input()), int(input())
set1 = {input() for _ in range(m)}
set2 = {input() for _ in range(n)}

result = set1.difference(set2)

print(len(result))

# 9.9
m, n = int(input()), int(input())
set1 = {input() for _ in range(m)}
set2 = {input() for _ in range(n)}

result = set1.symmetric_difference(set2)

if len(result) != 0:
    print(len(result))
else:
    print('NO')

# 9.10
set1 = {pupil for pupil in input().split()}
set2 = {pupil for pupil in input().split()}

print(*sorted(set1 | set2))

# 9.11
m = int(input())  # mat
n = int(input())  # inf
arr = [input() for _ in range(m + n)]
only_one = 0

for pupil in set(arr):
    if arr.count(pupil) == 1:
        only_one += 1

if only_one > 0:
    print(only_one)
else:
    print('NO')

# 9.12
m = int(input())
lessons = [(frozenset({input() for _ in range(int(input()))})) for _ in range(m)]
s = lessons[0]

for i in range(1, m):
    s = s & lessons[i]

print(*sorted(s), sep='\n')
