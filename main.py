from Elmor_Marketplace.clientes import Cliente

print("¡ElmorPlus!")


def menu_principal():
    print("\n** MENÚ PRINCIPAL **")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cliente.registrarse()
        menu_usuario()
    elif opcion == "2":
        cliente.iniciar_sesion()
        menu_usuario()
    elif opcion == "3":
        print("Gracias por usar ElmorPlus. ¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_principal()


def menu_usuario():
    print("\n** ELMOR PLUS **")
    print("1. Actualizar estado")
    print("2. Buscar amigo")
    print("3. Publicar producto")
    print("4. Buscar producto")
    print("5. Cerrar sesión")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cliente.publicar_estado()
        menu_usuario()
    elif opcion == "2":
        cliente.buscar_amigo()
        menu_usuario()
    elif opcion == "3":
        cliente.publicar_producto()
        menu_usuario()
    elif opcion == "4":
        cliente.buscar_producto()
        menu_usuario()
    elif opcion == "5":
        print("Sesión cerrada. Regresando al menú principal.")
        menu_principal()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_usuario()


cliente = Cliente("", "", "", "", "")

menu_principal()
