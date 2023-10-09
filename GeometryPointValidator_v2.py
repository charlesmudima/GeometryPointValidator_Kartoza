# TODO:
#  1) Need to create a class for the functions done
#  2) Need to take care of error handling i.e if the user enters a string as a coordinate
#  3) Store the valid points in a nested array or a list of lists
#  4) Need to take care of error handling. When the point is invalid we need to go back to the main menu
#  5) Need to save the points to a file (Add another mode that will save to file)
#  6) Need to read the point from a file

points_history = []

class point_validator:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def main_menu():
        print("The modes of this application include:")
        print("1. Check history of previous points")
        print("2. Validate a geometry point")
        print("3. Write to file")
        print("4. Exit")
        mode = int(input("Enter mode:"))
        if mode == 1:
            print("History of previous points")
            print("====================================================================")
            print(points_history)
            print("====================================================================")
            point_validator.main_menu()
        elif mode == 2:
            print("====================================================================")
            print("Please enter your geometery point in the following format: x,y")
            point = input("Enter point:")
            try:
                latitude = float(point.split(",")[0])
            except ValueError:
                print("====================================================================")
                print("Invalid latitude value")
                print("====================================================================")
                point_validator.main_menu()
            try:
                longitude = float(point.split(",")[1])
            except ValueError:
                print("====================================================================")
                print("Invalid longitude value")
                print("====================================================================")
                point_validator.main_menu()
            point = point_validator(latitude, longitude)
            print(point.latitude)
            print(point.longitude)
            point_validator.validator(point)
        elif mode == 3:
            # TODO: # Still to implement this here
            print("====================================================================")
            print("Writing to file")
            print("====================================================================")
            point_validator.write_to_file(points_history)
        elif mode == 4:
            print("Exit")
            exit()
        else:
            print("====================================================================")
            print("Invalid mode:")
            print("Please enter a valid input")
            print("====================================================================")
            point_validator.main_menu()
    
    def write_to_file(list_of_points):
        print("We are suppose to write to a file here")
        if len(list_of_points):
            print(list)
            with open(r'/home/charles/Desktop/Kartoza_Project/Points.txt', 'w') as fp:
                for item in list:
                    fp.write("%s" %item)
            print("====================================================================")
            point_validator.main_menu()
        else:
            print("The list has something, so we can write the content to a file")

    def re_enter_point():
        point = input("Enter point:")
        try: 
            latitude = float(point.split(",")[0])
        except ValueError:
            print("====================================================================")
            print("Invalid latitude")
            print("====================================================================")
            point_validator.re_enter_point()        
        try: 
            longitude = float(point.split(",")[1])
        except ValueError:
            print("====================================================================")
            print("Invalid longitude")
            print("====================================================================")
            point_validator.re_enter_point()        
        point = point_validator(latitude, longitude)
        point_validator.validator(point)

    def validator(self):
        if self.latitude > 90 or self.latitude < -90:
            print("====================================================================")
            print("Latitude is out of range: correct range is -90 to 90")
            print("Please re-enter the point in the correct range in the following format: x,y")
            point_validator.re_enter_point()
        elif self.longitude > 180 or self.longitude < -180:
            print("====================================================================")
            print("Longitude is out of range: correct range is -180 to 180")
            print("Please re-enter the point in the correct range in the following format: x,y")
            print("====================================================================")
            point_validator.re_enter_point()

        else:
            print("Latitude and Longitude are valid")
            points_history.append(self.latitude )
            points_history.append(self.longitude)
            print("====================================================================")
            point_validator.main_menu()
    
    def validate_input(self):
        try:
            self.latitude = float(self.latitude)
            self.longitude = float(self.longitude)
            point_validator.validator(self)
        except ValueError:
            print("Invalid input")
            print("====================================================================")
            point_validator.main_menu()
    
print("Welcome to the Geometry Point Validator!")
username = input("Enter username:")
print("====================================================================")
print("Hello: " + username)

point_validator.main_menu()


