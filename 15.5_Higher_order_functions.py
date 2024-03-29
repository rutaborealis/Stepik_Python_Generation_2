# 15.5
import functools

# 15.5.1
def round_two(item):
    return round(item, 2)

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013,
           23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

print(*map(round_two, numbers), sep='\n')

# 15.5.2
def predicat(item):
    return 99 < item < 1000 and item % 5 == 2

def cube(item):
    return item ** 3

numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424,
           1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488,
           668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434,
           1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669,
           105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175,
           959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018,
           1274, 387, 120, 340, 963, 832, 1127]

print(*map(cube, filter(predicat, numbers)), sep='\n')

# 15.5.3
def square_sum(x, y):
    return x + y ** 2

def square(num):
    return num ** 2

numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
           11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36,
           72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35,
           7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

total_reduce = functools.reduce(square_sum, numbers, 0)
total_map_filter= sum(map(square, numbers))

print(total_reduce)
# print(total_map_filter)

# 15.5.4
def predicat(item):
    return 9 < abs(item) < 100 and item % 7 == 0

def square(item):
    return item ** 2

numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270,
           219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35,
           152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
           187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35,
           211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2,
           79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234,
           10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

print(sum(map(square, filter(predicat, numbers))))

def func_apply(function, items):
    arr = []
    for item in items:
        res = function(item)
        arr.append(res)
    return arr

def add3(x):
    return x + 3

def mul7(x):
    return x * 7

print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))
