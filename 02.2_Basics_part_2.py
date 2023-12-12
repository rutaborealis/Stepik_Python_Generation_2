# 2.2
# 2.2.1
dots = [tuple(input().split()) for _ in range(int(input()))]
quarter1 = 0
quarter2 = 0
quarter3 = 0
quarter4 = 0

for dot in dots:
    if int(dot[0]) > 0 and int(dot[1]) > 0:
        quarter1 += 1
    elif int(dot[0]) < 0 and int(dot[1]) > 0:
        quarter2 += 1
    elif int(dot[0]) < 0 and int(dot[1]) < 0:
        quarter3 += 1
    elif int(dot[0]) > 0 and int(dot[1]) < 0:
        quarter4 += 1

print(f'Первая четверть: {quarter1} \n'
      f'Вторая четверть: {quarter2} \n'
      f'Третья четверть: {quarter3} \n'
      f'Четвертая четверть: {quarter4}')

# 2.2.2
numbers = [int(i) for i in input().split()]
count = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1

print(count)

# 2.2.3
numbers = [int(i) for i in input().split()]

for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(*numbers)

# 2.2.4
numbers = [int(i) for i in input().split()]
numbers.insert(0, numbers.pop())
print(*numbers)

# 2.2.5
numbers = [int(i) for i in input().split()]
count = 1

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        count += 1

print(count)

# 2.2.6
numbers = [int(input()) for _ in range(int(input()))]
product = int(input())
flag = False

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if (i != j) and (numbers[i] * numbers[j] == product):
            flag = True
            break

if flag:
    print('ДА')
else:
    print('НЕТ')

# 2.2.7
a, b = input(), input()

vars = ['камень камень', 'ничья', 'ножницы ножницы', 'ничья',
        'камень ножницы', 'Тимур', 'ножницы камень', 'Руслан',
        'бумага бумага', 'ничья', 'бумага камень', 'Тимур',
        'камень бумага', 'Руслан', 'ножницы бумага', 'Тимур',
        'бумага ножницы', 'Руслан']

print(vars[vars.index(a + ' ' + b) + 1])

# 2.2.8
a, b = input(), input()

vars = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
        'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
        'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
        'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
        'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
        'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
        'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
        'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
        'Спок-ящерица': 'Руслан'}

print(vars[(a + '-' + b)])

# 2.2.9
str = input().split('О')
if len(str) != 0:
    print(len(max(str)))
else:
    print('0')

# 2.2.10
import re

refrigerators = [(input().lower()).strip() for _ in range(int(input()))]

for i in refrigerators:
    if re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', i):
        print(refrigerators.index(i) + 1, end=' ')

# 2.2.11
word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()
