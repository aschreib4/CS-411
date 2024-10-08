from typing import Optional, List

from wildlife_tracker.habitat_management.habitat import Habitat

class HabitatManager:

    def __init__(self):
        self.habitats: dict[int, Habitat] = {}

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        habitat = Habitat(habitat_id, geographic_area, size, environment_type)
        self.habitats[habitat_id] = habitat
        return habitat

    def remove_habitat(self, habitat_id: int) -> None:
        if habitat_id in self.habitats:
            del self.habitats[habitat_id]

    def get_habitat_by_id(self, habitat_id: int) -> Habitat:
        return self.habitats.get(habitat_id)

    def get_habitat_details(self, habitat_id: int) -> dict:
        habitat = self.get_habitat_by_id(habitat_id)
        return habitat.__dict__ if habitat else {}


