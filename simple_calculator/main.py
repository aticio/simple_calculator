# -*- coding: utf-8 -*-
import operator
from functools import reduce

class SimpleCalculator:
    def add(self, *args):
        return sum(args)
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        if not all(args):
            raise ValueError
        return reduce(operator.mul, args)
    
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')
    
    def avg(self, it, ut=None):
        if not ut:
            ut = max(it)
        
        _it = [x for x in it if x <= ut]

        return sum(_it) / len(_it)