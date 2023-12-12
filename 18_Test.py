# 18 Test
# 18.1
filename = input()

with open(filename, encoding='utf-8') as file:
    content = file.readlines()
    count = len(content)
    print(count)

# 18.2
with open('ledger.txt', encoding='utf-8') as file:
    summary = 0

    for line in file:
        summary += int(line[1:].strip())

    print(f'${summary}')

# 18.3
with open('grades.txt', encoding='utf-8') as file:
    count = 0

    for line in file:
        students = line.strip().split(' ')
        ball_1 = int(students[1])
        ball_2 = int(students[2])
        ball_3 = int(students[3])
        if ball_1 >= 65 and ball_2 >= 65 and ball_3 >= 65:
            count += 1

    print(count)

# 18.4
with open('words.txt', encoding='utf-8') as file:
    content = file.read().split(' ')
    arr_length = [len(word) for word in content]
    m = max(arr_length)
    res = list(filter(lambda w: len(w) == m, content))
    print(*res, sep='\n')

# 18.5
filename = input()

with open(filename, encoding='utf-8') as file:
    content = file.readlines()
    count = len(content)

    if count < 10:
        for s in content:
            print(s, end='')
    else:
        res = content[-10:]
        for s in res:
            print(s, end='')

# 18.6
filename = input()

with open(filename, encoding='utf-8') as file, open('forbidden_words.txt', encoding='utf-8') as forbidden_file:
    arr_forbidden = forbidden_file.read().split(' ')

    for line in file:
        s_lower = line.lower()
        for forbidden_word in arr_forbidden:
            s_lower = s_lower.replace(forbidden_word, '*' * len(forbidden_word))
        for i, v in enumerate(s_lower):
            if v == '*':
                print('*', end='')
            else:
                print(line[i], end='')

# 18.7
import string

translate_dict = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
    'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
    'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
    'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
    'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
}

with open('cyrillic.txt', encoding='utf-8') as file, open('transliteration.txt', 'w', encoding='utf-8') as tr_file:
    for line in file:
        for ch in line:
            if ch in string.printable:
                print(ch, end='')
            else:
                print(translate_dict[ch], end='')

# 18.8
input_file = input()

with open(input_file, encoding='utf-8') as file:
    arr_content = file.readlines()
    result = []

    for ind, line in enumerate(arr_content):
        if (arr_content[ind].startswith('def ') and ind == 0) or \
                (arr_content[ind].startswith('def ') and not arr_content[ind - 1].startswith('#')):
            pos_1 = line.index(' ') + 1
            pos_2 = line.index('(')
            func = line[pos_1:pos_2]
            result.append(func)
    if len(result) == 0:
        print("Best Programming Team")
    else:
        print(*result, sep='\n')