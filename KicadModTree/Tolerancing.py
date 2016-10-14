from math import sqrt

PART_PLACEMENT_TOL = 0.1
PCB_LAND_FAB_TOL = 0.1

def RMS(*args):
    rms = 0
    for arg in args:
        rms += arg*arg
    return sqrt(rms)

def generateGullWingPadDims(GullWingParams, JointParams):

    try:
        toe, heel, side, crtyd_ex = JointParams
    except:
        "Not a valid set of params"
    
    try:
        pins, b_wmin, b_wmax, b_lmin, b_lmax, bl_lmin, bl_lmax, hmax, tl_min, tl_max, tw_min, tw_max, pitch = GullWingParams
    except: 
        "Not a valid set of params"

    Ltol = bl_lmax - bl_lmin
    Ttol = tl_max - tl_min
    Wtol = tw_max - tw_min
    Stol = sqrt(Ltol**2+2*Ttol**2)

    Smin = bl_lmin - 2 * tl_max
    Smax = Smin + Stol

    Gmin = Smax - 2*heel - RMS(Stol, PART_PLACEMENT_TOL, PCB_LAND_FAB_TOL)

    Xmax = tw_min + 2*side + RMS(Wtol, PART_PLACEMENT_TOL, PCB_LAND_FAB_TOL)

    Zmax = bl_lmin + 2*toe + RMS(Ltol, PART_PLACEMENT_TOL, PCB_LAND_FAB_TOL)

    pad_y = (Zmax - Gmin) / 2
    pad_x = Xmax

    print pad_x, pad_y