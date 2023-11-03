import requests

def create_user(username, password):
    """
    Crea un usuario en la API.

    Args:
        username: El nombre de usuario.
        password: La contraseña.

    Returns:
        El ID del usuario.
    """

    url = "https://petstore.swagger.io/v2/user"
    data = {
        "username": username,
        "password": password,
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception(f"Error al crear el usuario: {response.status_code}")

def get_user(user_id):
    """
    Recupera los datos del usuario.

    Args:
        user_id: El ID del usuario.

    Returns:
        Los datos del usuario.
    """

    url = f"https://petstore.swagger.io/v2/user/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al recuperar los datos del usuario: {response.status_code}")

def get_pets_by_status(status):
    """
    Obtiene las mascotas con el estado especificado.

    Args:
        status: El estado de las mascotas.

    Returns:
        Una lista de mascotas.
    """

    url = f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener las mascotas: {response.status_code}")
