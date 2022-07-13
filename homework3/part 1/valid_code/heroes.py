from antagonistfinder import AntagonistFinder


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack = True):
        self.name = name
        self.finder = AntagonistFinder()
        self.can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place):
        self.finder.get_antagonist(place)


class Kick:

    def attack(self):
        return 'Kick'


class Fire_a_gun:

    def attack(self):
        print('PIU PIU')


class Roundhouse_kick:

    def attack(self):
        print('Bump')


class Incinerate_with_lasers:

    def attack(self):
        print('Wzzzuuuup!')


class Media:

    @staticmethod
    def create_news(place, hero, tv_on=False):
        place_name = getattr(place, 'coordinates', True) if getattr(place, 'coordinates', True) != True \
            else getattr(place, 'name', 'place')
        hero_name = getattr(hero, 'name', 'hero')
        tv = ' In TV!' if tv_on == True else ' In newspaper!'
        print(f'{hero_name} saved the {place_name}!{tv}')


class Superman(Kick, SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)
    
    def ultimate(self):
        Incinerate_with_lasers.attack(self)



class ChuckNorris(Fire_a_gun, SuperHero):
    
    def __init__(self):
        super(ChuckNorris, self).__init__('Chack Norris', False)
