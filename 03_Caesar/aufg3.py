# Funktionsdefinition
def verschiebung(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl + schluessel
    if neueZahl > 90:
        neueZahl -= 26
    if neueZahl < 65:
        neueZahl += 26
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

# Funktionsaufrufe
print(verschiebung('P', 7))
print(verschiebung('A', 3))
print(verschiebung('T', 10))