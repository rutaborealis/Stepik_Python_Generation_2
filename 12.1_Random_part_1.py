# 12.1
import random

# 12.1.1
coin = [random.randint(0, 1) for _ in range(int(input()))]

for i in coin:
    if i == 0:
        print('Орел')
    else:
        print('Решка')

# 12.1.2
сube = [random.randint(1, 6) for _ in range(int(input()))]

for i in сube:
    print(i)

# 12.1.3
password = []

for _ in range(int(input())):
    choice = random.randint(0, 1)
    if choice == 0:
        password.append(chr(random.randint(65, 90)))
    else:
        password.append(chr(random.randint(97, 122)))

print(''.join(password))

# 12.1.4
lottery_ticket = [random.randint(1, 49) for _ in range(7)]
lottery_ticket.sort()
print(*lottery_ticket)
