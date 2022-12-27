#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal

from commissionEmployee import CommissionEmployee
from salariedCommissionEmployee import SalariedCommissionEmployee
from salariedEmployee import SalariedEmployee

# CommissionEmployee base class
c = CommissionEmployee('Sue', 'Jones', '3333333333333333',
                       Decimal('20000.00'), Decimal('0.10'))

# subclass SalariedCommissionEmployee derived from CommissionEmployee
s = SalariedCommissionEmployee('Bob', 'Lewis', '4444444444444444',
                               Decimal('10000.00'), Decimal('0.05'),
                               Decimal('1000.00'))

# new class that does not inherit from
# CommissionEmployee and SalariedCommissionEmployee
w = SalariedEmployee('John', 'Green', '5555555555555555', Decimal('550.00'))

employess = [c, s, w]

for employee in employess:
    print(employee)
    print(f'{employee.earnings():,.2f}\n')
