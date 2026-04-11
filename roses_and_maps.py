import pandas as pd
import numpy as np
import pygmt


'''
This script reads in a csv of lineations with line bearings between 0-180, and
corner coordinates of a bounding box, and creates a rose diagram using PyGMT.
Coming soon: makes an accompanying map that plots the points of the lineations
in the specified bounding box.

input: 
csv filepath
(coming soon) bounding box corner coordinates

output:
rose diagram in pdf form

exceptions:
-.csv must have x, y coordinates and line bearing columns labelled as:
x_coord, y_coord, bearing_corrected
-(coming soon) x_coords and y_coords must be in decimal degrees (not yet done)
'''

print("this is working")


#asking user for file and reading it
csv_file = input("Enter full path to CSV file: ").strip()
df = pd.read_csv(csv_file)

#extracting line bearings into a dataframe
azimuths = df["bearing_corrected"].dropna()
lengths = [1] * len(azimuths) 


#variables to adjust
bin_width = 10
r_max = 250
radial_grid = "xg20"
azimuth_grid = "yg30"
color = "green"


#PYGMT
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
