from time import time
from random import randint

def make_rand_list(n: int, low: int, high: int) -> list[int]:
    """
    Erzeugt eine Liste der Länge n von zufälligen ganzen Zahlen zwischen low und high.
    """
    lst = []
    for i in range(n):
        lst.append(randint(low, high))
    return lst

# Funktionsdefinitionen:
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def bubblesort(lst):
    n = len(lst)
    while n > 1:
        for j in range(0, n - 1):
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
        n -= 1

def bubblesort_optimized(lst):
    n = len(lst)
    while n > 1:
        ordered = True
        for j in range(0, n - 1):
            if lst[j] > lst[j+1]:
                swap(lst, j, j+1)
                ordered = False
        if ordered: break
        n -= 1

def selection_sort(lst):
    LU = lst.copy()
    LS = []
    while LU != []:
        minpos = 0
        for i in range(1, len(LU)):
            if LU[i] < LU[minpos]:
                minpos = i
        LS.append(LU[minpos])
        LU.pop(minpos)
    return LS


def selection_sort_inplace(lst):
    n = len(lst)
    u = 0
    while u < n - 1:
        minpos = u
        for i in range(u+1, n):
            if lst[i] < lst[minpos]:
                minpos = i
        swap(lst, u, minpos)
        u += 1


test_lst = make_rand_list(1000, 0, 99)
test_copies = []
for i in range(3):
    test_copies.append(test_lst.copy())

start = time()
bubblesort(test_copies[0])
end = time()
print("bubble: ", end - start)

start = time()
selection_sort(test_copies[1])
end = time()
print("select: ", end - start)