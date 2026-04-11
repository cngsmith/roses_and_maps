import pandas as pd
import numpy as np
import pygmt

pygmt.show_versions()
print("is this working")





#install packages


#m








# ##PAG CODE


# ##reading my attribute .csv as a dataframe
# df = pd.read_csv("indiv_orientations_msgl.csv")

# ##defining columns
# az_col = "azimuth_corrected"
# ice_col = "ice_flow_provenance"
# ref_col = "smith_reference" 
# cruise_col = "smith_cruise"

# ##filtering csv
# # filtering by content, comment row out if you don't want to filter by it, or make a list for multiple
# selected_ice = ["Chukchi Shelf"]
# #selected_ref = ["Smith"]
# #selected_cruise = ["Sikuliaq_2021"]

# #creating a filtered dataframe by creating a boolean series according to my chosen filter, comment out line you don't need
# df_filtered = df.copy()

# df_filtered = df_filtered[df_filtered[ice_col].isin(selected_ice)]
# #df_filtered = df_filtered[df_filtered[ref_col].isin(selected_ref)]
# #df_filtered = df_filtered[df_filtered[cruise_col].isin(selected_cruise)]

# msgl = df_filtered[az_col]

# #----------------------------------

# ##Pygmt

# #variables to change 
# bin_width = 10
# r_max = 15
# radial_grid = "xg5"
# azimuth_grid = "yg30"
# color = "green"

# #begin plotting

# fig = pygmt.Figure()
# fig.rose(
#     data=msgl,   
#     incols=[0],
#     region=[0, r_max, 0, 360],
#     sector=bin_width,
#     diameter="15c",
#     fill= color,
#     pen="1p,black",
#     frame=[radial_grid, azimuth_grid],
# )

# fig.show()