from antagonistfinder import AntagonistFinder


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def fire_a_gun(self):
        print('PIU PIU')

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def roundhouse_kick(self):
        print('Bump')

    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        if self.name == 'Clark Kent':
            self.incinerate_with_lasers()

class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        return 'Kick'

class Fire_a_gun:

    def attack(self):
        print('PIU PIU')

class Incinerate_with_lasers:

    def attack(self):
        print('Wzzzuuuup!')

class Roundhouse_kick:

    def attack(self):
        print('Bump')

class Media:

    @staticmethod
    def create_news(place, hero, tv_on=False):
        place_name = getattr(place, 'coordinates', True) if getattr(place, 'coordinates', True) != True \
            else getattr(place, 'name', 'place')
        hero_name = getattr(hero, 'name', 'hero')
        tv = ' In TV!' if tv_on == True else ' In newspaper!'
        print(f'{hero_name} saved the {place_name}!{tv}')

class ChuckNorris(Fire_a_gun, SuperHero):
    
    def __init__(self):
        super(ChuckNorris, self).__init__('Chack Norris', False)