class Pet:
    """
    Representa una mascota.

    Args:
        id: El ID de la mascota.
        name: El nombre de la mascota.
        status: El estado de la mascota.
    """

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

class PetsList:
    """
    Representa una lista de mascotas.

    Args:
        pets: Una lista de mascotas.
    """

    def __init__(self, pets):
        self.pets = pets

    def get_names(self):
        """
        Devuelve una lista de nombres de mascotas.

        Returns:
            Una lista de nombres de mascotas.
        """

        return [pet.name for pet in self.pets]
