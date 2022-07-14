from abc import ABC, abstractmethod
from typing import List


class Place(ABC):

    @abstractmethod
    def get_loc_antagonist(self):
        pass

class Kostroma(Place):
    city_name = 'Kostroma'

    @staticmethod
    def get_loc_antagonist():
        print('Orcs hid in the forest')

class Tokyo(Place):
    city_name = 'Tokyo'

    @staticmethod
    def get_loc_antagonist():
        print('Godzilla stands near a skyscraper')


class Planet(Place):

    def __init__(self, coordinate: List[float]):
        self.coordinate = coordinate

    @staticmethod
    def get_loc_antagonist():
        print('Alien is commin!')
