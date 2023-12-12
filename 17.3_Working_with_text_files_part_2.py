# 17.3
from functools import reduce
import operator
import re
import string
import random

# 17.3.1
with open('text.txt', encoding='utf-8') as file:
    s = file.readline().strip()
    print(s[::-1])

# 17.3.2
with open('data.txt', encoding='utf-8') as file:
    arr = file.readlines()

    for i in range(len(arr)-1, -1, -1):
        print(arr[i].strip())

# 17.3.3
with open('lines.txt', encoding='utf-8') as file:
    arr = [line.strip() for line in file.readlines()]
    arr_len = list(map(lambda x: len(x), arr))
    m = max(arr_len)

    print(*(filter(lambda x: len(x) == m, arr)), sep='\n')

# 17.3.4
with open('numbers.txt', encoding='utf-8') as file:
    for line in file:
        arr = [x.strip() for x in line.split(' ')]
        filter_result = list(filter(lambda x: x.isdigit(), arr))
        print(reduce(operator.add, [int(x) for x in filter_result], 0))

# 17.3.5
with open('nums.txt', encoding='utf-8') as file:
    my_list = [re.findall(r'\d+', line) for line in file.readlines()]
    summary = 0

    for arr in my_list:
        for x in arr:
            summary += int(x)

    print(summary)

# 17.3.6
with open('file.txt', encoding='utf-8') as file:
    num_lines = len(file.readlines())
    file.seek(0)
    content = file.read()
    clean_content = content.replace('.', '').replace(',', '').replace(';', '').replace(':', '').replace('-', '').replace('?', '').replace('!', '').replace('(', '').replace(')', '').replace('"','').replace('\n', ' ')
    arr_words = [w for w in clean_content.split(' ')]

    sum_letters = 0

    for word in arr_words:
        for i in word:
            if i in string.ascii_letters:
                sum_letters += 1

    print("Input file contains:")
    print(f'{sum_letters} letters')
    print(f'{len(arr_words)} words')
    print(f'{num_lines} lines')

# 17.3.7
with open('first_names.txt', encoding='utf-8') as file_f, open('last_names.txt', encoding='utf-8') as file_l:
    first = file_f.readlines()
    last = file_l.readlines()
    arr_first = [x.strip() for x in first]
    arr_last = [x.strip() for x in last]

    for _ in range(3):
        print(random.choice(arr_first), random.choice(arr_last))

# 17.3.8
with open('population.txt', encoding='utf-8') as file:
    arr = [city.strip().split('\t') for city in file.readlines()]
    result = list(filter(lambda x: x[0].startswith('G') and int(x[1]) > 500000, arr))

    for land in result:
        print(land[0])

# 17.3.9
def read_csv():
    result = []

    with open('data.csv', encoding='utf-8') as file:
        headers = [head.strip() for head in file.readline().split(',')]

        for line in file:
            one_line = [l.strip() for l in line.split(',')]
            create_tuple_list = list(zip(headers, one_line))
            dictionary = dict(create_tuple_list)
            result.append(dictionary)

    return result

read_csv()