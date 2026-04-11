import json
import time

aircraftsFile = "aircraft_example_file.json"
count = 0

while True:
    try:
        with open(aircraftsFile, "r") as file:
            data = json.load(file)
            # print(data['aircraft'])

            print("Number of aircraft: " + str(len(data['aircraft'])))

            for plane in data['aircraft']:
                print(plane['flight'] + ' at ' + str(plane["alt_baro"]) + " ft")

    except FileNotFoundError:
        print("The airplane data file could not be found.")

    except PermissionError:
        print("You do not have permission to read this file.")

    time.sleep(1)
    ## count += 1


# CODE FOR THE JSON PARSING AND DATA COLLECTION
