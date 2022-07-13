from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_local_antagonist(self):
        ...

class Kostroma:
    city_name = 'Kostroma'

    def get_loc_antagonist(self):
        print('Orcs hid in the forest')

class Tokyo:
    name = 'Tokyo'

    def get_loc_antagonist(self):
        print('Godzilla stands near a skyscraper')
