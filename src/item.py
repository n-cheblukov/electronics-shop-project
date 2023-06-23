import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV = '../src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        """Сложение экземпляров класса Phone и Item по количеству товара в магазине"""
        if not isinstance(other, self.__class__):
            raise ValueError('Невозможно сложить не зависящие классы')
        return self.quantity + other.quantity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 20:
            self.__name = new_name
        else:
            raise Exception(f'{new_name} - is too much letters')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return float(total_price)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    # Создаем класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        try:
            with open(cls.CSV, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row['name']) == 0 or int(row['price']) < 1 or int(row['quantity']) < 0:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    # Создаем статический метод, возвращающий число из числа-строки
    @staticmethod
    def string_to_number(file):
        return int(float(file))


class InstantiateCSVError(Exception):
    """
    Исключения повреждения CSV-файла
    """
    def __init__(self, massage):
        self.message = massage

    def __str__(self):
        return f'{self.message}'
