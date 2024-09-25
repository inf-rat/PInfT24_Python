from random import randint

def make_rand_list(n: int, low: int, high: int) -> list[int]:
    """
    Erzeugt eine Liste der Länge n von zufälligen ganzen Zahlen zwischen low und high.
    """
    lst = []
    for i in range(n):
        lst.append(randint(low, high))
    return lst

# Hier werden von euch weitere Funktionsdefinitionen geschrieben.

# Hier werden die geschriebenen Funktionen getestet:
test_list = make_rand_list(10, 0, 99)
print(test_list)