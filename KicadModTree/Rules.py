'''
kicad-footprint-generator is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

kicad-footprint-generator is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with kicad-footprint-generator. If not, see < http://www.gnu.org/licenses/ >.

(C) 2016 by Thomas Pointhuber, <thomas.pointhuber@gmx.at>
'''

### All units are in millimeters

DEFAULT_LAYER_WIDTH = {'F.SilkS': 0.15,
                       'B.SilkS': 0.15,
                       'F.CrtYd': 0.05,
                       'B.CrtYd': 0.05,
                       'F.Fab': 0.10,
                       'B.Fab': 0.10,
                       'F.Margin': 0.15,
                       'B.Margin': 0.15}

DEFAULT_WIDTH = 0.15

# Affects component orientation; see IPC-7351B/C
ZERO_ORIENTATION = ['LevelA', 'LevelB']

# Contour courtyard type introduced with IPC-7351C
COURTYARD_TYPE = ['Rectangle', 'Contour']

POLARITY_MARKER = ['Circle',
                   'Dot',
                   'Square',
                   'FilledSquare,'
                   'Rectangle',
                   'Triangle',
                   'Dash',
                   'Arc',
                   'Diode']

ASSY_OUTLINE_POLARITY_NOTCH = 1.00

ORIGIN_PLACEMENT = ['Centroid', 'Pin_1']

# Placed on Courtyard layer(s); 0.05 width
ORIGIN_CROSSHAIR = {'CircleDiameter': 0.50,
                   'CrosshairLengths': 0.70}

# Round pad placements to nearest 0.01mm
PAD_PLACEMENT_ROUNDING = 0.01

# Round pad sizes to nearest 0.01mm
PAD_SIZE_ROUNDING = 0.01

# Component placement tolerance
PLACEMENT_TOL = 0.025

# Pad size tolerancing
FABRICATION_TOL = 0.05

# Component density levels; affects pads, courtyard
DENSITY_LEVEL = ['Least', 'Nominal', 'Most']

SILK_CLEARANCE = 0.15

SILK_OUTLINES = ['MAX', 'NOM', 'MIN']

SILK_OUTLINE_ROUNDING = 0.01
SILK_OUTLINE_DEFAULT = SILK_OUTLINES['MAX']