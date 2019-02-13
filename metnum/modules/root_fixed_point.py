#!/usr/bin/env python

import time
import math

from common import Common
from metnum.helpers.run_function import run_function

LOOP_LIMIT = 1000000


class RootFixedPoint(Common):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Lack of argument to run root finding with Fixed Point Iteration method')
        self.function = argv[0]
        self.g_function = argv[1]
        self.first_x = float(argv[2])
        self.relative_error = float(argv[3]) if len(argv) > 3 else RootFixedPoint.default_error()
        self._performance = {}

    @staticmethod
    def help():
        return """math_function new_function x_0 [relative_error]

Arguments:
    math_function  : Math function in string with format python.
    new_function   : New math function in string with format python. This function is convertion of math_function when f(x) = 0.
    x_0            : First x value.
    relative_error : Optional. Relative error.
"""

    def execute(self):
        self._performance['loop'] = 1
        x_current = self.first_x

        while self._performance['loop'] < LOOP_LIMIT:
            new_x = self.run_g_function(x_current)
            testval = self.run_function(new_x)

            if abs(testval) < self.relative_error:
                return new_x

            x_current = new_x
            self._performance['loop'] += 1

        raise Exception('Loop forever?')

    def run_function(self, param_value):
        return run_function(self.function, param_value)

    def run_g_function(self, param_value):
        return run_function(self.g_function, param_value)

    def print_performance(self):
        print """
Performance:
    Total loop: %d
""" % (self._performance['loop'])
