# Funktionsdefinitionen
def verschiebung(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl + schluessel
    if neueZahl > 90:
        neueZahl -= 26
    if neueZahl < 65:
        neueZahl += 26
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

def verschluesselung(text, schluessel):
    result = ""
    for zeichen in text:
        result += verschiebung(zeichen, schluessel)
    return result


# Funktionsaufrufe
print(verschluesselung('ASTERIX', 3))
print(verschluesselung('DVWHULA', -3))