from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляров класса Phone с доп атрибутом количество сим карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Возвращает количество поддерживаемых сим-карт в телефоне
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        """
        Присваивает атрибуту number_of_sim значение new_number_of_sim,
        при условии, что это целое число больше нуля
        """
        if num > 0 and isinstance(num, int):
            self.__number_of_sim = num
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
