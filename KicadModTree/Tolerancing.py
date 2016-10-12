
from collections import namedtuple
from math import sqrt, pow

PART_PLACEMENT_TOL = 0.025
PCB_LAND_FAB_TOL = 0.05

def RMS(*args):
    rms = 0
    for arg in args:
        rms += arg*arg
    return sqrt(rms)


def generateSMDPadDims(pad_params, comp_params):

    try:
        toe, heel, side, crtyd_ex = pad_params
    except:
        "Not a valid set of params"
    
    try:
        pins, b_wmin, b_wmax, b_lmin, b_lmax, bl_lmin, bl_lmax, hmax, tl_min, tl_max, tw_min, tw_max, pitch = comp_params
    except: 
        "Not a valid set of params"

    Ltol = bl_lmax - bl_lmin
    Ttol = tl_max - tl_min

    Stol = sqrt(Ltol**2+2*(Ttol)**2)
    Smin = bl_lmin - 2 * tl_max
    Smax = Smin + Stol

    Wtol = tw_max - tw_min

    Gmin = Smax - 2*heel - RMS(Stol, PART_PLACEMENT_TOL, PCB_LAND_FAB_TOL)

    Xmax = tw_min + 2*side + RMS(Wtol, PART_PLACEMENT_TOL, PCB_LAND_FAB_TOL)
    
    Zmax = bl_lmin + 2*toe + RMS(Ltol, PART_PLACEMENT_TOL, PCB_LAND_FAB_TOL)
    
    pad_y = (Zmax - Gmin) / 2
    pad_x = Xmax

    print pad_x, pad_y

joint_params = namedtuple('params', [
    'toe',
    'heel',
    'side',
    'crtyd_ex'
])
nil = joint_params(
    toe = 0.15,
    heel = 0.25,
    side = -0.04,
    crtyd_ex = 0.1,
)

Params = namedtuple("Params", [
    'pins',
    'b_wmin',
    'b_wmax',
    'b_lmin',
    'b_lmax',
    'bl_lmin',
    'bl_lmax',
    'hmax',
    'tl_min',
    'tl_max',
    'tw_min',
    'tw_max',
    'pitch',
])

ssop = Params(
    pins = 44,
    b_wmin = 12.50,
    b_wmax = 13.10,
    b_lmin = 5.00,
    b_lmax = 5.60,
    bl_lmin = 7.40,
    bl_lmax = 8.20,
    hmax = 2.0,
    tl_min = 0.55,
    tl_max = 0.95,
    tw_min = 0.20,
    tw_max = 0.315,
    pitch = 0.50,
)

soic = Params(
    pins = 16,
    b_wmin = 9.80,
    b_wmax = 10.00,
    b_lmin = 3.8,
    b_lmax = 4.0,
    bl_lmin = 5.8,
    bl_lmax = 6.2,
    hmax = 2.0,
    tl_min = 0.4,
    tl_max = 1.27,
    tw_min = 0.36,
    tw_max = 0.48,
    pitch = 1.27,
)

generateSMDPadDims(nil, ssop)