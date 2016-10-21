from math import sqrt
from collections import namedtuple

PART_PLACEMENT_TOL = 0.025
PCB_LAND_FAB_TOL = 0.050

package = namedtuple('package', [
        'name',
        'n',
        'D_min',
        'D_max',
        'E1_min',
        'E1_max',
        'E_min',
        'E_max',
        'A_max',
        'L_min',
        'L_max',
        'b_min',
        'b_max',
        'e'
        ])

jointparams = namedtuple('jointparams', [
        'toe',
        'heel',
        'side',
        'crtyd_ex',
])

densitylevel = jointparams(
        toe = 0.25,
        heel = 0.25,
        side = 0.03,
        crtyd_ex = 0.20
)

SSOP_28_065 = package(
        name = 'SSOP-28',
        n = 28,
        D_min = 9.90,
        D_max = 10.50,
        E1_min = 5.00,
        E1_max = 5.60,
        E_min = 7.80,
        E_max = 8.20,
        A_max = 2.00,
        L_min = 0.55,
        L_max = 0.95,
        b_min = 0.15,
        b_max = 0.30,
        e = 0.65)

def generateGullWingPadDims(pkgparams):

    # OLD: Ltol = pkgparams.E_max - pkgparams.E_min
    Ltol = sqrt((pkgparams.E_max - pkgparams.E_min)**2 + (2 * PCB_LAND_FAB_TOL)**2 + (2 * PART_PLACEMENT_TOL)**2)
    print "LTol = ", Ltol
    # OLD: Wtol = pkgparams.b_max - pkgparams.b_min
    Wtol = sqrt((pkgparams.b_max - pkgparams.b_min)**2 + (2 * PCB_LAND_FAB_TOL)**2 + (2 * PART_PLACEMENT_TOL)**2)
    print "Wtol = ", Wtol
    Stol_rms = sqrt((pkgparams.E_max - pkgparams.E_min)**2 + 2 * (pkgparams.L_max - pkgparams.L_min)**2)
    print "Stol_rms = ", Stol_rms
    Smin = pkgparams.E_min - 2 * pkgparams.L_max
    print "Smin = ", Smin
    Smax = pkgparams.E_max - 2 * pkgparams.L_min
    print "Smax = ", Smax

    Stol = Smax - Smin
    Sdiff = Stol - Stol_rms
    print "Sdiff = ", Sdiff
    print "Stol = ", Stol

    n_Smin = Smin + Sdiff / 2
    print "n_Smin = ", n_Smin
    n_Smax = Smax - Sdiff / 2
    print "n_Smax = ", n_Smax

    Htol = sqrt((n_Smax - n_Smin)**2 + (2* PART_PLACEMENT_TOL)**2 + (2 * PCB_LAND_FAB_TOL)**2)

    Gmin = n_Smax - 2*densitylevel.heel - Htol
    print "Gmin = ", Gmin
    Xmax = pkgparams.b_min + 2*densitylevel.side + Wtol
    print "Xmax = ", Xmax
    Zmax = pkgparams.E_min + 2*densitylevel.toe + Ltol
    print "Zmax = ", Zmax
    pad_y = round((((Zmax - Gmin) / 2) * (1 / PCB_LAND_FAB_TOL)), 0) / (1 / PCB_LAND_FAB_TOL)
    pad_x = round(Xmax * (1 / PCB_LAND_FAB_TOL), 0) / (1 / PCB_LAND_FAB_TOL)

    print pad_x, pad_y

generateGullWingPadDims(SSOP_28_065)