import math


def area(r):
    '''
    Принимает число r, возвращает площадь круга радиусом r
    input:
        3
    output:
        28.274333882308138
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r, возвращает периметр окружности радиусом r
    input:
        6
    output:
        37.69911184307752
    '''
    return 2 * math.pi * r
