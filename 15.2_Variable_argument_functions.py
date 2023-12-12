# 15.2
# 15.2.1
def count_args(*args):
    return len(args)

# 15.2.2
def sq_sum(*args):
    output = [i ** 2 for i in args]
    return sum(output)

# 15.2.3
def mean(*args):
    output = [i for i in args if type(i) in (int, float)]
    if len(output) == 0:
        return 0
    else:
        return sum(output) / len(output)

# 15.2.4
def greet(name, *args):
    if len(args) == 0:
        ends = name
    elif len(args) == 1:
        ends = name + ' and ' + args[0]
    else:
        ends = name + ' and ' + ' and '.join(args)
    return 'Hello, ' + ends + '!'

# 15.2.5
def print_products(*args):
    output = [i for i in args if type(i) is (str) and len(i) > 0]
    if len(output) == 0:
        print('Нет продуктов')
    else:
        for i in range(len(output)):
            print(f'{i + 1}) {output[i]}')

# 15.2.6
def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(f'{key}: {value}')
