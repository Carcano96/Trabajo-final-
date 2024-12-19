import random


total = 0
num_usuario = ""

while num_usuario != "salir":
    num_usuario = input("Introduce piedra, papel o tijera (o 'salir' para terminar): ").lower()

    if num_usuario == "salir":
        print("Fin del juego.")
    elif num_usuario not in ["piedra", "papel", "tijera"]:
        print("Opción no válida. Intenta de nuevo.")
    else:
        num_pc = random.randint(1, 3)
        if num_pc == 1:
            eleccion_pc = "piedra"
        elif num_pc == 2:
            eleccion_pc = "papel"
        else:
            eleccion_pc = "tijera"

        print(f"La máquina eligió: {eleccion_pc}")

        if num_usuario == eleccion_pc:
            print("¡Empate!")
        elif (num_usuario == "piedra" and eleccion_pc == "tijera") or \
                (num_usuario == "papel" and eleccion_pc == "piedra") or \
                (num_usuario == "tijera" and eleccion_pc == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

        total += 1
        print(f"Total de juegos jugados: {total}")
