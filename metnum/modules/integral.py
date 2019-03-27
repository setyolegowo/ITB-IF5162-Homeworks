#!/usr/bin/env python

import time
import math

from common import Common
from metnum.helpers.run_function import run_function

class SquareStrip(Common):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Lack of argument to find total integral area with square strip method')
        self.function = argv[0]
        self.x_low = float(argv[1])
        self.x_high = float(argv[2])
        self.strips = int(argv[3])
        if self.strips <= 0:
            raise Exception('Strips should not equal or below zero')
        self._performance = {}

    @staticmethod
    def help():
        return """math_function x_low x_high strip

Arguments:
    math_function  : Math function in string with format python
    x_low          : Lowest range value
    x_high         : Highet range value
    strips         : Total strip to be used.
"""

    def execute(self):
        strip_wide = (self.x_high - self.x_low)/self.strips
        subtotal = self.run_function(self.x_low) + self.run_function(self.x_high)

        for x_i in range(1, self.strips - 1):
            subtotal += 2 * self.run_function(self.x_low + (strip_wide * x_i))

        self._performance['loop'] = self.strips
        return (strip_wide * subtotal)/2

    def run_function(self, param_value):
        return run_function(self.function, param_value)

    def print_performance(self):
        print """
Performance:
    Total loop: %d
""" % (self._performance['loop'])


class TrapeziumStrip(Common):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Lack of argument to find total integral area with trapezium strip method')
        self.function = argv[0]
        self.x_low = float(argv[1])
        self.x_high = float(argv[2])
        self.strips = int(argv[3])
        if self.strips <= 0:
            raise Exception('Strips should not equal or below zero')
        self._performance = {}

    @staticmethod
    def help():
        return """math_function x_low x_high strip

Arguments:
    math_function  : Math function in string with format python
    x_low          : Lowest range value
    x_high         : Highet range value
    strips         : Total strip to be used.
"""

    def execute(self):
        strip_wide = (self.x_high - self.x_low)/self.strips
        subtotal = self.run_function(self.x_low) + self.run_function(self.x_high)

        for x_i in range(1, self.strips - 1):
            subtotal += 2 * self.run_function(self.x_low + (strip_wide * x_i))

        self._performance['loop'] = self.strips
        return (strip_wide * subtotal)/2

    def run_function(self, param_value):
        return run_function(self.function, param_value)

    def print_performance(self):
        print """
Performance:
    Total loop: %d
""" % (self._performance['loop'])


class MidpointStrip(Common):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Lack of argument to find total integral area with midpoint strip method')
        self.function = argv[0]
        self.x_low = float(argv[1])
        self.x_high = float(argv[2])
        self.strips = int(argv[3])
        if self.strips <= 0:
            raise Exception('Strips should not equal or below zero')
        self._performance = {}

    @staticmethod
    def help():
        return """math_function x_low x_high strip

Arguments:
    math_function  : Math function in string with format python
    x_low          : Lowest range value
    x_high         : Highet range value
    strips         : Total strip to be used.
"""

    def execute(self):
        strip_wide = (self.x_high - self.x_low)/self.strips
        current_x = self.x_low + (strip_wide/2)
        subtotal = self.run_function(current_x)

        for x_i in range(1, self.strips - 1):
            current_x += strip_wide
            subtotal += self.run_function(current_x)

        self._performance['loop'] = self.strips
        return strip_wide * subtotal

    def run_function(self, param_value):
        return run_function(self.function, param_value)

    def print_performance(self):
        print """
Performance:
    Total loop: %d
""" % (self._performance['loop'])


class Simpson1Per3(Common):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Lack of argument to find total integral area with Simpson 1/3 method')
        self.function = argv[0]
        self.x_low = float(argv[1])
        self.x_high = float(argv[2])
        self.strips = int(argv[3])
        if self.strips <= 0:
            raise Exception('Strips should not equal or below zero')
        self._performance = {}

    @staticmethod
    def help():
        return """math_function x_low x_high strip

Arguments:
    math_function  : Math function in string with format python
    x_low          : Lowest range value
    x_high         : Highet range value
    strips         : Total strip to be used.
"""

    def execute(self):
        strip_wide = (self.x_high - self.x_low)/self.strips
        subtotal = self.run_function(self.x_low) + self.run_function(self.x_high)

        for x_i in range(1, self.strips - 1, 2):
            subtotal += 4 * self.run_function(self.x_low + (strip_wide * x_i))

        for x_i in range(2, self.strips - 2, 2):
            subtotal += 2 * self.run_function(self.x_low + (strip_wide * x_i))

        self._performance['loop'] = self.strips
        return (strip_wide * subtotal)/3

    def run_function(self, param_value):
        return run_function(self.function, param_value)

    def print_performance(self):
        print """
Performance:
    Total loop: %d
""" % (self._performance['loop'])


class Simpson3Per8(Common):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Lack of argument to find total integral area with Simpson 3/8 method')
        self.function = argv[0]
        self.x_low = float(argv[1])
        self.x_high = float(argv[2])
        self.strips = int(argv[3])
        if self.strips <= 0:
            raise Exception('Strips should not equal or below zero')
        self._performance = {}

    @staticmethod
    def help():
        return """math_function x_low x_high strip

Arguments:
    math_function  : Math function in string with format python
    x_low          : Lowest range value
    x_high         : Highet range value
    strips         : Total strip to be used.
"""

    def execute(self):
        strip_wide = (self.x_high - self.x_low)/self.strips
        subtotal = self.run_function(self.x_low) + self.run_function(self.x_high)

        for x_i in range(1, self.strips - 1):
            if x_i % 3 == 0:
                subtotal += 2 * self.run_function(self.x_low + (strip_wide * x_i))
            else:
                subtotal += 3 * self.run_function(self.x_low + (strip_wide * x_i))

        self._performance['loop'] = self.strips
        return (3 * strip_wide * subtotal)/8

    def run_function(self, param_value):
        return run_function(self.function, param_value)

    def print_performance(self):
        print """
Performance:
    Total loop: %d
""" % (self._performance['loop'])
