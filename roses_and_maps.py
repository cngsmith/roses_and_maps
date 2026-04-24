import pandas as pd
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


class RosesAndMaps:
    def __init__(self, csv_path,):
        '''
        initializes the instance by reading in the data and setting up
        a copy for filtering
        '''
        #create a pandas dataframe of lineations in the csv file
        self.df = pd.read_csv(csv_path)
        #creating a copy of data from which to filter
        self.filtered_df = self.df.copy()

        #debugging check
        print(f"Successfully loaded {len(self.df)} lineations.")


    # def set_bbox(self, x1, x2, y1, y2):
    # def plot_rose(self, output_filename):
    # def plot_map(self, output_filename):


if __name__ == "__main__":
    csv_path = input("Enter full path to CSV file: ").strip()
    
    # Initialize the instance
    my_lineations = RosesAndMaps(csv_path)
 

# ##asking for user input: data file path and map bounding box
# csv_file = input("Enter full path to CSV file: ").strip()
# df = pd.read_csv(csv_file)

# x_min = input("Enter the x_coordinate for the top left corner of the map: ").strip()
# y_max = input("Enter the y_coordinate for the top left corner of the map: ").strip()
# x_max = input("Enter the x_coordinate for the bottom right corner of the map: ").strip()
# y_min = input("Enter the y_coordinate for the bottom right corner of the map: ").strip()





# #asking user for file and reading it
# csv_file = input("Enter full path to CSV file: ").strip()
# df = pd.read_csv(csv_file)

# #extracting line bearings into a dataframe
# azimuths = df["bearing_corrected"].dropna()
# lengths = [1] * len(azimuths) 


# #variables to adjust
# bin_width = 10
# r_max = 250
# radial_grid = "xg20"
# azimuth_grid = "yg30"
# color = "green"


# #PYGMT
# fig = pygmt.Figure()

# fig.rose(
#     length=lengths,
#     azimuth=azimuths,
#     region=[0, r_max, 0, 360],
#     sector=bin_width,
#     diameter="15c",
#     fill=color,
#     pen="1p,black",
#     frame=[radial_grid, azimuth_grid],
# )

# fig.show()