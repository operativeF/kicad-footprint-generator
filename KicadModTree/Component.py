import sys
import os
from collections import namedtuple

sys.path.append("..")
from KicadModTree import * # NOQA
from KicadModTree.nodes.specialized.PadArray import PadArray
from KicadModTree.nodes.base.Pad import Pad
from KicadModTree.PadSizeGenerator import generateSMDPadDims
import KicadModTree.Rules as rules

pkgparams = namedtuple("Params", [
    'Dmin',
    'Dmax',
    'E1min',
    'E1max',
    'Emin',
    'Emax',
    'Amax',
    'Lmin',
    'Lmax',
    'bmin',
    'bmax',
    'e',
    'npx',
    'npy',
    'fN',
    'ort',
    'epad'
])

chipparams = namedtuple("Params", [
])

def make_pkg_comp(params, **kwargs):

    # descr = descr
    # density_level = density_level
    
    layers = ["F.Cu", "F.Paste", "F.Mask"]

    Dmin = params.Dmin
    Dmax = params.Dmax
    E1min = params.E1min
    E1max = params.E1max
    Emin = params.Emin
    Emax = params.Emax
    Amax = params.Amax
    Lmin = params.Lmin
    Lmax = params.Lmax
    bmin = params.bmin
    bmax = params.bmax
    e = params.e
    npx = params.npx
    npy = params.npy
    fN  = params.fN
    ZERO_ORIENTATION = params.ort

    Dnom = (Dmax - Dmin) + Dmin
    E1nom = (E1max - E1min) + E1min

    if params.epad:
        D2min = params.epad[0]
        D2max = params.epad[1]
        E2min = params.epad[2]
        E2max = params.epad[3]
    
    # get nominal dimensions
    Dnom = ( Dmax - Dmin ) + Dmin
    E1nom = ( E1max - E1min ) + E1min

    # get footprint name
    fpName = fN
    kicad_mod = Footprint(fN)

    kicad_mod.setDescription("test")
    kicad_mod.setAttribute("smd")
    kicad_mod.setTags("test")

    kicad_mod.append(Text(type='reference', 
                          text='REF**', 
                          at=[0, -3], 
                          layer='F.SilkS'))

    # get text reference size so it fits in the fab layer 
    # get length of reference Text
    # text_size = round(text_length / Dmin, 1) - 0.1
    # size = [text_size, text_size]
    # text_width = 0.1 * text_size

    kicad_mod.append(Text(type='value', 
                          text=fN, 
                          at=[0, 0], 
                          layer='F.Fab'))
    
    pin_y_pos = (Emax - E1max) / 2 + E1max
    pin_y_neg = -(Emax - E1max) / 2 - E1max

    # get pad measurements
    pad_x, pad_y = generateSMDPadDims(params)

    # draw the pads
    
    # Dual row package, pin 1 in upper left corner; Zero Orientation Level B
    if (npx and ZERO_ORIENTATION == 'B') and (not npy): 

        center_left = [pin_y_neg / 2, 0]
        center_right = [pin_y_pos / 2, 0]
        x_space = 0
        y_space = e
        pad_x, pad_y = pad_y, pad_x

        pa_left = PadArray(pincount=npx, 
                           intial = 1, 
                           center = center_left,
                           increment = 1, 
                           layers = layers, 
                           shape = Pad.SHAPE_ROUNDRECT, 
                           roundrect_rratio = 0.25, 
                           type = Pad.TYPE_SMT, 
                           size = [pad_x, pad_y], 
                           x_spacing = x_space,
                           y_spacing = y_space
        )
        pa_right = PadArray(pincount = npx, 
                            initial = npx * 2, 
                            center = center_right,
                            increment = -1, 
                            layers = layers, 
                            shape = Pad.SHAPE_ROUNDRECT, 
                            roundrect_rratio = 0.25, 
                            type = Pad.TYPE_SMT, 
                            size = [pad_x, pad_y], 
                            x_spacing = x_space,
                            y_spacing = y_space
        )
        kicad_mod.append(pa_left)
        kicad_mod.append(pa_right)

    # Dual row package, pin 1 in upper left corner; Zero Orientation Level A
    if (npx and ZERO_ORIENTATION == 'A') and (not npy):

        center_left = [0, pin_y_pos / 2]
        center_right = [0, pin_y_neg / 2]
        x_space = e
        y_space = 0

        pa_left = PadArray(pincount=npx, 
                           intial = 1, 
                           center = center_left,
                           increment = 1, 
                           layers = layers, 
                           shape = Pad.SHAPE_ROUNDRECT, 
                           roundrect_rratio = 0.25, 
                           type = Pad.TYPE_SMT, 
                           size = [pad_x, pad_y], 
                           x_spacing = x_space,
                           y_spacing = y_space)

        pa_right = PadArray(pincount = npx, 
                            initial = npx * 2, 
                            center = center_right,
                            increment = -1, 
                            layers = layers, 
                            shape = Pad.SHAPE_ROUNDRECT, 
                            roundrect_rratio = 0.25, 
                            type = Pad.TYPE_SMT, 
                            size = [pad_x, pad_y], 
                            x_spacing = x_space,
                            y_spacing = y_space)

        kicad_mod.append(pa_left)
        kicad_mod.append(pa_right)

    # Quad row package, pin 1 lower left corner, Zero Orientation Level A
    if (npx and npy and ZERO_ORIENTATION == 'A'):
        center_left = [pin_y_neg / 2, 0]
        center_right = [pin_y_pos / 2, 0]
        center_top = [0, pin_y_neg / 2]
        center_bottom = [0, pin_y_pos / 2]

        pa_left = PadArray(pincount=npx,
                           initial = 2 * npx + npy + 1,
                           center = center_left,
                           increment = 1, 
                           layers = layers, 
                           shape = Pad.SHAPE_ROUNDRECT, 
                           roundrect_rratio = 0.25, 
                           type = Pad.TYPE_SMT, 
                           size = [pad_y, pad_x], 
                           x_spacing = 0,
                           y_spacing = e)

        pa_right = PadArray(pincount = npx, 
                            initial = 2 * npx, # 2 * npx + npy, 
                            center = center_right,
                            increment = -1, 
                            layers = layers, 
                            shape = Pad.SHAPE_ROUNDRECT, 
                            roundrect_rratio = 0.25, 
                            type = Pad.TYPE_SMT, 
                            size = [pad_y, pad_x], 
                            x_spacing = 0,
                            y_spacing = e)

        pa_bottom = PadArray(pincount = npy, 
                            initial = 1, # npx + 1, 
                            center = center_bottom,
                            increment = 1, 
                            layers = layers, 
                            shape = Pad.SHAPE_ROUNDRECT, 
                            roundrect_rratio = 0.25, 
                            type = Pad.TYPE_SMT, 
                            size = [pad_x, pad_y], 
                            x_spacing = e,
                            y_spacing = 0)

        pa_top = PadArray(pincount = npy, 
                            initial = 2 * npx + npy, # 2 * npx + 2 * npy, 
                            center = center_top,
                            increment = -1, 
                            layers = layers, 
                            shape = Pad.SHAPE_ROUNDRECT, 
                            roundrect_rratio = 0.25, 
                            type = Pad.TYPE_SMT, 
                            size = [pad_x, pad_y], 
                            x_spacing = e,
                            y_spacing = 0)

        kicad_mod.append(pa_left)
        kicad_mod.append(pa_right)
        kicad_mod.append(pa_top)
        kicad_mod.append(pa_bottom)
    
    # Quad row package, pin 1 upper left corner, Zero Orientation Level B
    if (npx and npy and ZERO_ORIENTATION == 'B'):
        center_left = [pin_y_neg / 2, 0]
        center_right = [pin_y_pos / 2, 0]
        center_top = [0, pin_y_neg / 2]
        center_bottom = [0, pin_y_pos / 2]

        pa_left = PadArray(pincount=npx, 
            intial = 1, 
            center = center_left,
            increment = 1, 
            layers = layers, 
            shape = Pad.SHAPE_ROUNDRECT, 
            roundrect_rratio = 0.25, 
            type = Pad.TYPE_SMT, 
            size = [pad_y, pad_x], 
            x_spacing = 0,
            y_spacing = e)

        pa_right = PadArray(pincount = npx, 
            initial = 2 * npx + npy, 
            center = center_right,
            increment = -1, 
            layers = layers, 
            shape = Pad.SHAPE_ROUNDRECT, 
            roundrect_rratio = 0.25, 
            type = Pad.TYPE_SMT, 
            size = [pad_y, pad_x], 
            x_spacing = 0,
            y_spacing = e)

        pa_bottom = PadArray(pincount = npy, 
            initial = npx + 1, 
            center = center_bottom,
            increment = 1, 
            layers = layers, 
            shape = Pad.SHAPE_ROUNDRECT, 
            roundrect_rratio = 0.25, 
            type = Pad.TYPE_SMT, 
            size = [pad_x, pad_y], 
            x_spacing = e,
            y_spacing = 0)

        pa_top = PadArray(pincount = npy, 
            initial = 2 * npx + 2 * npy, 
            center = center_top,
            increment = -1, 
            layers = layers, 
            shape = Pad.SHAPE_ROUNDRECT, 
            roundrect_rratio = 0.25, 
            type = Pad.TYPE_SMT, 
            size = [pad_x, pad_y], 
            x_spacing = e,
            y_spacing = 0)

        kicad_mod.append(pa_left)
        kicad_mod.append(pa_right)
        kicad_mod.append(pa_top)
        kicad_mod.append(pa_bottom)

    if ZERO_ORIENTATION == 'A':
        outline = [
        {'x': -Dnom/2,'y': -E1nom/2},
        {'x': Dnom/2,'y': -E1nom/2},
        {'x': Dnom/2,'y': E1nom/2},
        {'x': -Dnom/2 + 1,'y': E1nom/2},
        {'x': -Dnom/2,'y': -E1nom/2 + 1},
        {'x': -Dnom/2,'y': -E1nom/2},]
        kicad_mod.append(PolygoneLine(polygone=outline, layer='F.Fab', width=0.12))
    
    elif ZERO_ORIENTATION == 'B':
        outline = [
        {'x': -Dnom/2 + 1,'y': -E1nom/2},
        {'x': Dnom/2,'y': -E1nom/2},
        {'x': Dnom/2,'y': E1nom/2},
        {'x': -Dnom/2,'y': E1nom/2},
        {'x': -Dnom/2,'y': -E1nom/2 + 1},
        {'x': -Dnom/2 + 1,'y': -E1nom/2},]
        kicad_mod.append(PolygoneLine(polygone=outline, layer='F.Fab', width=0.12))
    else:
        print "Invalid orientation (must be A or B)"
    # create silkscreen

    # add designator for pin #1

    # draw the courtyard

    # draw fab outlines for pads if selected as option
    # TODO: if DRAW_PAD_FAB:

    # add model
    kicad_mod.append(Model(filename="${{KISYS3DMOD}}/Housings_SSOP/{fp_name}.{model_type}".format(
                           fp_name = fN, 
                           model_type = rules.MODEL_3D_TYPE, 
                           at=[0, 0, 0], 
                           scale=[1, 1, 1], 
                           rotate=[0, 0, 0])))

    print(kicad_mod.getCompleteRenderTree())
    filename = fN + ".kicad_mod"

    # write file
    file_handler = KicadFileHandler(kicad_mod)
    file_handler.writeFile(filename)
    
    