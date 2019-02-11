#!/usr/bin/env python

import math

def run_function(function, param):
    return eval(function, {
        'sqrt': math.sqrt,
        'pow': math.pow
    }, {
        'x': float(param)
    })