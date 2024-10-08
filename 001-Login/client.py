import requests
import time

# URL del endpoint de login
url = "http://127.0.0.1:5000/login"

# Datos del usuario para enviar en la petición POST
data = {
    'username': 'user', # Cambia esto por el usuario que quieras
    'password': '1234'  # Cambia esto por la contraseña que quieras
}

# Función para enviar la petición POST al servidor
def send_post_request():
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"Login request successful: {response.text}")
        else:
            print(f"Login request failed: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Enviar las peticiones POST constantemente en intervalos de 5 segundos
while True:
    send_post_request()
    time.sleep(5)  # Espera 5 segundos antes de la próxima petición
