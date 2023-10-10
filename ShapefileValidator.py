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
# /home/charles/Desktop/Kartoza_Project/GeometryPointValidator/GeometryPointValidator_Kartoza/shapefiles/za_boundaries.shp

from osgeo import ogr
# the user is supposed to request for the path
# we are supposed to read the path to the shapefile and open it.
shapefile = ogr.Open("/path/to/shapefile")
class ShapefileValidator:
    # read the shapefile
    # I think there should be classes that allow me to read in a shapefile
    # I think there should be classes that al/home/charles/Desktop/Kartoza_Project/GeometryPointValidator/GeometryPointValidator_Kartoza/shapefiles/za_boundaries.shp me to write to a shapefile
    def __init__(self, path):
        self.path = path

    def readPathToFile():
        # request the user to enter the path to the shapefile
        # read the path to the shapefile
        # return the path to the shapefile
        print("================ShapeFileValidator=======================================")
        print("Please enter the path to the shapefile")
        path = input("Enter path:")
        file = ogr.Open(path)
        shape = file.GetLayer(0)
        #first feature of the shapefile
        feature = shape.GetFeature(0)
        first = feature.ExportToJson()
        print(first) # (GeoJSON format)
        {"geometry": {"type": "LineString", "coordinates": [[0.0, 0.0], [25.0, 10.0], [50.0, 50.0]]}, "type": "Feature", "properties": {"FID": 0.0}, "id": 0}

ShapefileValidator.readPathToFile()
