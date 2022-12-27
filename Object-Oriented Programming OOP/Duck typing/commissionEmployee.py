#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal


class CommissionEmployee:
    """Class representing an employee who gets paid
    commission based on gross sales."""

    def __init__(self, first_name, last_name, cf,
                 gross_sales, commission_rate):
        """Initialize CommissionEmployee's attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._cf = cf
        self.gross_sales = gross_sales  # validate via property
        self.commission_rate = commission_rate  # validate via property

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def cf(self):
        return self._cf

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        """Set gross sales or raise ValueError if invalid."""

        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')

        self._gross_sales = sales

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        """Set commission rate or raise ValueError if invalid."""

        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError(
               'Interest rate must be greater than 0 and less than 1')

        self._commission_rate = rate

    def earnings(self):
        """Calculate earnings."""
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        """Return string representation for repr()."""
        return ('CommissionEmployee: ' +
                f'{self.first_name} {self.last_name}\n' +
                f'codice fiscale: {self.cf}\n' +
                f'vendite lorde: {self.gross_sales:.2f}\n' +
                f'tasso di commissione: {self.commission_rate:.2f}')
