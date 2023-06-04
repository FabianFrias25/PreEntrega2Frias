import json

class Cliente:
    def __init__(self, user, email, password, name, last_name):
        self.user = user
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def registrarse(self):
        print("**REGISTRARSE**\n")
        newdata = {
            'user': input("Nombre de usuario (sin espacio, por ejemplo: name_lastnane#): ").lower(),
            'email': input("Correo: "),
            'password': input("Contraseña: "),
            'name': input("Nombre: "),
            'lastName': input("Apellido: ")
        }
        with open("Elmor_Marketplace/usuarios.json", "r") as file:
            data = json.load(file)
        data["usuarios"].append(newdata)
        with open("Elmor_Marketplace/usuarios.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Registro exitoso.")

    def iniciar_sesion(self):
        print("**INICIAR SESION**\n")
        username = input("Nombre de usuario: ").lower()
        password = input("Contraseña: ")
        with open("Elmor_Marketplace/usuarios.json", "r") as file:
            data = json.load(file)
            encontrado = False
            for user in data["usuarios"]:
                if user["user"] == username and user["password"] == password:
                    print(f"Bienvenido a Elmor Plus @{username}")
                    encontrado = True
                    break
            if not encontrado:
                print("Usuario no encontrado")

    def publicar_estado(self):
        estado = input("EXPRESATE AL MUNDO: ")
        print(f'@{self.user} dijo: "{estado}"')


    def buscar_amigo(self):
        import random
        numero_aleatorio = random.randint(1, 5000)
        numero_aleatorio2 = random.randint(0, 2000)
        with open("Elmor_Marketplace/usuarios.json", "r") as file:
            data = json.load(file)
            buscar = input("Buscar persona amigo por nombre de usuario: ").lower()
            for usuario in data["usuarios"]:
                if usuario["user"] == buscar:
                    print("Usuario encontrado:")
                    print(f'@{buscar}\n{numero_aleatorio} "Amigos - {numero_aleatorio2} Publicaciones"')
                    break
            else:
                print("Amigo no encontrado")


    def publicar_producto(self):
        print("**ELMOR MARKETPLACE**\n")
        tipo = input("Ingrese el tipo de mercadería: ").lower()
        marca = input("Ingrese la marca o cosa: ")
        condicion = input("Ingrese la condición (nuevo o usado): ")
        tiempo_uso = int(input("Ingrese el tiempo de uso en años: "))
        precio = float(input("Ingrese el precio: "))

        producto = f"{tipo}|{marca}|{condicion}|{tiempo_uso}|{precio}"

        with open("Elmor_Marketplace/ListaDeProductos.txt", "a") as file:
            file.write(producto + "\n")

        print("Producto publicado exitosamente.")

    def buscar_producto(self):
        print("**ELMOR MARKETPLACE**\n")
        with open("Elmor_Marketplace/ListaDeProductos.txt", "r") as file:
            productos = file.readlines()

        tipo_buscar = input("Ingrese el tipo de mercadería a buscar: ").lower()

        encontrados = []

        for producto in productos:
            datos = producto.strip().split("|")
            tipo = datos[0]

            if tipo == tipo_buscar:
                encontrados.append(producto)

        if len(encontrados) > 0:
            print("Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos que buscas.")