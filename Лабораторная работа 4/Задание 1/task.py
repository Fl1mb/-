# TODO: описать базовый класс

class Animal:
    """
    Базовый класс для всех животных.

    Атрибуты:
        _age (int): Возраст животного. Должен быть непубличным, чтобы предотвратить
                    случайное изменение извне.
        _weight (float): Вес животного. Должен быть непубличным, чтобы обеспечить
                         контроль над изменениями веса.
        _gender (str): Пол животного. Должен быть непубличным, чтобы избежать
                       некорректных изменений.
    """

    def __init__(self, age: int, weight: float, gender: str):
        """
        Инициализация атрибутов животного.

        Args:
            age (int): Возраст животного.
            weight (float): Вес животного.
            gender (str): Пол животного.
        """
        self._age = age
        self._weight = weight
        self._gender = gender

    # Базовые геттеры и сеттеры
    # Они наследуются
    @property
    def age(self) -> int:
        """Получить возраст животного."""
        return self._age

    @age.setter
    def age(self, new_age: int):
        """Установить новый возраст животного.

        Args:
            new_age (int): Новый возраст животного.

        Raises:
            TypeError: Если новый возраст не является целым числом.
            ValueError: Если новый возраст отрицательный.
        """
        if not isinstance(new_age, int):
            raise TypeError("Возраст должен быть целочисленного типа")
        if new_age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = new_age

    @property
    def weight(self) -> float:
        """Получить вес животного."""
        return self._weight

    @weight.setter
    def weight(self, new_weight: float):
        """Установить новый вес животного.

        Args:
            new_weight (float): Новый вес животного.

        Raises:
            TypeError: Если новый вес не является числом.
            ValueError: Если новый вес отрицательный.
        """
        if not isinstance(new_weight, (float, int)):
            raise TypeError("Вес должен быть числом")
        if new_weight < 0:
            raise ValueError("Вес не может быть отрицательным")
        self._weight = new_weight

    @property
    def gender(self) -> str:
        """Получить пол животного."""
        return self._gender

    def __str__(self) -> str:
        """Строковое представление животного."""
        return f'I am {self.__class__.__name__}. I am {self.age} years old. I am {self.gender}.'

    def __repr__(self) -> str:
        """Представление животного для отладки."""
        return f'{self.__class__.__name__}(age={self.age}, weight={self.weight}, gender={self.gender})'

    # Базовый метод (в наследнике без изменений)
    def age_in_months(self) -> int:
        """Получить возраст животного в месяцах."""
        return self.age * 12

# TODO: описать дочерний класс

class Horse(Animal):
    """
    Класс для лошадей, наследующий от класса Animal.

    Атрибуты:
        _breed (str): Порода лошади. Должен быть непубличным, чтобы предотвратить
                      случайное изменение извне.
    """
    # Переопределенный метод инициализации (перегружен)
    def __init__(self, age: int, weight: float, gender: str, breed: str):
        """
        Инициализация атрибутов лошади.

        Args:
            age (int): Возраст лошади.
            weight (float): Вес лошади.
            gender (str): Пол лошади.
            breed (str): Порода лошади.
        """
        super().__init__(age, weight, gender)
        self._breed = breed

    @property
    def breed(self) -> str:
        """Получить породу лошади."""
        return self._breed

    # Перегруженный метод __str__
    def __str__(self) -> str:
        """Строковое представление лошади с указанием породы."""
        return f'I am a {self.breed} horse. I am {self.age} years old and I am {self.gender}.'

    # Перегруженный метод __repr__
    def __repr__(self) -> str:
        """Представление лошади для отладки."""
        return f'{self.__class__.__name__}(age={self.age}, weight={self.weight}, gender={self.gender}, breed={self.breed})'

    def gallop(self) -> str:
        """Метод, который имитирует галоп лошади.

        Returns:
            str: Сообщение о том, что лошадь галопирует.
        """
        return f'The {self.breed} horse is galloping!'





