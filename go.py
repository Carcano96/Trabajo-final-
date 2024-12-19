import requests
import time
import os
import random

def obtener_preguntas(numero=15):
    url = f"https://opentdb.com/api.php?amount={numero}&difficulty=easy&type=multiple"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos['results']

def mostrar_pregunta(pregunta):
    print(f"Pregunta: {pregunta['question']}")
    opciones = [pregunta['correct_answer']] + pregunta['incorrect_answers']
    random.shuffle(opciones)
    for i, opcion in enumerate(opciones):
        print(f"Opción {i + 1}: {opcion}")
    return opciones

def limpiar_pantalla():
    os.system('cls')

def juego_trivia():
    print("¡Bienvenido al juego de trivia!")
    nombre_jugador = input("¿Cómo te llamas? ")
    print(f"{nombre_jugador}, ¡prepárate para responder preguntas!\n")

    puntuacion = 0
    preguntas = obtener_preguntas()
    comodin = {'disponible': True}

    for indice, pregunta in enumerate(preguntas):
        print(f"\nPregunta {indice + 1}. Puntuación actual: {puntuacion} puntos")
        opciones = mostrar_pregunta(pregunta)

        if comodin['disponible']:
            print("Escribe 'COMODÍN' para saltar esta pregunta si lo deseas.")

        respuesta = input("Tu respuesta (1-4 o escribe 'SALIR' para plantarte): ").lower()

        if respuesta == 'comodín' and comodin['disponible']:
            print("¡Has usado el comodín para saltar esta pregunta!")
            comodin['disponible'] = False
            continue

        if respuesta == 'salir':
            print(f"{nombre_jugador}, has decidido plantarte con {puntuacion} puntos.")
            time.sleep(2)
            limpiar_pantalla()
            break

        try:
            respuesta_elegida = int(respuesta) - 1
            if opciones[respuesta_elegida] == pregunta['correct_answer']:
                print("¡Respuesta correcta!")
                puntuacion += 1
                time.sleep(1)
                if puntuacion == 15:
                    print("¡Felicidades! Has ganado el juego con 15 puntos.")
                    break
            else:
                print(f"¡Incorrecto! La respuesta correcta era: {pregunta['correct_answer']}")
                print(f"Tu puntuación final es: {puntuacion}")
                puntuacion = 0
                break

        except (ValueError, IndexError):
            print("Opción no válida. Termina el juego.")
            break

    print("\nFIN DEL JUEGO")

# Llamada principal para iniciar el juego
juego_trivia()