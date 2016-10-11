#!/usr/bin/env python

import sys
import os
from collections import namedtuple


sys.path.append("..\\..")
from KicadModTree import * # NOQA
from KicadModTree.nodes.specialized.PadArray import PadArray
from KicadModTree.nodes.base.Pad import Pad
import KicadModTree.Rules as rules

Params = namedtuple("Params", [
    'pins',
    'lmin',
    'lmax',
    'wmin',
    'wmax',
    'wpmin',
    'wpmax',
    'hmax',
    'pitch'
])

ssop = {}

ssop['16'] = Params(
    pins = 16,
    
    lmin = 5.90,
    lmax = 6.50,

    wmin = 5.00,
    wmax = 5.60,

    wpmin = 7.40,
    wpmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['16-N'] = Params(
    pins = 16,
    
    lmin = 4.801,
    lmax = 4.978,

    wmin = 3.810,
    wmax = 3.988,

    wpmin = 5.817,
    wpmax = 6.198,

    hmax = 2.0,

    pitch = 0.635,
)

ssop['20'] = Params(
    pins = 20,
    
    lmin = 6.90,
    lmax = 7.50,

    wmin = 5.00,
    wmax = 5.60,

    wpmin = 7.40,
    wpmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['20-N'] = Params(
    pins = 20,
    
    lmin = 8.560,
    lmax = 8.738,

    wmin = 3.810,
    wmax = 3.988,

    wpmin = 5.817,
    wpmax = 6.198,

    hmax = 2.0,

    pitch = 0.635,
)

ssop['24-N'] = Params(
    pins = 24,
    
    lmin = 8.560,
    lmax = 8.738,

    wmin = 3.810,
    wmax = 3.988,

    wpmin = 5.817,
    wpmax = 6.198,

    hmax = 2.0,

    pitch = 0.635,
)

ssop['24'] = Params(
    pins = 24,
    
    lmin = 7.90,
    lmax = 8.50,

    wmin = 5.00,
    wmax = 5.60,

    wpmin = 7.40,
    wpmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['28'] = Params(
    pins = 28,
    
    lmin = 9.90,
    lmax = 10.50,

    wmin = 5.00,
    wmax = 5.60,

    wpmin = 7.40,
    wpmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['28-N'] = Params(
    pins = 28,
    
    lmin = 9.804,
    lmax = 9.982,

    wmin = 3.810,
    wmax = 3.988,

    wpmin = 5.817,
    wpmax = 6.198,

    hmax = 1.75,

    pitch = 0.635,
)

ssop['36'] = Params(
    pins = 36,
    
    lmin = 12.50,
    lmax = 13.10,

    wmin = 5.00,
    wmax = 5.60,

    wpmin = 7.40,
    wpmax = 8.20,

    hmax = 2.0,

    pitch = 0.65,
)

ssop['36-W'] = Params(
    pins = 36,
    
    lmin = 15.291,
    lmax = 15.545,

    wmin = 7.417,
    wmax = 7.595,

    wpmin = 10.11,
    wpmax = 10.55,

    hmax = 2.64,

    pitch = 0.80,
)

ssop['44'] = Params(
    pins = 44,
    
    lmin = 12.50,
    lmax = 13.10,

    wmin = 5.00,
    wmax = 5.60,

    wpmin = 7.40,
    wpmax = 8.20,

    hmax = 2.0,

    pitch = 0.50,
)

ssop['44-W'] = Params(
    pins = 44,
    
    lmin = 17.73,
    lmax = 17.93,

    wmin = 7.417,
    wmax = 7.595,

    wpmin = 10.11,
    wpmax = 10.55,

    hmax = 2.64,

    pitch = 0.80,
)

ssop['48'] = Params(
    pins = 48,
    
    lmin = 12.50,
    lmax = 13.10,

    wmin = 5.00,
    wmax = 5.60,

    wpmin = 7.40,
    wpmax = 8.20,

    hmax = 2.0,

    pitch = 0.50,
)

# Pin Count, Lmin, Lmax,  Wmin, Wmax, W+pins_min, W+pin_max, Hmax, Pitch

dlevels = namedtuple("dlevels", [
    LevelA,
    LevelB,
    LevelC,
])

dattr = namedtuple("dattr", [
    'toe',
    'toe_round',
    'heel',
    'heel_round',
    'side',
    'side_round',
    'crtyd_ex',
])

ssop['0.50'] = dlevels(
    LevelA['A'] = dattr(
        toe = 0.55,
        toe_round = '0.2f',
        heel = 0.45,
        heel_round = '0.2f',
        side = 0.05,
        side_round = '0.2f',
        crtyd_ex = 0.5,
    ),
    LevelB['B'] = dattr(
        toe = 0.55,
        toe_round = '0.2f',
        heel = 0.45,
        heel_round = '0.2f',
        side = 0.05,
        side_round = '0.2f',
        crtyd_ex = 0.5,
    ),
    LevelC['C'] = dattr(
        toe = 0.55,
        toe_round = '0.2f',
        heel = 0.45,
        heel_round = '0.2f',
        side = 0.05,
        side_round = '0.2f',
        crtyd_ex = 0.5,
    ),
)

ssop['0.635'] = dlevels(
    LevelA['A'] = dattr(
        toe = 0.55,
        toe_round = '0.2f',
        heel = 0.45,
        heel_round = '0.2f',
        side = 0.05,
        side_round = '0.2f',
        crtyd_ex = 0.5,
    ),
    LevelB['B'] = dattr(
        toe = 0.55,
        toe_round = '0.2f',
        heel = 0.45,
        heel_round = '0.2f',
        side = 0.05,
        side_round = '0.2f',
        crtyd_ex = 0.5,
    ),
    LevelC['C'] = dattr(
        toe = 0.55,
        toe_round = '0.2f',
        heel = 0.45,
        heel_round = '0.2f',
        side = 0.05,
        side_round = '0.2f',
        crtyd_ex = 0.5,
    ),
)

# ssop['0.65'] = dlevels(
#     LevelA = [],
#     LevelB = [],
#     LevelC = [],
# )

# ssop['0.80'] = dlevels(
#     LevelA = [],
#     LevelB = [],
#     LevelC = [],
# )
# courtyard = COURTYARD_TYPE()
prefix = "SSOP-"

desc = "SSOP package, {pnum}"
# ssop lead dimensions; used for fabrication outlines of pads
# length, width; 0.05mm line width fab layer; measurements are maximums
ssop_lead_dims = [0.95, 0.38]



for k in ssop.keys():
    
    # extract information
    pnum, lmin, lmax, wmin, wmax, wpmin, wpmax, hmax, pitch = ssop_pkg
    nominal_l, nominal_w = ((lmax - lmin) / 2 + lmin), ((wmax - wmin) / 2 + wmin)    
    pins = "{pnum}_".format(pnum=pnum)
    dims = "{nominal_l:0.1f}x{nominal_w:0.1f}mm".format(nominal_l=nominal_l, nominal_w=nominal_w)
    # set pad layers
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
    pin_y_pos = (wpmax-wmax)/2+wmax
    pin_y_neg = -(wpmax-wmax)/2-wmax
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
    kicad_mod.append(RectLine(start=[lmax/2, -wmax/2], end=[-lmax/2, wmax/2], layer='F.Fab', width=0.15))

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