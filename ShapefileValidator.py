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
from osgeo import gdal
from osgeo import osr # dealing with projections and spatial reference
from shapely.geometry import shape
shapefile_path = "/home/charles/Desktop/Kartoza_Project/GeometryPointValidator/GeometryPointValidator_Kartoza/shapefiles/RandomPoints.shp"
class ShapefileValidator:
    def __init__(self, path):
        self.path = path

    def menu():
        print("================ShapeFileValidator=======================================")
        print("1. Submit path to shapefile")
        print("2. Exit")
        mode = int(input("Enter mode:"))

        if mode == 1:
            print("=============================READING-IN SHAPEFILE=======================================")
            ShapefileValidator.readPathToFile()
        elif mode == 2:
            print("Exit")
            exit()

    def readPathToFile():
        print("Please enter the path to the shapefile")
        # path = input("Enter path:") Temporarily removed this line
        # ogr.Open(path, 0) # 0 means read-only. 1 means writeable. 
        file = ogr.Open(shapefile_path)
        shape = file.GetLayer(0)
        #first feature of the shapefile
        feature = shape.GetFeature(0)
        layerDefinition = shape.GetLayerDefn()
        for i in range(layerDefinition.GetFieldCount()):
            print(layerDefinition.GetFieldDefn(i).GetName())
        # print(layerDefinition)
        first = feature.ExportToJson()
        print(first) # (GeoJSON format)
        {"geometry": {"type": "LineString", "coordinates": [[0.0, 0.0], [25.0, 10.0], [50.0, 50.0]]}, "type": "Feature", "properties": {"FID": 0.0}, "id": 0}
        # ShapefileValidator.ConvertToShape(first)
    
    
    def ConvertToShape(firstly):
        print("###hey###")
        shp_geom = shape(firstly['geometry']) # or shp_geom = shape(first) with PyShp
        print(shp_geom)
        # LINESTRING [(0 0, 25 10, 50 50)]
        # print type(shp_geom)
        # <class 'shapely.geometry.linestring.LineString'>
ShapefileValidator.readPathToFile()
