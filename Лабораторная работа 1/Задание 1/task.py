# Описание класса Земля
class Earth:
    def __init__(self, diameter: float, population: int):
        """
        Инициализация планеты Земля.

        :param diameter: Диаметр Земли в километрах. Должен быть положительным числом.
        :param population: Население Земли. Должно быть неотрицательным числом.

        :raises ValueError: Если диаметр не положительный или население отрицательное.
        """
        if diameter <= 0:
            raise ValueError("Диаметр Земли должен быть положительным числом.")
        if population < 0:
            raise ValueError("Население не может быть отрицательным.")
        self.diameter = diameter
        self.population = population

    def get_info(self) -> str:
        """
        Получить информацию о Земле.

        :return: Строка с информацией о диаметре и населении Земли.

        >>> earth = Earth(12742, 7800000000)
        >>> earth.get_info()
        'Диаметр Земли: 12742 км, Население: 7800000000'
        """
        return f"Диаметр Земли: {self.diameter} км, Население: {self.population}"

    def update_population(self, new_population: int) -> None:
        """
        Обновить население Земли.

        :param new_population: Новое население. Должно быть неотрицательным числом.

        :raises ValueError: Если новое население отрицательное.
        """
        if new_population < 0:
            raise ValueError("Население не может быть отрицательным.")
        self.population = new_population


# Описание класса Бутылка
class Bottle:
    def __init__(self, volume: float, material: str):
        """
        Инициализация бутылки.

        :param volume: Объем бутылки в литрах. Должен быть положительным числом.
        :param material: Материал бутылки (например, 'пластик', 'стекло').

        :raises ValueError: Если объем не положительный.
        """
        if volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом.")
        self.volume = volume
        self.material = material

    def get_bottle_info(self) -> str:
        """
        Получить информацию о бутылке.

        :return: Строка с информацией о объеме и материале бутылки.

        >>> bottle = Bottle(1.5, "пластик")
        >>> bottle.get_bottle_info()
        'Объем: 1.5 л, Материал: пластик'
        """
        return f"Объем: {self.volume} л, Материал: {self.material}"

    def refill(self, additional_volume: float) -> None:
        """
        Заполнить бутылку дополнительным объемом.

        :param additional_volume: Дополнительный объем в литрах. Должен быть положительным числом.

        :raises ValueError: Если дополнительный объем не положительный.
        """
        if additional_volume <= 0:
            raise ValueError("Дополнительный объем должен быть положительным числом.")
        self.volume += additional_volume


# Описание класса Лампа
class Lamp:
    def __init__(self, brightness: int, color: str):
        """
        Инициализация лампы.

        :param brightness: Яркость лампы в люменах. Должна быть положительным числом.
        :param color: Цвет света лампы (например, 'белый', 'желтый').

        :raises ValueError: Если яркость не положительная.
        """
        if brightness <= 0:
            raise ValueError("Яркость лампы должна быть положительным числом.")
        self.brightness = brightness
        self.color = color
        self.is_on = False  # Лампа изначально выключена

    def turn_on(self) -> None:
        """
        Включить лампу.
        """
        self.is_on = True

    def turn_off(self) -> None:
        """
        Выключить лампу.
        """
        self.is_on = False

    def get_info(self) -> str:
        """
        Получить информацию о лампе.

        :return: Строка с информацией о яркости, цвете и состоянии лампы.

        >>> lamp = Lamp(800, "белый")
        >>> lamp.get_info()
        'Яркость: 800 люмен, Цвет: белый, Включена: False'
        """
        return f"Яркость: {self.brightness} люмен, Цвет: {self.color}, Включена: {self.is_on}"

    def set_brightness(self, new_brightness: int) -> None:
        """
        Установить новую яркость лампы.

        :param new_brightness: Новая яркость в люменах. Должна быть положительным числом.

        :raises ValueError: Если новая яркость не положительная.
        """
        if new_brightness <= 0:
            raise ValueError("Яркость лампы должна быть положительным числом.")
        self.brightness = new_brightness
