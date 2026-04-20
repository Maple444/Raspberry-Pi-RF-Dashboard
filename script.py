import json
import time
import os

aircraftsFile = "/run/readsb/aircraft.json"
# titleBanner = r"""
#   ______   _______   _______          ______   __                                          ______     __            ________                             __                           
#  /      \ |       \ |       \        /      \ |  \                                        /      \   |  \          |        \                           |  \                          
# |  $$$$$$\| $$$$$$$\| $$$$$$$\      |  $$$$$$\ \$$  ______    _______   ______   ______  |  $$$$$$\ _| $$_          \$$$$$$$$______   ______    _______ | $$   __   ______    ______  
# | $$___\$$| $$  | $$| $$__| $$      | $$__| $$|  \ /      \  /       \ /      \ |      \ | $$_  \$$|   $$ \           | $$  /      \ |      \  /       \| $$  /  \ /      \  /      \ 
#  \$$    \ | $$  | $$| $$    $$      | $$    $$| $$|  $$$$$$\|  $$$$$$$|  $$$$$$\ \$$$$$$\| $$ \     \$$$$$$           | $$ |  $$$$$$\ \$$$$$$\|  $$$$$$$| $$_/  $$|  $$$$$$\|  $$$$$$\
#  _\$$$$$$\| $$  | $$| $$$$$$$\      | $$$$$$$$| $$| $$   \$$| $$      | $$   \$$/      $$| $$$$      | $$ __          | $$ | $$   \$$/      $$| $$      | $$   $$ | $$    $$| $$   \$$
# |  \__| $$| $$__/ $$| $$  | $$      | $$  | $$| $$| $$      | $$_____ | $$     |  $$$$$$$| $$        | $$|  \         | $$ | $$     |  $$$$$$$| $$_____ | $$$$$$\ | $$$$$$$$| $$      
#  \$$    $$| $$    $$| $$  | $$      | $$  | $$| $$| $$       \$$     \| $$      \$$    $$| $$         \$$  $$         | $$ | $$      \$$    $$ \$$     \| $$  \$$\ \$$     \| $$      
#   \$$$$$$  \$$$$$$$  \$$   \$$       \$$   \$$ \$$ \$$        \$$$$$$$ \$$       \$$$$$$$ \$$          \$$$$           \$$  \$$       \$$$$$$$  \$$$$$$$ \$$   \$$  \$$$$$$$ \$$                                                                                                                                                                                     
                                                                                                                                                                                
# """

while True:
    try:
        if not os.path.exists(aircraftsFile):
            print("Waiting for readsb aircraft data")
            time.sleep(1)
            continue

        os.system('clear')

        # print(titleBanner)
        print("SDR Aircraft Tracker\n") ## Temporary title text

        with open(aircraftsFile, "r") as file:
            data = json.load(file)

            # Holds all of the airplane data 
            aircraft_list = data.get("aircraft",[])

            print("Number of aircraft: " + str(len(aircraft_list)))
            print('-' * 40)

            for plane in aircraft_list:
                flight = plane.get("flight", "Unknown")
                alt = plane.get("alt_baro", "N/A")
                print(f"Aircraft {flight} is at {alt} ft.")

            print('')
            print('')
            
            print("Be sure your SDR and its antenna are in an open area with lots of reception!")

    except FileNotFoundError:
        print("The airplane data file could not be found.")

    except PermissionError:
        print("You do not have permission to read this file.")

    except json.JSONDecodeError:
        # readsb may be writing the file while we read it
        pass

    time.sleep(1)
