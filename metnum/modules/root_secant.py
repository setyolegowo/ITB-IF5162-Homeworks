#!/usr/bin/env python

import time
import math

from common import Common
from metnum.helpers.run_function import run_function

LOOP_LIMIT = 1000000

class RootSecant(Common):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Lack of argument to run root finding with secant method')
        self.function = argv[0]
        self.x_0 = float(argv[1])
        self.x_1 = float(argv[2])
        self.relative_error = float(argv[3]) if len(argv) > 3 else RootSecant.default_error()
        self._performance = {}

    @staticmethod
    def help():
        return """math_function x_0 x_1 [relative_error]

Arguments:
    math_function  : Math function in string with format python
    x_0            : Lowest range value
    x_1            : Highet range value
    relative_error : Optional. Relative error.
"""

    def execute(self):
        self._performance['loop'] = 1
        x_before = self.x_0
        x_now = self.x_1

        while self._performance['loop'] < LOOP_LIMIT:
            x_next = self.new_x_mid(x_now, x_before)

            if abs((x_next - x_now)/x_next) <= self.relative_error:
                return x_next

            x_before = x_now
            x_now = x_next
            self._performance['loop'] += 1

        raise Exception('Loop forever?')

    def new_x_mid(self, x_low, x_high):
        return x_low - (self.run_function(x_low) * (x_high - x_low) / (self.run_function(x_high) - self.run_function(x_low)))

    def run_function(self, param_value):
        return run_function(self.function, param_value)

    def print_performance(self):
        print """
Performance:
    Total loop: %d
""" % (self._performance['loop'])
