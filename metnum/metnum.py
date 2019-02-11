#!/usr/bin/env python

from __future__ import print_function
import sys

from modules import root_binary, root_regula

class Metnum():
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
    root_regula                 : Finding root value using Regula Fasi method
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

        print('Result is found: ' + str(mode.execute()))
        if self._print_performace:
            mode.print_performance()


    @staticmethod
    def mode_map():
        return {
            'root_binary': root_binary.RootBinary,
            'root_bisection': root_binary.RootBinary,
            'root_regula': root_regula.RegulaFasi
        }
