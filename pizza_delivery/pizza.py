#!/usr/bin/env python

# В. Пупкин развозит пиццу. Ему сообщают адрес доствки в виде
# <улица> <номер дома>-<номер квартиры>
#
# Приезжая по указанному адресу, Вася видит здание с числом этажей `floors`.
# Для простоты будем считать, что на каждом этаже в подъезде находятся 4 квартиры.
#
# Помогите Васе посчитать, в каком подъезде и на каком этаже находится нужная квартира n.
#
# Для решения понадобится использовать деление по модулю %
# или целочисленное деление //.

FLATS_PER_FLOOR = 4


def find_entrance(floors, n):
    """
    floors - число этажей в доме
    n - номер квартиры
    """
    entrance_one = floors * FLATS_PER_FLOOR
    entrance_summ = 0
    entrance = 0
    while n > entrance_summ:
        entrance_summ += entrance_one
        entrance += 1
    return entrance


def find_floor(floors, n):
    """
    floors - число этажей в доме
    n - номер квартиры
    """
    entrance_calc = entrance * floors * FLATS_PER_FLOOR
    floor = floors + 1
    while entrance_calc >= n:
        entrance_calc -= FLATS_PER_FLOOR
        floor -= 1
    return floor


if __name__ == "__main__":
    floors = int(input("Число этажей: "))
    flat_num = int(input("Номер квартиры: "))

    entrance = find_entrance(floors, flat_num)
    floor = find_floor(floors, flat_num)
    print(entrance, floor)

