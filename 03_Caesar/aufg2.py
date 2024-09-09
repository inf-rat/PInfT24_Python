zeichen = 'T'
schluessel = 10
zahl = ord(zeichen)
neueZahl = zahl + schluessel
if neueZahl > 90:
    neueZahl -= 26
if neueZahl < 65:
    neueZahl += 65
neuesZeichen = chr(neueZahl)
print(neuesZeichen)