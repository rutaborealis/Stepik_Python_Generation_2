# 11 Test
# 11.1
my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
           'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
           'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

my_dict = {key: [i for i in my_dict[key] if i <= 20] for key in my_dict}

# 11.2
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

emails_lis = []
for domain, list_value in emails.items():
    for username in list_value:
        emails_lis.append(username + "@" + domain)

print(*sorted(emails_lis), sep='\n')

# 11.3
dnk = input()

rnk = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

for nukl in dnk:
    print(rnk[nukl], end='')

# 11.4
words = input().split()

result = {}
for i in words:
    result[i] = result.get(i, 0) + 1

for key, value in result.items():
    for i in range(1, value + 1):
        pos = words.index(key)
        words[pos] = str(i)

result = " ".join(words)

print(result)

# 11.5
def scramble_result(word, language):
    result = 0

    for char in word:
        for item in language:
            if char in item[0]:
                result += item[1]

    return result

word = input().upper()

english = [('AEIOULNSTR', 1),
           ('DG', 2),
           ('BCMP', 3),
           ('FHVWY', 4),
           ('K', 5),
           ('JX', 8),
           ('QZ', 10)]

result = scramble_result(word, english)
print(result)

# 11.6
def build_query_string(params):
    result = []

    for key, value in sorted(params.items()):
        result.append(f"{key}={value}")

    return "&".join(result)

# 11.7
def merge(values):
    dict_merge = {}

    for dictionary in values:
        for key, value in dictionary.items():
            if key not in dict_merge:
                dict_merge[key] = {value}
            else:
                dict_merge[key].add(value)

    return dict_merge

# 11.8
s = {'write': 'W', 'read': 'R', 'execute': 'X'}
dictionary = {}

n = int(input())
for _ in range(n):
    arr = input().split()
    name = arr[0]
    dictionary[name] = []
    for i in range(1, len(arr)):
        dictionary[name].append(arr[i])

m = int(input())
arr_query = []
for _ in range(m):
    query = input().split()
    arr_query.append(query)

for query in arr_query:
    method_execute = query[0]
    file_execute = query[1]
    if s[method_execute] in dictionary[file_execute]:
        print('OK')
    else:
        print('Access denied')

# 11.9
n = int(input())
dictionary = {}

for _ in range(n):
    arr = input().split()
    name = arr[0]
    tovar = arr[1]
    count = int(arr[2])
    if name not in dictionary:
        dictionary[name] = {tovar: count}
    else:
        if tovar not in dictionary[name]:
            dictionary[name][tovar] = count
        else:
            dictionary[name][tovar] = dictionary[name].get(tovar) + count

for dict_name, dict_sales in sorted(dictionary.items()):
    print(f"{dict_name}:")
    for k, v in sorted(dict_sales.items()):
        print(k, v)
