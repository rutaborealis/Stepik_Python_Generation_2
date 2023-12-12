# 10.3
# 10.3.1
n = 16
result = {}

for i in range(1, n):
    result[i] = i ** 2

# 10.3.2
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = {}

result = dict1.copy()
for key in dict2:
    if key in result:
        result[key] = result.get(key) + dict2[key]
    else:
        result[key] = dict2[key]

# 10.3.3
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for char in text:
    result[char] = result.get(char, 0) + 1

# 10.3.4
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
text_list = s.split()
text_dict = {}

for word in text_list:
    text_dict[word] = text_dict.get(word, 0) + 1

max_value = max(text_dict.values())

result = {}
for key, value in text_dict.items():
    if value == max_value:
        result[key] = value

print(min(result))

# 10.3.5
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for i in range(len(pets)):
    key = pets[i][1:]
    if key not in result:
        result[key] = [pets[i][0]]
    else:
        result[key].append(pets[i][0])

# 10.3.6
text_list = [word.strip('.,"\'-?:!;()').lower() for word in input().split()]
text_dict = {}

for word in text_list:
    text_dict[word] = text_dict.get(word, 0) + 1

min_value = min(text_dict.values())

result = {}
for key, value in text_dict.items():
    if value == min_value:
        result[key] = value

print(min(result))

# 10.3.7
text = input().split()
result = {}

for word in text:
    result[word] = result.get(word, 0) + 1

for key, value in result.items():
    if value > 1:
        for i in range(value):
            pos = text.index(key)
            text[pos] = key + '_' + str(i)

result_string = ' '.join(text)
result_string = result_string.replace('_0', '')

print(result_string)
