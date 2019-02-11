#!/usr/bin/env python

import time
import math

from common import Common
from metnum.helpers.run_function import run_function

LOOP_LIMIT = 1000000

class RegulaFasi(Common):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception(
                'Lack of argument to run root finding with regula fasi method')
        self.function = argv[0]
        self.x_low = float(argv[1])
        self.x_high = float(argv[2])
        self.relative_error = float(argv[3]) if len(
            argv) > 3 else RegulaFasi.default_error()
        self._performance = {}

    @staticmethod
    def help():
        return """math_function x_low x_high [relative_error]

Arguments:
    math_function  : Math function in string with format python
    x_low          : Lowest range value
    x_high         : Highet range value
    relative_error : Optional. Relative error.
"""

    @staticmethod
    def default_error():
        return 0.000001

    def execute(self):
        self._performance['loop'] = 1
        old_x_mid = None
        x_low = self.x_low
        x_high = self.x_high

        while self._performance['loop'] < LOOP_LIMIT:
            x_mid = self.new_x_mid(x_low, x_high)
            test_val = self.run_function(x_low) * self.run_function(x_mid)

            # Test
            if test_val < 0:
                x_high = x_mid
            elif test_val > 0:
                x_low = x_mid
            else:
                return x_mid

            if old_x_mid is not None:
                if abs((x_mid - old_x_mid)/x_mid) <= self.relative_error:
                    return x_mid

            old_x_mid = x_mid
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
