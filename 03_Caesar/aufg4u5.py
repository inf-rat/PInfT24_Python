# Funktionsdefinitionen
def verschiebung(buchstabe, schluessel):
    zahl = ord(buchstabe)
    neueZahl = zahl + schluessel
    if neueZahl > 90:
        neueZahl -= 26
    if neueZahl < 65:
        neueZahl += 26
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

def verschluesselung(text, schluessel):
    result = ""
    for buchstabe in text:
        result += verschiebung(buchstabe, schluessel)
    return result

def entschluesselung(text, schluessel):
    return verschluesselung(text, -schluessel)

# Funktionsaufrufe
print(verschluesselung('ASTERIX', 3))
print(entschluesselung('DVWHULA', 3))
