frase=input("introduce una frase")
vocales="aeiouAEIOU"
num_vocales=0
num_consonantes=0
for caracter in frase:
    if caracter.isalpha():
        if caracter in vocales:
            num_vocales +=1
        else:
            num_consonantes +=1
print(f"En la frase hay {num_vocales} vocales y {num_consonantes} consonantes.")

