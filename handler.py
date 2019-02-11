#!/usr/bin/env python

import sys

from metnum.metnum import Metnum

if __name__ == "__main__":
    _metnum = Metnum(sys.argv)
    retval = _metnum.execute()
