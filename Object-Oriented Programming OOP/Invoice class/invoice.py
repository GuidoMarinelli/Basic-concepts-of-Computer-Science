#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal


class Invoice:
    """Class representing the invoice of an item sold in a hardware store."""

    def __init__(self, item_code, item, quantity_of_purchased_items,
                 item_price):
        """Initialize Invoice's attributes."""
        self._item_code = item_code
        self._item = item
        self.quantity_of_purchased_items = quantity_of_purchased_items
        self.item_price = item_price

    @property
    def item_code(self):
        return self._item_code

    @property
    def item(self):
        return self._item

    @property
    def quantity_of_purchased_items(self):
        return self._quantity_of_purchased_items

    @quantity_of_purchased_items.setter
    def quantity_of_purchased_items(self, quantity):
        """Set the quantity of items purchased or
        raises ValueError if invalid."""

        if quantity < int(0):
            raise ValueError('The quantity of items purchased must be >= 0')

        self._quantity_of_purchased_items = quantity

    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, price):
        """‘Set the price of the item or raise ValueError if it is invalid."""

        if price < Decimal('0.00'):
            raise ValueError('The price of the item must be >= 0')

        self._item_price = price

    def calculate_invoice(self):
        """Calculate the amount of the invoice."""
        return self._quantity_of_purchased_items * self._item_price

    def __repr__(self):
        """Return string representation for repr()."""
        return ('Fattura:\n' +
                f'codice articolo: {self._item_code}\n' +
                f'articolo: {self._item}\n' +
                'quantità articoli acquistati:' +
                f' {self._quantity_of_purchased_items}\n' +
                f'prezzo singolo articolo: {self._item_price:.2f}')


# show the features of the Invoice class
def main():
    bolt = Invoice('1234', 'Bullone', 3, Decimal('1.50'))
    print(bolt)
    print(f'{bolt.calculate_invoice():.2f}')


if __name__ == '__main__':
    main()
