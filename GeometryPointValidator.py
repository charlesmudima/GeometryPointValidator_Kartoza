points_history = []
def main_menu():
    print("The modes of this application include:")
    print("1. Check history of previous points")
    print("2. Validate a geometry point")
    print("3. Exit")
    mode = int(input("Enter mode:"))
    if mode == 1:
        print("History of previous points")
        print("====================================================================")
        print(points_history)
        main_menu()

    if mode == 2:
        print("Please enter your geometery point in the following format: x,y")
        point = input("Enter point:")
        latitude = float(point.split(",")[0])
        longitude = float(point.split(",")[1])
        validator(latitude, longitude)
    if mode == 3:
        print("Exit")
        exit()

def validator(latitude, longitude):     
    if latitude > 90 or latitude < -90:
        print("Latitude is out of range")
    elif longitude > 180 or longitude < -180:
        print("Longitude is out of range")
    else:
        print("Latitude and Longitude are valid")
        points_history.append(str(latitude) + "," + str(longitude))
        print("====================================================================")
        main_menu()

    
print("Welcome to the Geometry Point Validator!")
username = input("Enter username:")
print("====================================================================")
print("Hello: " + username)

main_menu()


