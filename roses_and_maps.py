import pandas as pd
import numpy as np
import pygmt


'''
This script reads in a csv of lineations with line bearings between 0-180, and
corner coordinates of a bounding box, and creates a rose diagram using PyGMT.

input: 
csv filepath
bounding box corner coordinates (not yet done)

output:
rose diagram

exceptions:
-csv must have x, y coordinates and line bearing columns labelled as:
x_coord, y_coord, bearing_corrected
-x_coords and y_coords must be in decimal degrees (not yet done)'''

print("is this working")

import pygmt

print("is this working")

azimuths = [90, 90, 75, 60]
lengths = [1] * len(azimuths) 

bin_width = 10
r_max = 15
radial_grid = "xg5"
azimuth_grid = "yg30"
color = "green"

fig = pygmt.Figure()

fig.rose(
    length=lengths,
    azimuth=azimuths,
    region=[0, r_max, 0, 360],
    sector=bin_width,
    diameter="15c",
    fill=color,
    pen="1p,black",
    frame=[radial_grid, azimuth_grid],
)

fig.show()
