from typing import Union
from heroes import Superman, SuperHero, Media, ChuckNorris, TV, Newspaper, PlanetExpress
from places import Kostroma, Tokyo, Place, Planet


def save_the_place(hero: SuperHero, place: Place, media: Media):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.create_news(place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), TV(Superman()))
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), Newspaper(ChuckNorris()))
    print('-' * 20)
    save_the_place(Superman(), Planet([13.88, 14.77]), PlanetExpress(Superman()))
    print('-' * 20)
    save_the_place(ChuckNorris(), Planet([12.99, 15.54]), PlanetExpress(ChuckNorris()))
