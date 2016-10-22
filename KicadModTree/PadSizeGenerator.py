from math import sqrt
from openpyxl import load_workbook
from collections import namedtuple

PART_PLACEMENT_TOL = 0.025
PCB_LAND_FAB_TOL = 0.05

def getJointParams(pkgtype, pitch, densitylvl):
    wb = load_workbook('C:/KicadRepo/kicad-footprint-generator/KicadModTree/JointParams.xlsx')
    if pkgtype in ['SOIC', 'SSOP', 'SOP', 'QFP']:
        sheet = wb.get_sheet_by_name('SOP_QFP')
        joints = namedtuple('joint', [
            'toe',
            'heel',
            'side',
            'crtyd_ex',
        ])
        if pitch > 1.00:
            set_row = '3'
        elif pitch > 0.80 and pitch <= 1.00:
            set_row = '4'
        elif pitch > 0.65 and pitch <= 0.80:
            set_row = '5'
        elif pitch > 0.50 and pitch <= 0.65:
            set_row = '6'
        elif pitch > 0.40 and pitch <= 0.50:
            set_row = '7'
        elif pitch < 0.40:
            set_row = '8'
        else:
            return "Invalid parameter"
        
        if densitylvl == 'A':
            set_range = "JKLM"
        elif densitylvl == 'B':
            set_range = "FGHI"
        elif densitylvl == 'C':
            set_range = "BCDE"
        else:
            return "Invalid range"
        tv = set_range[0] + set_row
        hv = set_range[1] + set_row
        sv = set_range[2] + set_row
        cv = set_range[3] + set_row

        jointparams = joints(
        toe = sheet[("{}".format(tv))].value,
        heel = sheet[("{}".format(hv))].value,
        side = sheet[("{}".format(sv))].value,
        crtyd_ex = sheet[("{}".format(cv))].value,
        )

        return jointparams

def generateGullWingPadDims(pkgparams, pkgtype, dlvl):

    densitylevel = getJointParams(pkgtype, pkgparams.e, dlvl)

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

    n_Smin = Smin + Sdiff / 2
    n_Smax = Smax - Sdiff / 2

    Htol = sqrt((n_Smax - n_Smin)**2 + (2* PART_PLACEMENT_TOL)**2 + (2 * PCB_LAND_FAB_TOL)**2)

    Gmin = n_Smax - 2*densitylevel.heel - Htol
    Xmax = pkgparams.b_min + 2*densitylevel.side + Wtol
    Zmax = pkgparams.E_min + 2*densitylevel.toe + Ltol

    pad_y = round((((Zmax - Gmin) / 2) * (1 / PCB_LAND_FAB_TOL)), 0) / (1 / PCB_LAND_FAB_TOL)
    pad_x = round(Xmax * (1 / PCB_LAND_FAB_TOL), 0) / (1 / PCB_LAND_FAB_TOL)

    return pad_x, pad_y

def generatePthPadDims(comparams, densitylvl):
    SPOKE_QTY = 4
    MINIMUM_ANNULAR_RING = 0.05
    SPOKE_WIDTH_PERCENTAGE = 0.75

    drill_size = comparams.max_lead_d + densitylvl.hole_over_lead
    pad_diameter = 2 * (MINIMUM_ANNULAR_RING) + (densitylvl.min_fab_allow) + (comparams.max_lead_d) + (densitylvl.hole_over_lead)
    
    thermal_spoke_w = (SPOKE_WIDTH_PERCENTAGE * drill_size) / SPOKE_QTY
    pad_thermal_id = densitylvl.thermal_id + pad_diameter
    pad_thermal_od = densitylvl.thermal_od + pad_diameter
    pad_thermal_gap = pad_thermal_od - pad_thermal_id

    