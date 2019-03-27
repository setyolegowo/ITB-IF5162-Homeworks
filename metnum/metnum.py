#!/usr/bin/env python

from __future__ import print_function
import sys

from modules import root_binary, root_regula, root_secant, root_fixed_point, root_newton_raphson, integral, interpolation

class Metnum(object):
    def __init__(self, argv):
        self._program_name = argv[0]
        if len(argv) == 1:
            print('Choose one mode as first argument\n')
            print(self._help())
            sys.exit(1)

        self._print_performace = False
        if argv[1] == '-p':
            self._print_performace = True
            argv = argv[2:]
        else:
            argv = argv[1:]
        self._mode = argv[0]
        self._argv = argv[1:] if len(argv) > 1 else {}

    def _help(self):
        return './' + self._program_name + """ mode [args]

Available modes:
    root_binary, root_bisection : Finding root value using Binary/Bisection method
    root_regula                 : Finding root value using Regula-Falsi method
    root_secant                 : Finding root value using Secant method
    root_fixed_point            : Finding root value using Fixed Point method
    root_newton_rhapson         : Finding root value using Newton Rhapson method
    interpolation_linear        : Find interpolation function for linear interpocation method
    interpolation_lagrange      : Find interpolation function for lagrange interpocation method
    interpolation_newton        : Find interpolation function for newton interpocation method
    interpolation_linear_calc   : Find value from generated linear interpolation function
    interpolation_lagrange_calc : Find value from generated lagrange interpolation function
    interpolation_newton_calc   : Find value from generated newton interpolation function
    integral_square_strip       : Integral finding using square strip method.
    integral_trapezium_strip    : Integral finding using trapezium strip method.
    integral_midpoint_strip     : Integral finding using midpoint strip method.
    integral_simpson_1_3        : Integral finding using Simpson 1/3 method.
    integral_simpson_3_8        : Integral finding using Simpson 3/8 method.
"""


    def execute(self):
        if (self._mode == '-h'):
            print(self._help())
            sys.exit(0)

        try:
            mode = Metnum.mode_map()[self._mode](self._argv)
        except Exception as exc:
            print(exc.message + '\n')
            print('./' + self._program_name + ' ' + self._mode + ' ' + Metnum.mode_map()[self._mode].help())
            sys.exit(1)

        result = mode.execute()
        if isinstance(result, str):
            print('Generated function: y = ' + str(result))
        else:
            print('Result is found: ' + str(result))

        if self._print_performace:
            mode.print_performance()


    @staticmethod
    def mode_map():
        return {
            'root_binary': root_binary.RootBinary,
            'root_bisection': root_binary.RootBinary,
            'root_regula': root_regula.RegulaFasi,
            'root_secant': root_secant.RootSecant,
            'root_fixed_point': root_fixed_point.RootFixedPoint,
            'root_newton_rhapson': root_newton_raphson.RootNewtonRaphson,
            'integral_square_strip': integral.SquareStrip,
            'integral_trapezium_strip': integral.TrapeziumStrip,
            'integral_midpoint_strip': integral.MidpointStrip,
            'integral_simpson_1_3': integral.Simpson1Per3,
            'integral_simpson_3_8': integral.Simpson3Per8,
            'interpolation_linear': interpolation.LinearInterpolation,
            'interpolation_lagrange': interpolation.LagrangeInterpolation,
            'interpolation_newton': interpolation.NewtonInterpolation,
            'interpolation_linear_calc': interpolation.CalculateLinear,
            'interpolation_lagrange_calc': interpolation.CalculateLagrange,
            'interpolation_newton_calc': interpolation.CalculateNewton,
        }
