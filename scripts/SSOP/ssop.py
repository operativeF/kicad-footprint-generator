#!/usr/bin/env python

import sys
import os
from collections import namedtuple


sys.path.append("..\\..")
from KicadModTree import * # NOQA
from KicadModTree.nodes.specialized.PadArray import PadArray
from KicadModTree.nodes.base.Pad import Pad
import KicadModTree.Rules as rules

DEFAULT_DENSITY_LEVEL = 'B' # Nominal

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

ssop = {}

ssop['16'] = Params(
    pins = 16,
    
    b_wmin = 5.90,
    b_wmax = 6.50,

    b_lmin = 5.00,
    b_lmax = 5.60,

    bl_lmin = 7.40,
    bl_lmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['16-N'] = Params(
    pins = 16,
    
    b_wmin = 4.801,
    b_wmax = 4.978,

    b_lmin = 3.810,
    b_lmax = 3.988,

    bl_lmin = 5.817,
    bl_lmax = 6.198,

    hmax = 2.0,

    pitch = 0.635,
)

ssop['20'] = Params(
    pins = 20,
    
    b_wmin = 6.90,
    b_wmax = 7.50,

    b_lmin = 5.00,
    b_lmax = 5.60,

    bl_lmin = 7.40,
    bl_lmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['20-N'] = Params(
    pins = 20,
    
    b_wmin = 8.560,
    b_wmax = 8.738,

    b_lmin = 3.810,
    b_lmax = 3.988,

    bl_lmin = 5.817,
    bl_lmax = 6.198,

    hmax = 2.0,

    pitch = 0.635,
)

ssop['24-N'] = Params(
    pins = 24,
    
    b_wmin = 8.560,
    b_wmax = 8.738,

    b_lmin = 3.810,
    b_lmax = 3.988,

    bl_lmin = 5.817,
    bl_lmax = 6.198,

    hmax = 2.0,

    pitch = 0.635,
)

ssop['24'] = Params(
    pins = 24,
    
    b_wmin = 7.90,
    b_wmax = 8.50,

    b_lmin = 5.00,
    b_lmax = 5.60,

    bl_lmin = 7.40,
    bl_lmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['28'] = Params(
    pins = 28,
    
    b_wmin = 9.90,
    b_wmax = 10.50,

    b_lmin = 5.00,
    b_lmax = 5.60,

    bl_lmin = 7.40,
    bl_lmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['28-N'] = Params(
    pins = 28,
    
    b_wmin = 9.804,
    b_wmax = 9.982,

    b_lmin = 3.810,
    b_lmax = 3.988,

    bl_lmin = 5.817,
    bl_lmax = 6.198,

    hmax = 1.75,

    pitch = 0.635,
)

ssop['36'] = Params(
    pins = 36,
    
    b_wmin = 12.50,
    b_wmax = 13.10,

    b_lmin = 5.00,
    b_lmax = 5.60,

    bl_lmin = 7.40,
    bl_lmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['36-W'] = Params(
    pins = 36,
    
    b_wmin = 15.291,
    b_wmax = 15.545,

    b_lmin = 7.417,
    b_lmax = 7.595,

    bl_lmin = 10.11,
    bl_lmax = 10.55,

    hmax = 2.64,

    pitch = 0.80,
)

ssop['44'] = Params(
    pins = 44,
    
    b_wmin = 12.50,
    b_wmax = 13.10,

    b_lmin = 5.00,
    b_lmax = 5.60,

    bl_lmin = 7.40,
    bl_lmax = 8.20,

    hmax = 2.0,

    pitch = 0.50,
)

ssop['44-W'] = Params(
    pins = 44,
    
    b_wmin = 17.73,
    b_wmax = 17.93,

    b_lmin = 7.417,
    b_lmax = 7.595,

    bl_lmin = 10.11,
    bl_lmax = 10.55,

    hmax = 2.64,

    pitch = 0.80,
)

ssop['48'] = Params(
    pins = 48,
    
    b_wmin = 12.50,
    b_wmax = 13.10,

    b_lmin = 5.00,
    b_lmax = 5.60,

    bl_lmin = 7.40,
    bl_lmax = 8.20,

    hmax = 2.0,

    pitch = 0.50,
)

# Pin Count, b_wmin, b_wmax,  b_lmin, b_lmax, W+pins_min, W+pin_max, Hmax, Pitch

d_params = namedtuple("d_params", [
    'toe',
    'toe_round',
    'heel',
    'heel_round',
    'side',
    'side_round',
    'court_ex',
])

d_levels = {}

d_levels['A_gt_0.625mm'] = d_params(
    toe = 0.55,
    toe_round = '0.2f',
    heel = 0.45,
    heel_round = '0.2f',
    side = 0.05,
    side_round = '0.2f',
    court_ex = 0.5,
)

d_levels['B_gt_0.625mm'] = d_params(
    toe = 0.35,
    toe_round = '0.2f',
    heel = 0.35,
    heel_round = '0.2f',
    side = 0.02,
    side_round = '0.2f',
    court_ex = 0.25,
)

d_levels['C_gt_0.625mm'] = d_params(
    toe = 0.15,
    toe_round = '0.2f',
    heel = 0.25,
    heel_round = '0.2f',
    side = 0.01,
    side_round = '0.2f',
    court_ex = 0.1,
)

d_levels['A_lt_0.625mm'] = d_params(
    toe = 0.55,
    toe_round = '0.2f', # two place even decimal
    heel = 0.45,
    heel_round = '0.1f',
    side = 0.01,
    side_round = '0.2f',
    court_ex = 0.5,
)

d_levels['B_lt_0.625mm'] = d_params(
    toe = 0.35,
    toe_round = '0.2f', # two place even decimal
    heel = 0.35,
    heel_round = '0.2f',
    side = -0.02,
    side_round = '0.2f',
    court_ex = 0.25,
)

d_levels['C_lt_0.625mm'] = d_params(
    toe = 0.15,
    toe_round = '0.2f',
    heel = 0.25,
    heel_round = '0.2f',
    side = -0.04,
    side_round = '0.2f',
    court_ex = 0.1,
)

prefix = "SSOP-"

desc = "SSOP package, {pnum}"
# ssop lead dimensions; used for fabrication outlines of pads
# length, width; 0.05mm line width fab layer; measurements are maximums
ssop_lead_dims = [0.95, 0.38]

for k in ssop.keys():
    
    prop = ssop[k]

    name = prefix + k + 

    layers = ["F.Cu", "F.Paste", "F.Mask"]

    footprint_name = prefix + pins + dims

    kicad_mod = Footprint(footprint_name)
    kicad_mod.setDescription("test")
    kicad_mod.setAttribute("smd")
    kicad_mod.setTags("test")

    kicad_mod.append(Text(type='reference', text='REF**', at=[0, -3], layer='F.SilkS'))
    kicad_mod.append(Text(type='value', text=footprint_name, at=[1.5, 3], layer='F.Fab'))

    
    # **TODO** Implement zero orientation function
    # if ZERO_ORIENTATION == 'LevelA': # pin 1 in upper left corner
    #     l,w = w,l
    # else 'LevelB': # pin 1 in lower left corner; rotated 90 from LevelA
    #     continue
    pin_y_pos = (bl_lmax-b_lmax)/2+b_lmax
    pin_y_neg = -(bl_lmax-b_lmax)/2-b_lmax
    pad_l_start = [-(pitch*pnum/4-pitch/2), pin_y_pos/2]
    pad_r_start = [-(pitch*pnum/4-pitch/2), -pin_y_pos/2]

    pad_num_r_start = pnum/2 + 1
    # draw the pads
    pa_left = PadArray(pincount=pnum/2, intial=1, start=pad_l_start, increment=1, layers=layers, shape=Pad.SHAPE_ROUNDRECT, roundrect_ratio=0.25, type = Pad.TYPE_SMT, size = [0.4, 1.2], x_spacing = pitch)
    pa_right = PadArray(pincount=pnum/2, initial=pnum, start=pad_r_start, increment=-1, layers=layers, shape=Pad.SHAPE_ROUNDRECT, roundrect_ratio=0.25, type=Pad.TYPE_SMT, size=[0.4, 1.2], x_spacing = pitch)
    kicad_mod.append(pa_left)
    kicad_mod.append(pa_right)

    # create silkscreen
    # kicad_mod.append()

    # add designator for pin #1

    # draw the courtyard

    # kicad_mod.append(RectLine(start=[], end=[], layer='F.CrtYd'))

    # draw the fabrication outline
    kicad_mod.append(RectLine(start=[b_wmax/2, -b_lmax/2], end=[-b_wmax/2, b_lmax/2], layer='F.Fab', width=0.15))

    # draw fab outlines for pads if selected as option
    # **TODO** if DRAW_PAD_FAB:
        
    # **TODO** Have it get the zero orientation first

    # add model
    kicad_mod.append(Model(filename="Housings_SSOP/{fp_name}.{model_type}".format(fp_name = footprint_name, model_type = rules.MODEL_3D_TYPE),
                           at=[0, 0, 0], scale=[1, 1, 1], rotate=[0, 0, 0]))

    print(kicad_mod.getCompleteRenderTree())

    filename = prefix + "{pins}{l}x{w}mm_{p}mm".format(pins=pins, l=nominal_l, w=nominal_w, p=pitch) + ".kicad_mod"
    # write file
    file_handler = KicadFileHandler(kicad_mod)
    file_handler.writeFile(filename)