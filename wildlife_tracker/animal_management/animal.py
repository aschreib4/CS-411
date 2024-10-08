from typing import Any, Optional

class Animal:

    def __init__(self, animal_id: int, species: str, health_status: Optional[str] = None):
        self.animal_id = animal_id
        self.species = species
        self.health_status = health_status
