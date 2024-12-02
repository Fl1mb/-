from task_1 import Car, Tree, Book
# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    book = Book("1984", "George Orwell", 328)
    car = Car("Toyota", "Camry", 2020)
    tree = Tree("Oak", 5.0, 10)
    try:
     # TODO: вызвать метод с некорректными аргументами(b)
        car.update_year("str")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        new_book = Book("C++", "Бьёрн Страуструп", -132)

    except ValueError:
        print('Ошибка: неправильные данные')

    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        tree.grow(-4123)
    except ValueError:
        print('Ошибка: неправильные данные')
