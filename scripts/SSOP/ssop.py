#!/usr/bin/env python

import sys
import os
sys.path.append("..//..")
from KicadModTree.Component import *

DEFAULT_DENSITY_LEVEL = 'B' # Nominal

ssop = {
    'SSOP_8' : pkgparams(
        Dmin = 2.75,
        Dmax = 3.15,
        E1min = 2.70,
        E1max = 2.90,
        Emin = 3.75,
        Emax = 4.25,
        Amax = 1.30,
        Lmin = 0.20,
        Lmax = 0.60,
        bmin = 0.15,
        bmax = 0.30,
        e = 0.65,
        npx = 4,
        npy = 0,
        fN = 'SSOP-8',
        ort = 'A',
        epad = None,
    )
}

make_pkg_comp(ssop['SSOP_8'])
