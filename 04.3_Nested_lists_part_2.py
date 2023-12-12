# 4.3
# 4.3.1
n = int(input())

nested_list = [[i for i in range(1, n + 1)] for _ in range(n)]

for row in nested_list:
    print(row)

# 4.3.2
n = int(input())

nested_list = [[j + 1 for j in range(i + 1)] for i in range(n)]

for row in nested_list:
    print(row)

# 4.3.3
def pascal(n):
    pascal_list = []
    for i in range(n + 1):
        pascal_list.append([1 for j in range(i + 1)])
    for i in range(n + 1):
        for j in range(1, i):
            pascal_list[i][j] = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
    print(pascal_list[n])


pascal(int(input()))

# 4.3.4
n = int(input())
triangle = []

for i in range(n + 1):
    triangle.append([1] + [0] * n)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

for i in range(n):
    for j in range(0, i + 1):
        print(triangle[i][j], end=' ')
    print()

# 4.3.5
char_list = []
a = []

for char in input().split():
    if len(a) == 0:
        a.append(char)
    else:
        if a[len(a) - 1] == char:
            a.append(char)
        else:
            char_list.append(a[:])
            a.clear()
            a.append(char)
if a:
    char_list.append(a[:])

print(char_list)

# 4.3.6
string = input().split()
n = int(input())
result = []
temp = []

for char in string:
    temp.append(char)
    if len(temp) == n:
        result.append(temp[:])
        temp.clear()

if len(string) % n != 0:
    result.append(temp[:])

print(result)

# 4.3.7
string = input().split()
result = [[]]
temp = []

for i in range(len(string)):
    for j in range(len(string)):
        temp = string[j:i + j + 1]
        if len(temp) == i + 1:
            result.append(temp)

print(result)