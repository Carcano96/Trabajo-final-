import random


numero_secreto = random.randint(1, 100)

intentos = 0

print("¡Bienvenido al juego de adivinar el número!")
print("He pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?")


while True:
    numero_usuario = input("Introduce un número: ")


    if numero_usuario.isdigit():
        numero_usuario = int(numero_usuario)
        intentos += 1


        if numero_usuario < numero_secreto:
            print("El número es mayor. ¡Sigue intentando!")
        elif numero_usuario > numero_secreto:
            print("El número es menor. ¡Sigue intentando!")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
          
    else:
        print("Por favor, introduce un número válido.")


