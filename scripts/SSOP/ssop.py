#!/usr/bin/env python

import sys
import os


sys.path.append("..\\..")
from KicadModTree import * # NOQA
from KicadModTree.nodes.specialized.PadArray import PadArray
from KicadModTree.nodes.base.Pad import Pad
import KicadModTree.Rules as rules

# Pin Count, Lmin, Lmax,  Wmin, Wmax, W+pins_min, W+pin_max, Hmax, Pitch
ssop_pkgs = [
[16, 5.90,   6.50,   5.00,  5.60,  7.40,  8.20,  2.0,  0.65],  # SSOP-16
[16, 4.801,  4.978,  3.810, 3.988, 5.817, 6.198, 2.0,  0.635], # SSOP-16-N
[20, 6.90,   7.50,   5.00,  5.60,  7.40,  8.20,  2.0,  0.65],  # SSOP-20
[20, 8.560,  8.738,  3.810, 3.988, 5.817, 6.198, 2.0,  0.635], # SSOP-20-N
[24, 8.560,  8.738,  3.810, 3.988, 5.817, 6.198, 2.0,  0.635], # SSOP-24-N
[24, 7.90,   8.50,   5.00,  5.60,  7.40,  8.20,  2.0,  0.65],  # SSOP-24
[28, 9.90,   10.50,  5.00,  5.60,  7.40,  8.20,  2.0,  0.65],  # SSOP-28
[28, 9.804,  9.982,  3.810, 3.988, 5.817, 6.198, 1.75, 0.635], # SSOP-28-N
[36, 12.50,  13.10,  5.00,  5.60,  7.40,  8.20,  2.0,  0.65],  # SSOP-36
[36, 15.291, 15.545, 7.417, 7.595, 10.11, 10.55, 2.64, 0.80],  # SSOP-36-W
[44, 12.50,  13.10,  5.00,  5.60,  7.40,  8.20,  2.0,  0.50],  # SSOP-44
[44, 17.73,  17.93,  7.417, 7.595, 10.11, 10.55, 2.64, 0.80],  # SSOP-44-W
[48, 12.50,  13.10,  5.00,  5.60,  7.40,  8.20,  2.0,  0.50],  # SSOP-48
]

# courtyard = COURTYARD_TYPE()
prefix = "SSOP-"

desc = "SSOP package, {pnum}"
# ssop lead dimensions; used for fabrication outlines of pads
# length, width; 0.05mm line width fab layer; measurements are maximums
ssop_lead_dims = [0.95, 0.38]



for ssop_pkg in ssop_pkgs:
    
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