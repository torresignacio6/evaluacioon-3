import requests
from Funciones import obtener_post
from Funciones.obtener_users import obtener_usuarios_api
from Funciones.fernet import encriptar_texto  # Importamos la función de encriptación

def mostrar_datos(opcion):
    if opcion == '1':
        # Obtener los datos de la API de posts
        posts = obtener_post.obtener_posts_api()

        # Mostrar los datos de las publicaciones
        print("\n--- Publicaciones ---")
        for post in posts:
            print(f"ID: {post['id']}")
            print(f"ID usuario: {post['userId']}")
            print(f"Título: {post['title']}")
            print(f"Cuerpo: {post['body']}")
            print("-" * 20)

    elif opcion == '2':
        # Obtener los datos de la API de usuarios
        usuarios = obtener_usuarios_api()

        # Mostrar los datos de los usuarios
        print("\n--- Usuarios ---")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['name']}")
            print(f"Nombre usuario: {usuario['username']}")
            print(f"Email: {usuario['email']}")
            print(f"Teléfono: {usuario['phone']}")
            print(f"Sitio web: {usuario['website']}")
            print("-" * 20)

    elif opcion == '3':
        encriptar_texto()  # Llamamos a la función de encriptación

    elif opcion == '4':
        print("Saliendo..")
        exit()

    else:
        print("Opción inválida.")

while True:
    opcion = input(
        '''
        (-Presione 1) Para mostrar los POST 
        (-Presione 2) Para mostrar los USERS
        (-Presione 3) Para encriptar un texto 
        (-Presione 4) Para salir
        '''
    )
    mostrar_datos(opcion)
