# 15.8
import functools

# 15.8.1
func = lambda x: x % 19 == 0 or x % 13 == 0

# 15.8.2
func = lambda x: x[0].lower() == x[-1].lower() == 'a'

# 15.8.3
is_non_negative_num = lambda s: set(s).issubset(set('.0123456789')) and s.count('.') < 2

# 15.8.4
is_num = lambda s: set(s).issubset(set('-.0123456789')) and s.count('.') < 2 and s[1:].count('-') == 0

# 15.8.5
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
         'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
         'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
         'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
         'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

filter_result = filter(lambda x: len(x) == 6, words)
print(*sorted(filter_result))

# 15.8.6
numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80,
           93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
           53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94,
           37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

filter_result = filter(lambda x: x % 2 == 0 or (x % 2 == 1 and x <= 47), numbers)
map_result = map(lambda x: x // 2 if x % 2 == 0 else x, filter_result)
print(*map_result)

# 15.8.7
data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
        (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

sort_data = sorted(data, key=lambda item: item[1][-1], reverse=True)
for item in sort_data:
    print(item[1] + ':', item[0])

# 15.8.8
data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

data.sort()

sorted_data = sorted(data, key=lambda x: len(x))
print(*sorted_data)

# 15.8.9
mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
              'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
              2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
              'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
              'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet',
              859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth',
              'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage',
              'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552,
              1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

print(max(mixed_list, key=lambda x: x if type(x)==int else 0))

# 15.8.10
mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76,
              70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort',
              13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80,
              'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon',
              'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt',
              'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]

sorted_list_1 = sorted(mixed_list, key=lambda x: x if type(x) == int else 0)
sorted_list_2 = sorted(sorted_list_1, key=lambda x: x if type(x) == str else '')
print(*sorted_list_2)

# 15.8.11
rgb = [int(i) for i in input().split()]
invRGB = list(map(lambda x: 255 - x, rgb))
print(*invRGB)

# 15.8.12
import functools

coefficients = [int(i) for i in input().split()]
x = int(input())

def evaluate(coefficients, x):
    arr = list(
        map(lambda c, z, n: c * z ** n, coefficients, [x] * len(coefficients), range(len(coefficients) - 1, -1, -1)))
    reduce_result = functools.reduce(lambda x, y: x + y, arr, 0)
    print(reduce_result)

evaluate(coefficients, x)