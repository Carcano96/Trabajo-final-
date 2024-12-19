
total = 0
num = int(input("Introduce un número: "))

while num != 0:
    if num >= 10:
        print(f"{num} es positivo y es numero alto")
    elif num <0:
        print(f"{num} es negativo")
    elif 0 < num < 10:
        print(f"{num} está entre 0 y 10 , numero bajo")
    num = int(input("Introduce un número: "))
else:
    print("Fin del programa")

