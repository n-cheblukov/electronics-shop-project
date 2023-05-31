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