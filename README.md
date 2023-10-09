# GeometryPointValidator_Kartoza
This is a simple python function that will validate a point geometry and print if it valid or not

The repo contains code for two versions of the geometry point validator. The descriptions and specifications of the two versions can be found below.

## Version 1: Description
A Python function that will validate a Point geometry and print whether it is valid and the reason.
The Lat and Lon in float will be taken from user input.
In this implimentation valid points for latitude were between -90 and 90, and for longitude between -180 and 180.

Additional features:
- Show the history of all points entered by the user. It will print the count of Points, followed by each point, valid result, and reason.
- End, to end session
- User can choose which feature to use (Validate Point, Check History, or End)
- If the feature user chooses does not exist, then it will print “Command does not exist”.

## Version 2: Description
- Combine your functions into a Class named PointValidator
- Add error handling at least on the Lat and Lon input. Think of any error that could be handled.
- Add feature to export current history to a file. Filename must contain current date and time when the file is exported. Example: "point-2023.02.14-00.15.01", the format is "point-{year}.{double digit month}.{double digit date}-{double digit hour}.{double digit minutes}.{double digit seconds}"
- Add feature to read exported file. User must input the filename and/or the full path of the file. The content of the file would be added to the current history. If you used list to store current history, then the file content would be added to that list.
