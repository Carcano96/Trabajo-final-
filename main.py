import time
import random
import os
from Juego_Millonario import preguntas


def mostrar(pregunta):
    print(f"PREGUNTA: {pregunta['question']}")
    opciones = [pregunta['correct_answer']] + pregunta['incorrect_answers']
    random.shuffle(opciones)
    for i, opcion in enumerate(opciones):
        print(f"OPCION {i + 1}: {opcion}")
    return opciones

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def juego():
    print('Bienvenido al juego "QUIEN QUIERE SER MILLONARIO"')
    jugador = input("¿CÓMO TE LLAMAS? ")
    print(f"{jugador}, ¡PREPÁRATE PARA RESPONDER PREGUNTAS!")

    puntuacion = 0
    preguntas_lista = preguntas()
    comodin = {'disponible': True}

    for indice, pregunta in enumerate(preguntas_lista):
        print(f"\nPregunta {indice + 1}. Puntuación actual: {puntuacion} puntos")
        opciones = mostrar(pregunta)

        if comodin['disponible']:
            print("ESCRIBE 'COMODÍN' PARA SALTAR ESTA PREGUNTA SI LO DESEAS")

        respuesta = input("TU RESPUESTA (1-4 O ESCRIBE 'SALIR' PARA PLANTARTE): ").lower()

        if respuesta == 'comodín' and comodin['disponible']:
            print("¡HAS USADO EL COMODÍN PARA SALTAR ESTA PREGUNTA!")
            comodin['disponible'] = False
            continue

        if respuesta == 'salir':
            print(f"{jugador}, has decidido plantarte con {puntuacion} puntos.")
            time.sleep(3)
            limpiar()
            break

        try:
            elegido = int(respuesta) - 1
            if opciones[elegido] == pregunta['correct_answer']:
                print("¡RESPUESTA CORRECTA!")
                puntuacion += 1
                time.sleep(1)
                if puntuacion == 15:
                    print("¡FELICIDADES, HAS GANADO EL JUEGO CON 15 PUNTOS!")
                    break
            else:
                print(f"¡INCORRECTO! La respuesta correcta era: {pregunta['correct_answer']}")
                print(f"TU PUNTUACIÓN FINAL ES: {puntuacion}")
                puntuacion = 0
                break
        except (ValueError, IndexError):
            print("OPCIÓN NO VÁLIDA. TERMINA EL JUEGO.")
            break

    print("FIN DEL JUEGO")

juego()


