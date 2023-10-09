# TODO:
# The program should read in the shapefile
# The user should be prompted to provide the path to shapefile
# reading the shapefile path would probably be as a string 
# We will probably use the read and write functions 
# Consider reading in the file using GDAL
# Cammel case convention for the class name
# checking geometry intersection ()
# could use fiona, json of shp using fiona, and create geometry using shapely
# Highly recommend fiona

from osgeo import ogr

shapefile = ogr.Open("/path/to/shapefile")
class ShapefileValidator:
    # read the shapefile
    # I think there should be classes that allow me to read in a shapefile
    # I think there should be classes that allow me to write to a shapefile
    