"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def product_item():
    item1 = Item('TV', 150000, 5)
    return item1


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


def test_check_name(product_item):
    product_item.name = 'Hi-Fi'
    assert product_item.name == 'Hi-Fi'


def test_repr_str(product_item):
    assert repr(product_item) == "Item('TV', 150000, 5)"
    assert str(product_item) == 'TV'
