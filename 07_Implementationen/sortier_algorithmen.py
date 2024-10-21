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


# Test Bubblesort:
print("Test Bubblesort:")
test_list1 = make_rand_list(6, 0, 99)
print("sortiert:   ", test_list1)
bubblesort(test_list1)
print("unsortiert: ", test_list1, "\n")

# Test Selection-Sort:
print("\nTest Selection-Sort:")
test_list2 = make_rand_list(6, 0, 99)
print("sortiert:   ", test_list2)
sorted_list = selection_sort(test_list2)
print("unsortiert: ", sorted_list)

# Test Selection-Sort in place:
print("\nTest Selection-Sort in place:")
test_list3 = make_rand_list(6, 0, 99)
print("sortiert:   ", test_list3)
selection_sort_inplace(test_list3)
print("unsortiert: ", test_list3)
