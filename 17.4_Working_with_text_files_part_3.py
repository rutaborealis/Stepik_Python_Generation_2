# 17.4
import random
import datetime

# 17.4.1
input_text = input()
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(input_text)

# 17.4.2
with open('random.txt', 'w', encoding='utf-8') as file:
    for _ in range(25):
        i = random.randint(111, 777)
        file.write(f'{i}\n')

# 17.4.3
with open('input.txt', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as file2:
    arr_content = file.readlines()

    for i, value in enumerate(arr_content):
        file2.write(f'{i + 1}) {value}')

# 17.4.4
with open('class_scores.txt', encoding='utf-8') as file, open('new_scores.txt', 'w', encoding='utf-8') as file2:
    for line in file:
        arr = line.split(' ')
        ocenka = int(arr[1]) + 5
        if ocenka > 100:
            ocenka = 100
        file2.write(f'{arr[0]} {ocenka}\n')

# 17.4.5
with open('goats.txt', encoding='utf-8') as file, open('answer.txt', 'w', encoding='utf-8') as file2:
    line = file.readline()
    dictionary = dict()

    while line != "GOATS":
        line = file.readline().strip()
        if line != "GOATS":
            dictionary[line] = 0
    total = 0

    for line in file:
        line = line.strip()
        dictionary[line] = dictionary.get(line, 0) + 1
        total += 1

    result = list(filter(lambda item: dictionary[item] * 100 > total * 7, dictionary))
    result.sort()

    for item in result:
        file2.write(item + '\n')

# 17.4.6
n = int(input())
arr_files = [input().strip() for _ in range(n)]

with open('output.txt', 'a', encoding='utf-8') as outputfile:
    for filename in arr_files:
        with open(filename, encoding='utf-8') as inputfile:
            content = inputfile.readlines()
        outputfile.writelines(content)

# 17.4.7
with open('logfile.txt', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as outputfile:
    for line in file:
        content = line.strip().replace(',', '').split(' ')
        time_input = content[2]
        time_output = content[3]

        t1 = datetime.timedelta(hours=int(time_input[:2]), minutes=int(time_input[3:]))
        t2 = datetime.timedelta(hours=int(time_output[:2]), minutes=int(time_output[3:]))
        delta = t2 - t1

        if delta >= datetime.timedelta(hours=1):
            outputfile.write(f'{content[0]} {content[1]}\n')