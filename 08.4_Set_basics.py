# 8.4
# 8.4.1
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(min(numbers) + max(numbers))

# 8.4.2
numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
average = sum(numbers) / len(numbers)
print(average)

# 8.4.3
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
sum = 0

for num in numbers:
    sum += num ** 2

print(sum)

# 8.4.4
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
fruits_list = sorted(fruits, reverse=True)
print(*fruits_list, sep='\n')

# 8.4.5
string_set = set(input())
print(len(string_set))

# 8.4.6
string_list = [i for i in input()]

string_set = set(string_list)

if len(string_list) == len(string_set):
    print('YES')
else:
    print('NO')

# 8.4.7
string_list = set([i for i in input() + input()])
sample_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

if string_list == sample_set:
    print('YES')
else:
    print('NO')

# 8.4.8
set1, set2 = set(input()), set(input())

if set1 == set2:
    print('YES')
else:
    print('NO')

# 8.4.9
text_list = [set(i) for i in input().split(' ')]

if text_list[0] == text_list[1] == text_list[2]:
    print('YES')
else:
    print('NO')
