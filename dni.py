dni_letra = lambda dni: "TRWAGMYFPDXBNJZSQVHLCKE"[dni % 23]


dni = int(input("Introduce el número de tu DNI (sin letra): "))


print(f"La letra de tu DNI es: {dni_letra(dni)}")