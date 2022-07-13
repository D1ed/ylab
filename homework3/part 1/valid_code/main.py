from typing import Union
from heroes import Superman, SuperHero, Media, ChuckNorris
from places import Kostroma, Tokyo



def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    mass_media = Media()
    mass_media.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo())
