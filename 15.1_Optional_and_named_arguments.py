# 15.1
# 15.1.1
def matrix(n=1, m=None, value=0):
    if m is None:
        m = n
    output = [[value] * m for _ in range(n)]
    return output
