from task_1 import  Bottle, Earth, Lamp
# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    bottle = Bottle(0.5, "Alum")
    earth = Earth(6000, 800000000)
    lamp = Lamp(15, "White")
    try:
     # TODO: вызвать метод с некорректными аргументами(b)
        print(earth.get_info())
        earth.update_population(-3123123)
    except ValueError:
        print('Ошибка: неправильные данные')
    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        print(bottle.get_bottle_info())
        bottle.refill(-1)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        print(lamp.get_info())
        lamp.set_brightness(-213)
    except ValueError:
        print('Ошибка: неправильные данные')
