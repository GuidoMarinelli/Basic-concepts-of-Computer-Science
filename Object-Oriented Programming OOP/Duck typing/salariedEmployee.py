#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal


class SalariedEmployee:
    """Class representing an employee who gets paid a weekly salary."""

    def __init__(self, first_name, last_name, cf, weekly_salary):
        """Initialize SalariedEmployee attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._cf = cf
        self.weekly_salary = weekly_salary  # validate via property

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
    def weekly_salary(self):
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, salary):
        """Set weekly salary or raise ValueError if invalid."""

        if salary < Decimal('0.00'):
            raise ValueError('Salary worked must be >= 0.0')

        self._weekly_salary = salary

    def earnings(self):
        """Calcola i guadagni."""
        return self._weekly_salary

    def __repr__(self):
        """Return string representation for repr()."""
        return ('SalariedEmployee: ' +
                f'{self.first_name} {self.last_name}\n' +
                f'codice fiscale: {self.cf}\n' +
                f'stipendio settimanale: {self.weekly_salary:.2f}')
