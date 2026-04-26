# roses_and_maps

## version 1.5.3

A program to create rose diagrams and maps using PyGMT, for mega-scale glacial lineation interpretation.

The script is able to read in bearing and coordinate data from a .csv and produce a rose diagram as a .pdf given bounding box coordinates. It also produces an associated map showing the position of the lineation data.

Toy data is provided for testing.

![example rose diagram](example_rosediagrams.png)

Task 1:

The script is organized with one class called RosesAndMaps. One function reads in the data from the .csv file, another filters it by a bounding box, another plots a rose diagram, and one will eventually plot the associated map. I might also add a few other functions such as one that gives me the mean orientation of my filtered dataset.

Task 2:

I use input() as a parameter input system. I will also plan to add tests, like assert statements, within my code.

## installation instructions:

install PyGMT and it's associated dependencies to your conda/mamba environment.
    for example:
    
    micromamba activate GEOS694
    micromamba install PyGMT

download coords_lineations_toydata.csv locally. Provide the filepath when prompted.
