#!/usr/bin/env python

import sys
import os
from collections import namedtuple

sys.path.append("..\\..")
from KicadModTree import * # NOQA
from KicadModTree.nodes.specialized.PadArray import PadArray
from KicadModTree.nodes.base.Pad import Pad
from KicadModTree.Tolerancing import generateGullWingPadDims
from KicadModTree.PackageDimensioning import getPackageDims
import KicadModTree.Rules as rules

DEFAULT_DENSITY_LEVEL = 'B' # Nominal

desc = "SSOP package, {fp.n}"

ssop = getPackageDims('GullWingParams', 'SSOP')
layers = ["F.Cu", "F.Paste", "F.Mask"]

for k in ssop:
    
    fp = ssop[k]

    # get nominal dimensions
    D_nominal = (fp.D_max - fp.D_min) + fp.D_min
    E1_nominal = (fp.E1_max - fp.E1_min) + fp.E1_min
    
    fpname = fp.name + "_{l}x{w}mm_{p}mmPitch".format(pins=fp.n, l=D_nominal, w=E1_nominal, p=fp.e)
    filename = fpname + ".kicad_mod" 
    kicad_mod = Footprint(fpname)
    kicad_mod.setDescription("test")
    kicad_mod.setAttribute("smd")
    kicad_mod.setTags("test")

    kicad_mod.append(Text(type='reference', 
                          text='REF**', 
                          at=[0, -3], 
                          layer='F.SilkS'))
    kicad_mod.append(Text(type='value', 
                          text=fp.name, 
                          at=[0, 0], 
                          layer='F.Fab'))

    # if ZERO_ORIENTATION == 'LevelA': # pin 1 in upper left corner
    #     l,w = w,l
    # else 'LevelB': # pin 1 in lower left corner; rotated 90 from LevelA
    #     continue   # do nothing, by default pads are LevelB

    pin_y_pos = (fp.E_max - fp.E1_max) / 2 + fp.E1_max
    pin_y_neg = -(fp.E_max - fp.E1_max) / 2 - fp.E1_max
    pad_l_start = [ -(fp.e * fp.n / 4 - fp.e / 2), pin_y_pos / 2 ]
    pad_r_start = [ -(fp.e * fp.n / 4 - fp.e / 2), -pin_y_pos / 2 ]

    # get pad measurements
    pad_x, pad_y = generateGullWingPadDims(fp, 'SSOP', DEFAULT_DENSITY_LEVEL)

    # draw the pads
    pad_num_r_start = fp.n/2 + 1
    pa_left = PadArray(pincount=fp.n/2, 
                       intial=1, 
                       start=pad_l_start, 
                       increment=1, 
                       layers=layers, 
                       shape=Pad.SHAPE_ROUNDRECT, 
                       roundrect_rratio=0.25, 
                       type = Pad.TYPE_SMT, 
                       size = [pad_x, pad_y], 
                       x_spacing = fp.e)

    pa_right = PadArray(pincount=fp.n/2, 
                        initial=fp.n, 
                        start=pad_r_start, 
                        increment=-1, 
                        layers=layers, 
                        shape=Pad.SHAPE_ROUNDRECT, 
                        roundrect_rratio=0.25, 
                        type=Pad.TYPE_SMT, 
                        size = [pad_x, pad_y], 
                        x_spacing = fp.e)

    kicad_mod.append(pa_left)
    kicad_mod.append(pa_right)

    # create silkscreen
    silkline = Line(start=Point(-fp.D_max/2, pin_y_pos), 
                    end=Point(-fp.D_max/2, pin_y_neg), 
                    layer="F.SilkS", 
                    width=0.15)

    kicad_mod.append(silkline)
    # add designator for pin #1

    # draw the courtyard

    # kicad_mod.append(RectLine(start=[], end=[], layer='F.CrtYd'))

    # draw the fabrication outline
    kicad_mod.append(RectLine(start=[fp.D_max/2, -fp.E1_max/2], 
                              end=[-fp.D_max/2, fp.E1_max/2], 
                              layer='F.Fab', 
                              width=0.15))

    # draw fab outlines for pads if selected as option
    # **TODO** if DRAW_PAD_FAB:
        
    # **TODO** Have it get the zero orientation first

    # add model
    kicad_mod.append(Model(filename="${{KISYS3DMOD}}/Housings_SSOP/{fp_name}.{model_type}".format(
                           fp_name = fp.name, 
                           model_type = rules.MODEL_3D_TYPE, 
                           at=[0, 0, 0], 
                           scale=[1, 1, 1], 
                           rotate=[0, 0, 0])))

    print(kicad_mod.getCompleteRenderTree())

    # write file
    file_handler = KicadFileHandler(kicad_mod)
    file_handler.writeFile(filename)