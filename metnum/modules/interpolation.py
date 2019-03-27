#!/usr/bin/env python

import time
import math

from common import Common
from metnum.helpers.run_function import run_function


class LinearInterpolation(Common):
    def __init__(self, argv):
        if len(argv) < 2:
            raise Exception('Must have 2 points')
        self.x_low, self.y_low = [float(x) for x in argv[0].split(',')]
        self.x_high, self.y_high = [float(x) for x in argv[1].split(',')]

    @staticmethod
    def help():
        return """x_low,x_high x_high,y_high

Arguments:
    x_low,y_low    : Low point
    x_high,y_high  : High point
"""

    def execute(self):
        a_1 = (self.y_high - self.y_low)/(self.x_high - self.x_low)
        a_0 = (self.x_high*self.y_low - self.x_low*self.y_high)/(self.x_high - self.x_low)
        return str(a_0) + ' + ' + str(a_1) + '*x'

    def print_performance(self):
        print 'No performance can be calculated'

class LagrangeInterpolation(Common):
    def __init__(self, argv):
        if len(argv) < 2:
            raise Exception('Minimum 2 points')
        self.data_x = []
        self.data_y = []
        self.total_point = len(argv)
        for el in argv:
            x, y = (float(iel) for iel in el.split(','))
            self.data_x.append(x)
            self.data_y.append(y)

    @staticmethod
    def help():
        return """x_0,y_0 x_1,y_1 [x_2,y_2, [x_3, y_3], ...]

Arguments:
    x_i,y_i        : Point(s) at i for 0 < i <= n
"""

    def execute(self):
        retval = []
        for index in range(0, self.total_point):
            retval.append('(' + str(self.__calculate_y_per_x(index)) + '*' + self.__get_x(index) + ')')
        return ' + '.join(retval)

    def __calculate_y_per_x(self, index):
        retval = self.data_y[index]
        for index_j in range(0, self.total_point):
            if index_j != index:
                retval /= self.data_x[index] - self.data_x[index_j]
        return retval

    def __get_x(self, index):
        retval = []
        for index_j in range(0, self.total_point):
            if index_j != index:
                if self.data_x[index_j] < 0:
                    retval.append('(x + ' + str(abs(self.data_x[index_j])) + ')')
                else:
                    retval.append('(x - ' + str(self.data_x[index_j]) + ')')

        return '*'.join(retval)

    def print_performance(self):
        print 'No performance can be calculated'


class NewtonInterpolation(Common):
    def __init__(self, argv):
        if len(argv) < 2:
            raise Exception('Minimum 2 points')
        self.data_x = []
        self.data_y = []
        self.data_st = []
        self.total_point = len(argv)
        for el in argv:
            x, y = (float(iel) for iel in el.split(','))
            self.data_x.append(x)
            self.data_y.append(y)

    @staticmethod
    def help():
        return """x_0,y_0 x_1,y_1 [x_2,y_2, [x_3, y_3], ...]

Arguments:
    x_i,y_i        : Point(s) at i for 0 < i <= n
"""

    def execute(self):
        retval = []
        for index in range(0, self.total_point):
            retval.append('(' + str(self.__calculate_y(index)) + self.__get_x(index) + ')')
        return ' + '.join(retval)

    def __calculate_y(self, index):
        retval = []
        for index_j in range(0, self.total_point - index):
            if index == 0:
                retval.append(self.data_y[index_j])
            else:
                retval.append((self.data_st[index - 1][index_j + 1] - self.data_st[index - 1][index_j])/(self.data_x[index_j + index] - self.data_x[index_j]))
        self.data_st.append(retval)
        return self.data_st[index][0]

    def __get_x(self, index):
        retval = []
        for index_j in range(0, index):
            if self.data_x[index_j] < 0:
                retval.append('(x + ' + str(abs(self.data_x[index_j])) + ')')
            else:
                retval.append('(x - ' + str(self.data_x[index_j]) + ')')

        if len(retval) > 0:
            return '*' + '*'.join(retval)
        return ''

    def print_performance(self):
        print 'No performance can be calculated'


class Calculate(Common):
    def __init__(self, argv):
        self.val_x = float(argv[0])
        self.interpolation = None

    @staticmethod
    def help():
        return """x_low,x_high x_high,y_high

Arguments:
    x_low,y_low    : Low point
    x_high,y_high  : High point
"""

    def execute(self):
        function = self.interpolation.execute()
        print 'Generated function: y = ' + function
        return run_function(function, self.val_x)

    def print_performance(self):
        self.interpolation.print_performance()

class CalculateLinear(Calculate):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Must have 2 points')
        super(CalculateLinear, self).__init__(argv)
        self.interpolation = LinearInterpolation(argv[1:])

    @staticmethod
    def help():
        return 'x_val ' + LinearInterpolation.help() + """    x_val          : X value
"""

class CalculateLagrange(Calculate):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Minimum have 2 points')
        super(CalculateLagrange, self).__init__(argv)
        self.interpolation = LagrangeInterpolation(argv[1:])

    @staticmethod
    def help():
        return 'x_val ' + LagrangeInterpolation.help() + """    x_val          : X value
"""


class CalculateNewton(Calculate):
    def __init__(self, argv):
        if len(argv) < 3:
            raise Exception('Minimum have 2 points')
        super(CalculateNewton, self).__init__(argv)
        self.interpolation = NewtonInterpolation(argv[1:])

    @staticmethod
    def help():
        return 'x_val ' + NewtonInterpolation.help() + """    x_val          : X value
"""
