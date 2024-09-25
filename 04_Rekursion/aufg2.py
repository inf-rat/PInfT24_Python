def summe_iterativ(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print(summe_iterativ(5))