# 8.2
# 8.2.1
n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
out = (k - y) + m + (n - x) + z
print(out)

# 8.2.2
n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(
    input()), int(input())

l1 = n + m - t - x
l2 = n + k - t - z
l3 = m + k - t - y

book_n = n - t - l1 - l2
book_m = m - t - l1 - l3
book_k = k - t - l2 - l3

#  Прочитали только одну книгу.
print(book_n + book_m + book_k)

# Прочитали две книги.
print(l1 + l2 + l3)

# Не прочитали ни одной из рекомендованных книг.
print(a - (book_n + book_m + book_k + l1 + l2 + l3 + t))
