import requests
from Modelos.users import User
from Auxiliares.construir_url import url_servicio

def obtener_usuarios_api():
    direccion = url_servicio("users")  # reutilizacion de la funcion url_de servicio

    try:
        respuesta = requests.get(direccion)
        print(respuesta)
        respuesta.raise_for_status()

        if respuesta.status_code == 200:
            return respuesta.json()
    except requests.exceptions.Timeout:
        print("El tiempo de espera para obtener la respuesta ha expirado.")

    except requests.exceptions.ConnectionError:
        print("No se pudo establecer comunicación con el servidor.")

    except requests.exceptions.RequestException as error:
        print(f"Se produjo un error al procesar la solicitud: {error}")