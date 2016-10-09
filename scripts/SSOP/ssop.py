#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.join(sys.path[0], "../.."))  # enable package import from parent directory


from KicadModTree import * # NOQA
from KicadModTree.Rules import *
# from KicadModTree.nodes.specialized.PadArray import PadArray

pitch = 0.65


if __name__ == '__main__':
    
    footprint_name = 
    
    pad_w = 
    pad_h = 

    kicad_mod = Footprint(footprint_name)
    kicad_mod.setDescription("")
    kicad_mod.setTags("")

    kicad_mod.append(Text(type='reference', text='REF**', at=[0, -3], layer='F.SilkS'))
    kicad_mod.append(Text(type='value', text=footprint_name, at=[1.5, 3], layer='F.Fab'))

    # create silkscreen
    kicad_mod.append()

    # add designator for pin #1

    # add courtyard
    kicad_mod.append(RectLine(start=[], end=[], layer='F.CrtYd'))

    # create pads
    
    # add model
    kicad_mod.append(Model(filename="Housings_SSOP/{footprint_name}.{model_type}",
                           at=[0, 0, 0], scale=[1, 1, 1], rotate=[0, 0, 0]))

    print(kicad_mod.getCompleteRenderTree())

    # write file
    file_handler = KicadFileHandler(kicad_mod)
    file_handler.writeFile("")