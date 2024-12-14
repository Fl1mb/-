from pyexpat import ParserCreate


class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author) #вызываем конструктор родителя
        self._pages = pages # сделал атрибут pages protected, потому что все равно пишутся свойства для него

    def __repr__(self)->str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if pages < 0:
            raise ValueError("Количество страниц не может быть меньше нуля.")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц не может быть не целым числом")
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author) #вызываем конструктор родителя
        self._duration = duration

    def __repr__(self)->str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if duration < 0:
            raise ValueError("Продолжительность книги не может быть меньше нуля.")
        if not isinstance(duration, (float, int)):
            raise TypeError("Продолжительность книги должно быть числового типа")
        self._duration = duration



