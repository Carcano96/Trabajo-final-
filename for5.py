
nombre = input("Introduce tu nombre: ")


cantidad_letras = len(nombre)


if cantidad_letras % 2 == 0:
    par_impar = "par"
else:
    par_impar = "impar"

print(f"El nombre: {nombre} – Contiene {cantidad_letras} letras y es {par_impar}.")