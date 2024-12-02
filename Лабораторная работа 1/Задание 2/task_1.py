# TODO: Подробно описать три произвольных класса



# TODO: описать класс
class Car:
    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация автомобиля.

        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля. Должен быть не меньше 1886 (года первого автомобиля).

        :raises ValueError: Если год меньше 1886.
        """
        if year < 1886:
            raise ValueError("Год выпуска не может быть меньше 1886.")
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self) -> str:
        """
        Получить информацию об автомобиле.

        :return: Строка с информацией об автомобиле.

        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.get_car_info()
        'Toyota Camry, 2020'
        """
        return f"{self.make} {self.model}, {self.year}"

    def update_year(self, new_year: int) -> None:
        """
        Обновить год выпуска автомобиля.

        :param new_year: Новый год выпуска. Должен быть не меньше 1886.

        :raises ValueError: Если новый год меньше 1886.
        """
        if not isinstance(new_year, int):
            raise TypeError("Год выпуска должен быть int")
        self.year = new_year



# TODO: описать ещё класс
class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге. Должно быть положительным числом.

        :raises ValueError: Если количество страниц не положительное.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self) -> str:
        """
        Получить краткое содержание книги.

        :return: Строка с названием и автором книги.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.get_summary()
        '1984 by George Orwell'
        """
        return f"{self.title} by {self.author}"

    def read_pages(self, pages_to_read: int = 10) -> str:
        """
        Прочитать определенное количество страниц.

        :param pages_to_read: Количество страниц для чтения. Должно быть положительным числом.

        :raises ValueError: Если количество страниц для чтения не положительное.

        :return: Строка с сообщением о прочитанных страницах.

        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_pages(20)
        'Вы прочитали 20 страниц.'
        """
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным числом.")
        return f"Вы прочитали {pages_to_read} страниц."


# TODO: и ещё один

class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Инициализация дерева.

        :param species: Вид дерева.
        :param height: Высота дерева в метрах. Должна быть положительной.
        :param age: Возраст дерева в годах. Должен быть неотрицательным.

        :raises ValueError: Если высота не положительная или возраст отрицательный.
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        self.species = species
        self.height = height
        self.age = age

    def grow(self, growth: float) -> None:
        """
        Увеличить высоту дерева.

        :param growth: Увеличение высоты в метрах. Должно быть положительным числом.

        :raises ValueError: Если увеличение высоты не положительное.
        """
        if growth <= 0:
            raise ValueError("Увеличение высоты должно быть положительным числом.")
        self.height += growth

    def get_tree_info(self) -> str:
        """
        Получить информацию о дереве.

        :return: Строка с информацией о дереве.

        >>> tree = Tree("Oak", 5.0, 10)
        >>> tree.get_tree_info()
        'Вид: Oak, Высота: 5.0 м, Возраст: 10 лет'
        """
        return f"Вид: {self.species}, Высота: {self.height} м, Возраст: {self.age} лет"


