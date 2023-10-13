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

import fiona
from shapely.geometry import shape, mapping
from shapely.validation import explain_validity
from shapely.ops import unary_union
import csv

class ShapefileProcessor:
    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path

    def validate_geometry(self):
        with fiona.open(self.shapefile_path) as source:
            valid_features = []
            invalid_features = []

            for feature in source:
                geom = shape(feature['geometry'])
                if geom.is_valid:
                    # adding the valid to the list
                    valid_features.append(feature)
                else:
                    invalid_features.append(feature)
                    print(f"Invalid geometry found: {explain_validity(geom)}")
    
        return valid_features, invalid_features
    
    def remove_invalid_geometry_and_export(self, output_shapefile):

        valid_features, invalid_features = self.validate_geometry()

        with fiona.open(output_shapefile, 'w', driver= 'ESRI Shapefile', schema=output_shapefile.schema, crs=output_shapefile.crs) as output:
            for feature in valid_features:
                # but you see here we are just writing the valid features out, but we are not taking of projections
                output.write(feature)

    def check_intersection(self):
        valid_geometry_types = ['LineString', 'MultiLineString', 'Polygon', 'MultiPolygon']
        intersection_features = []

        with fiona.open(self.shapefile_path) as source:
            features = list(source)

        for i, feature in enumerate(features):
            geom = shape(feature['geometry'])
            if geom.geom_type in valid_geometry_types:
                intersect = False
                for j, other_feature in enumerate(features):
                    if i != j:
                        other_geom = shape(other_feature['geometry'])
                        if geom.intersects(other_geom):
                            intersect = True
                            break
                if not intersect:
                    intersection_features.append(feature)

        return intersection_features

    def remove_intersecting_geometry_and_export(self, output_shapefile):
        intersection_features = self.check_intersection()

        with fiona.open(output_shapefile, 'w', driver='ESRI Shapefile', schema=output_shapefile.schema, crs=output_shapefile.crs) as output:
            for feature in intersection_features:
                print("Remember to change this back")
                output.write(feature)
                

    def convert_to_csv(self, output_csv):
        point_features = []

        with fiona.open(self.shapefile_path) as source:
            for feature in source:
                geom = shape(feature['geometry'])
                if geom.geom_type == 'Point':
                    point_features.append(feature)
                else:
                    print("Warning: Some features have geometry types other than Point.")

            with open(output_csv, 'w') as csvfile:
                print(source.schema)
                writer = csv.DictWriter(csvfile, fieldnames=source.schema['properties'].keys())
                writer.writeheader()
                for feature in point_features:
                    writer.writerow(feature['properties'])

# Check the part that gets the features.

# Example usage:
shapefile_path = "/home/charles/Desktop/Kartoza_Project/GeometryPointValidator/GeometryPointValidator_Kartoza/shapefiles/RandomPoints.shp"
output_shapefile = "/home/charles/Desktop/Kartoza_Project/GeometryPointValidator/GeometryPointValidator_Kartoza/shapefiles/Rdm_output.shp"
output_csv = "/home/charles/Desktop/Kartoza_Project/GeometryPointValidator/GeometryPointValidator_Kartoza/shapefiles/Rdm_output.csv"

processor = ShapefileProcessor(shapefile_path)
processor.remove_invalid_geometry_and_export(output_shapefile)
processor.remove_intersecting_geometry_and_export(output_shapefile)
processor.convert_to_csv(output_csv)
