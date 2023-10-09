# Point and Shapefile validator
This repo contains programs for two spatial data validators, name geometry point validator and shapefile validator. The geometry point validator currently has two versions, described below.

# GeometryPointValidator
This is a simple python function that will validate a point geometry and print if it valid or not

## GeometryPointValidator Version 1:
A Python function that will validate a Point geometry and print whether it is valid and the reason.
The Lat and Lon in float will be taken from user input.
In this implimentation valid points for latitude were between -90 and 90, and for longitude between -180 and 180.

Additional features:
- Show the history of all points entered by the user. It will print the count of Points, followed by each point, valid result, and reason.
- End, to end session
- User can choose which feature to use (Validate Point, Check History, or End)
- If the feature user chooses does not exist, then it will print “Command does not exist”.

## GeometryPointValidator Version 2:
- Combine your functions into a Class named PointValidator
- Add error handling at least on the Lat and Lon input. Think of any error that could be handled.
- Add feature to export current history to a file. Filename must contain current date and time when the file is exported. Example: "point-2023.02.14-00.15.01", the format is "point-{year}.{double digit month}.{double digit date}-{double digit hour}.{double digit minutes}.{double digit seconds}"
- Add feature to read exported file. User must input the filename and/or the full path of the file. The content of the file would be added to the current history. If you used list to store current history, then the file content would be added to that list.

# Shapefile Validator 
- Make a class that operates on a shapefile with these features as options. Each point would be a separate option on the screen.
- Validate each feature, whether they are valid geometry or not.
- Check the intersection among features. This will only be valid if the geometry type is LineString, MultiLineString, Polygon, or MultiPolygon. If the geometry type is not one of them, then show a warning that this feature is not applicable.
- Remove invalid geometry and export to a shapefile. 
- Remove intersecting geometry and export to a shapefile.
- Convert to CSV. This will only be valid if the geometry type is Point. If the shapefile's geometry type is not Point, then show warning that this feature is not applicable.