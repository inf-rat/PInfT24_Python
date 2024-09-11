def summe_iterativ(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def summe_rekursiv(n):
    if n <= 0:
        return 0
    else:
        return n + summe_rekursiv(n - 1)

print(summe_rekursiv(5))
