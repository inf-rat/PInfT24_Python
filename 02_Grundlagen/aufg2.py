# Aufg. 2a)
username = input("Wie heißt du?: ")
print("Hallo", username, ".")

# Aufg. 2b)
test_string = "PYTHON_IST_KEINE_INSEL"
substrings = []
while test_string:
    substrings.append(test_string[:3])
    test_string = test_string[3:]

for substring in substrings:
     print(substring)