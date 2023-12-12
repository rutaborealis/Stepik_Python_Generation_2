# 10.4
# 10.4.1
coder_dictionary = {}
for _ in range(int(input())):
    key, value = input().split(': ')
    coder_dictionary[key.lower()] = value

for _ in range(int(input())):
    search = input().lower()
    if search in coder_dictionary:
        print(coder_dictionary[search])
    else:
        print('Не найдено')

# 10.4.2
word1, word2 = input(), input()
dict1 = {}
dict2 = {}

for i in word1:
    dict1[i] = dict1.get(i, 0) + 1

for j in word2:
    dict2[j] = dict2.get(j, 0) + 1

if dict1 == dict2:
    print('YES')
else:
    print('NO')

# 10.4.3
sentence1 = [word.strip('.,"\'-?:!;()').lower() for word in input().split()]
sentence2 = [word.strip('.,"\'-?:!;()').lower() for word in input().split()]
dict1 = {}
dict2 = {}

for word in sentence1:
    for i in word:
        dict1[i] = dict1.get(i, 0) + 1

for word in sentence2:
    for j in word:
        dict2[j] = dict2.get(j, 0) + 1

if dict1 == dict2:
    print('YES')
else:
    print('NO')

# 10.4.4
synonym_dictionary = {}
for _ in range(int(input())):
    key, value = input().split(' ')
    synonym_dictionary[key] = value

search = input()

for key, value in synonym_dictionary.items():
    if search == key:
        print(value)
    elif search == value:
        print(key)

# 10.4.5
n = int(input())
countries_dictionary = {}

for _ in range(n):
    country = [object for object in input().split()]
    for i in range(1, len(country)):
        countries_dictionary[country[i]] = country[0]

m = int(input())
for _ in range(m):
    search = input()
    if search in countries_dictionary.keys():
        print(countries_dictionary[search])

# 10.4.6
n = int(input())
dictionary = {}

for _ in range(n):
    item = input().lower().split()
    if item[1] not in dictionary:
        dictionary[item[1]] = [item[0]]
    else:
        dictionary[item[1]].append(item[0])

item = [input().lower() for _ in range(int(input()))]
for name in item:
    if name in dictionary:
        print(*dictionary[name], sep=' ')
    else:
        print("абонент не найден")

# 10.4.7
secret = input()
n = int(input())
dictionary = {}

for _ in range(n):
    item = input().split(': ')
    dictionary[int(item[1])] = item[0]

for char in secret:
    print(dictionary[secret.count(char)], end='')
