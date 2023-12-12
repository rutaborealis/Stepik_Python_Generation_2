# 12.2
import random
import string

# 12.2.1
def generate_ip():
    ip = []

    for _ in range(4):
        ip.append(str(random.randint(0, 255)))

    return '.'.join(ip)

# 12.2.2
def generate_index():
    # LetterLetterNumber_NumberLetterLetter
    letters = string.ascii_uppercase
    numbers = list(range(0, 100))

    index = f'{random.choice(letters) + random.choice(letters) + str(random.choice(numbers))}_' \
            f'{str(random.choice(numbers)) + random.choice(letters) + random.choice(letters)}'

    return index

# 12.2.3
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

random.shuffle(matrix)

# 12.2.4
lottery_tickets = set()

while len(lottery_tickets) < 100:
    ticket = random.randint(1000000, 9999999)
    lottery_tickets.add(ticket)

for ticket in lottery_tickets:
    print(ticket)

# 12.2.5
word = list(input())
random.shuffle(word)
print(''.join(word))

# 12.2.6
matrix = [[0] * 5 for _ in range(5)]
numbers = list(range(1, 76))
random.shuffle(numbers)
index = 0

for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            matrix[i][j] = 0
        else:
            matrix[i][j] = numbers[index]
            index +=1

for i in range(5):
    for j in range(5):
        print(str(matrix[i][j]).ljust(3), end='')
    print()

# 12.2.7
students = [input() for _ in range(int(input()))]
friends = students[:]

for student in students:
    while True:
        friend = random.choice(friends)
        if student != friend:
            print(student, '-', friend)
            friends.remove(friend)
            break

# 12.2.8
list_symbols_all = string.ascii_letters+string.digits
list_symbols= list_symbols_all.replace('l','').replace('I','').replace('1','').replace('o','').replace('O','').replace('0','')

n, m = int(input()), int(input())

def generate_password(length):
    for _ in range(length):
        symbol = random.choice(list_symbols)
        print(symbol, end='')

def generate_passwords(count, length):
    for _ in range(count):
        generate_password(length)
        print()

generate_passwords(n, m)

# 12.2.9
digits = string.digits.replace('0', '').replace('1', '')
lowercases = string.ascii_lowercase.replace('l', '').replace('o', '')
uppercases = string.ascii_uppercase.replace('I', '').replace('O', '')

n, m = int(input()), int(input())

def generate_password(length):
    print(random.choice(uppercases), end='')
    print(random.choice(digits), end='')
    print(random.choice(lowercases), end='')

    for _ in range(length - 3):
        symbol = random.choice(uppercases + lowercases + digits)
        print(symbol, end='')

def generate_passwords(count, length):
    for _ in range(count):
        generate_password(length)
        print()

generate_passwords(n, m)
