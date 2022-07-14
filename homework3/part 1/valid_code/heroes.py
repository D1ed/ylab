from antagonistfinder import AntagonistFinder
from abc import ABC, abstractmethod
from places import Place


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack = True):
        self.name = name
        self.finder = AntagonistFinder()
        self.can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        pass

    def ultimate(self):
        pass

class Kick:
    
    def kick(self):
        return 'Kick'

class Gun:

    def fire_a_gun(self):
        print('PIU PIU')


class RoundhouseKick:

    def roundhouse_kick(self):
        print('Bump')


class IncinerateWithLasers:

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class Superman(SuperHero, Kick, IncinerateWithLasers):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)
   
    def attack(self):
        self.kick()

    def ultimate(self):
        self.incinerate_with_lasers()
    

class ChuckNorris(SuperHero, Gun):
    
    def __init__(self):
        super(ChuckNorris, self).__init__('Chack Norris', False)

    def attack(self):
        self.fire_a_gun()


class Media(ABC):

    def __init__(self, hero: SuperHero):
        self.hero_name = getattr(hero, "name")

    @abstractmethod
    def create_news(self, place: Place):
        pass


class TV(Media):

    def __init__(self, hero: SuperHero):
        super(TV, self).__init__(hero)

    def create_news(self, place: Place):
        place_name = getattr(place, 'city_name')
        print(f'{self.hero_name} saved the {place_name}! Watch in TV!')


class Newspaper(Media):

    def __init__(self, hero: SuperHero):
        super(Newspaper, self).__init__(hero)

    def create_news(self, place: Place):
        place_name = getattr(place, 'city_name')
        print(f'{self.hero_name} saved the {place_name}! Read in our newspaper!')


class PlanetExpress(Media):

    def __init__(self, hero: SuperHero):
        super(PlanetExpress, self).__init__(hero)

    def create_news(self, place: Place):
        place_name = getattr(place, 'coordinate')
        print(f'{self.hero_name} saved the {place_name}! Thanks for read us, PlanetExpress!')
