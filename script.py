import json
import time
import os

aircraftsFile = "/run/readsb/aircraft.json"
count = 0

while True:
    try:
        os.system('clear')
        
        if not os.path.exists(aircraftsFile):
            print("Waiting for readsb aircraft data")
            time.sleep(1)
            continue

        with open(aircraftsFile, "r") as file:
            data = json.load(file)
            # print(data['aircraft'])

            # Holds all of the airplane data 
            aircraft_list = data.get(aircraft,[])

            print("Number of aircraft: " + len(aircraft_list))
            print('-' * 40)

            for plane in data['aircraft']:
                # print(plane['flight'] + ' at ' + str(plane["alt_baro"]) + " ft")
                print(f"Aircraft {plane.get('flight')} is at {str(plane.get('alt_baro'))} ft.")

    except FileNotFoundError:
        print("The airplane data file could not be found.")

    except PermissionError:
        print("You do not have permission to read this file.")

    except json.JSONDecodeError:
        pass

    time.sleep(1)
    ## count += 1
