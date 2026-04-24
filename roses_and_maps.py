import pandas as pd
import pygmt


'''
This script reads in a csv of lineations with line bearings between 0-180, and
corner coordinates of a bounding box, and creates a rose diagram using PyGMT.
Coming soon: makes an accompanying map that plots the points of the lineations
in the specified bounding box.

input: 
filepath to csv
bounding box corner coordinates

output:
rose diagram in pdf form

exceptions:
-.csv must have x, y coordinates and line bearing columns labelled as:
x_coord, y_coord, bearing_corrected
-x_coord and y_coord must be in decimal degrees
'''

class RosesAndMaps:
    def __init__(self, csv_path,):
        '''
        initializes the instance by reading in the data and setting up
        a copy for filtering
        '''
        #adjustable attributes
        self.r_max = 250
        self.bin_width = 10
        self.color = "green"

        #create a pandas dataframe of lineations in the csv file
        self.df = pd.read_csv(csv_path)
        #creating a copy of data from which to filter
        self.filtered_df = self.df.copy()

        #debugging check
        print(f"{len(self.df)} lineations in csv_file.")


    def set_bbox(self, x_min, x_max, y_min, y_max):
        '''
        setting up bounding box.
        '''
        self.filtered_df = self.df[
            (self.df["x_coord"] >= x_min) &
            (self.df["x_coord"] <= x_max) &
            (self.df["y_coord"] >= y_min) &
            (self.df["y_coord"] >= y_max) 
            ].copy()

        #debugging check
        print(f"{len(self.filtered_df)} lineations in bounding box.")

    def plot_rose(self):
            '''
            Plotting filtered dataframe as rose diagram.
            '''
            azimuths = self.filtered_df["bearing_corrected"].dropna()
            lengths = [1] * len(azimuths)

            fig = pygmt.Figure()

            fig.rose(
                length = lengths,
                azimuth = azimuths,
                region = [0, self.r_max, 0, 360],
                sector = self.bin_width,
                diameter = "15c",
                fill = self.color,
                pen = "1p,black",
                frame = ["xg20", "yg30"],
            )

            fig.show()

    # coming soon: def plot_map(self):

if __name__ == "__main__":
    csv_path = input("Enter full path to CSV file: ").strip()
    
    my_lineations = RosesAndMaps(csv_path)

    x1 = float(input("Enter x_min: "))
    x2 = float(input("Enter x_max: "))
    y1 = float(input("Enter y_min: "))
    y2 = float(input("Enter y_max: "))
    
    my_lineations.set_bbox(x1, x2, y1, y2)
    my_lineations.plot_rose()