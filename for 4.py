lista=[]
cantidad=input("introduce cuantos nombres ")
for i in range (cantidad):
     nombre = input(f"Introduce el nombre {i + 1}: ")

lista.append(nombre)
print(nombre)