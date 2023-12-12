# 8.5
# 8.5.1
list_sets = [set(input().lower()) for _ in range(int(input()))]

for item in list_sets:
    print(len(item))

# 8.5.2
list_sets = [set(input().lower()) for _ in range(int(input()))]
result = set()

for item in list_sets:
    for char in item:
        result.add(char)

print(len(result))

# 8.5.3
text = input().lower().split()
result = set()

for word in text:
    result.add(word.strip('.,;:-?!'))

print(len(result))

# 8.5.4
arr = [int(i) for i in input().split()]
s = set()

for elem in arr:
    if elem not in s:
        s.add(elem)
        print('NO')
    else:
        print('YES')
