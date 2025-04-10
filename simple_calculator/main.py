# -*- coding: utf-8 -*-
import operator
from functools import reduce

class SimpleCalculator:
    def add(self, *args):
        return sum(args)
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        return reduce(operator.mul, args)
    
    def div(self, a, b):
        return a / b