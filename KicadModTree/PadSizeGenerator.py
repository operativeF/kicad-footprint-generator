from math import sqrt
from collections import namedtuple

PART_PLACEMENT_TOL = 0.025
PCB_LAND_FAB_TOL = 0.05
INV_PART_PLACEMENT_TOL = 1 / PART_PLACEMENT_TOL
INV_PCB_LAND_FAB_TOL = 1 / PCB_LAND_FAB_TOL

def generateSMDPadDims(pkgparams, jointparams):

    toe, heel, side, crtyd_ex = jointparams

    Ltol = sqrt((pkgparams.Emax - pkgparams.Emin)**2 + (2 * PCB_LAND_FAB_TOL)**2 + (2 * PART_PLACEMENT_TOL)**2)
    Wtol = sqrt((pkgparams.bmax - pkgparams.bmin)**2 + (2 * PCB_LAND_FAB_TOL)**2 + (2 * PART_PLACEMENT_TOL)**2)
    Stol_rms = sqrt((pkgparams.Emax - pkgparams.Emin)**2 + 2 * (pkgparams.Lmax - pkgparams.Lmin)**2)

    Smin = pkgparams.Emin - 2 * pkgparams.Lmax
    Smax = pkgparams.Emax - 2 * pkgparams.Lmin

    Stol = Smax - Smin
    Sdiff = Stol - Stol_rms

    n_Smin = Smin + Sdiff / 2
    n_Smax = Smax - Sdiff / 2

    Htol = sqrt((n_Smax - n_Smin)**2 + (2* PART_PLACEMENT_TOL)**2 + (2 * PCB_LAND_FAB_TOL)**2)

    Gmin = n_Smax - 2*heel - Htol
    Xmax = pkgparams.bmin + 2*side + Wtol
    Zmax = pkgparams.Emin + 2*toe + Ltol

    pad_y = round((((Zmax - Gmin) / 2) * INV_PCB_LAND_FAB_TOL), 0) / INV_PCB_LAND_FAB_TOL
    pad_x = round(Xmax * INV_PCB_LAND_FAB_TOL, 0) / INV_PCB_LAND_FAB_TOL

    return pad_x, pad_y

def generatePTHPadDims(comparams, densitylvl):
    SPOKE_QTY = 4
    MINIMUM_ANNULAR_RING = 0.05
    SPOKE_WIDTH_PERCENTAGE = 0.75

    drill_size = comparams.max_lead_d + densitylvl.hole_over_lead
    pad_diameter = 2 * (MINIMUM_ANNULAR_RING) + (densitylvl.min_fab_allow) + (comparams.max_lead_d) + (densitylvl.hole_over_lead)
    
    thermal_spoke_w = (SPOKE_WIDTH_PERCENTAGE * drill_size) / SPOKE_QTY
    pad_thermal_id = densitylvl.thermal_id + pad_diameter
    pad_thermal_od = densitylvl.thermal_od + pad_diameter
    pad_thermal_gap = pad_thermal_od - pad_thermal_id

# def generate_BGA_PadDims():

# def generate_LGA_PadDims():

# def generate_CGA_PadDims():

# def generateUnderbodyPadDims():

# def generateNPTHPadDims():