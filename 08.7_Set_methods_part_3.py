# 8.7
# 8.7.1
x = set(input())
y = set(input())

if x.isdisjoint(y):
    print('NO')
else:
    print('YES')

# 8.7.2
x = set(input())
y = set(input())

if y.issubset(x):
    print('YES')
else:
    print('NO')

# 8.7.3
set1 = set([int(i) for i in input().split()])
set2 = set([int(i) for i in input().split()])
set3 = set([int(i) for i in input().split()])

result = set1.intersection(set2)
result = result.difference(set3)
result = list(result)
result.sort(reverse=True)
print(*result)

# 8.7.4
set1 = set([int(i) for i in input().split()])
set2 = set([int(i) for i in input().split()])
set3 = set([int(i) for i in input().split()])

union_set = set1.union(set2)
union_set = union_set.union(set3)

intersection_set = set1.intersection(set2)
intersection_set = intersection_set.intersection(set3)

result = union_set.difference(intersection_set)
result = list(result)
result.sort()
print(*result)

# 8.7.5
set1 = set([int(i) for i in input().split()])
set2 = set([int(i) for i in input().split()])
set3 = set([int(i) for i in input().split()])

result = set3.difference(set1, set2)

result = list(result)
result.sort(reverse=True)
print(*result)

# 8.7.6
set1 = set([int(i) for i in input().split()])
set2 = set([int(i) for i in input().split()])
set3 = set([int(i) for i in input().split()])
sample = set(range(11))

result = sample.difference(set1, set2, set3)

result = list(result)
result.sort()
print(*result)
