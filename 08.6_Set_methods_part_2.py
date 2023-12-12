# 8.6
# 8.6.1
A, B = set(input().split()), set(input().split())
result = A.intersection(B)
print(len(result))

# 8.6.2
A, B = set(input().split()), set(input().split())
result = [int(i) for i in A.intersection(B)]
result.sort()
print(*result)

# 8.6.3
A, B = set(input().split()), set(input().split())
result = [int(i) for i in A.difference(B)]
result.sort()
print(*result)

# 8.6.4
list_sets = [set(input()) for _ in range(int(input()))]
result = list_sets[0]

for set in list_sets:
    result = result.intersection(set)

result = [int(i) for i in result]
result.sort()

print(*result)