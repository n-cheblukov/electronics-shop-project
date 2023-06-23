"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.keyboard import KeyBoard
import os


@pytest.fixture
def product_item():
    item1 = Item('TV', 150000, 5)
    return item1


@pytest.fixture
def phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test_calculate_total_price(product_item):
    assert product_item.calculate_total_price() == 750000.0


def test_apply_discount(product_item):
    Item.pay_rate = 0.5
    product_item.apply_discount()
    assert product_item.price == 75000


def test_string_to_number():
    assert Item.string_to_number('153') == 153
    assert Item.string_to_number('25.234') == 25
    assert Item.string_to_number('35.8') == 35


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    Item.CSV = "file"
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

    Item.CSV = '../tests/test.csv'
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_check_name(product_item):
    product_item.name = 'Hi-Fi'
    assert product_item.name == 'Hi-Fi'


def test_repr_str(product_item):
    assert repr(product_item) == "Item('TV', 150000, 5)"
    assert str(product_item) == 'TV'


def test_add(product_item, phone):
    assert product_item + phone == 10


def test_keyboard_change_lang():
    k = KeyBoard('Keyboard', 100, 10)
    assert str(k) == 'Keyboard'
    for i in ['RU', 'EN', 'RU', 'EN']:
        k.change_lang()
        assert k.language == i
