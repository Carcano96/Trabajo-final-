usuario="ad"
codigo="12345"
usuario_insertado=""
codigo_insertado=""
while usuario != usuario_insertado and codigo != codigo_insertado:
    usuario_insertado=input("introduce el usuario")
    codigo_insertado=input("introduce la contaseña")

    if usuario == usuario_insertado and codigo == codigo_insertado:
        print("acceso concedido")

    else:
        print("usuario o contraseña incorrectos")