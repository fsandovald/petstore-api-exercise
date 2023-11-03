import api
import models

# Creamos un usuario
user_id = api.create_user("user", "password")

# Recuperamos los datos del usuario
user_data = api.get_user(user_id)

# Obtenemos las mascotas vendidas
pets = api.get_pets_by_status("sold")

# Creamos una lista de mascotas
pets_list = models.PetsList(pets)

# Imprimimos el nombre de las mascotas
for pet in pets_list.pets:
    print(pet.name)
