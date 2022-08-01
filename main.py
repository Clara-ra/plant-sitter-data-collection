import sys
import time
import dialog
import client
import data_collection


    
if __name__ == "__main__":
    plants_list = client.get_plants_list()
    res = input(dialog.quantify_plant_list(plants_list)).lower()
    print(res)
    if (res == "x"):
        sys.exit("exiting program.")
    elif (res == "0"):
        plant_id, plant_name = dialog.add_a_plant()
        print(plant_id)
        print(plant_name)
    else:
        plant_id, plant_name = dialog.get_plant_id(int(res), plants_list)
        print(plant_id)
        print(plant_name)
    res = input("{0} selected! Press Enter to begin data collection.".format(plant_name))
    if (res == ""):
        while True:
            datapoint = data_collection.collect()
            print("data point generated. sending data...")
            response = client.add_plant_data(plant_id, datapoint)
            print("data successfully sent! database entry:")
            print(response)
            print("sleeping for an hour till next read.")
            time.sleep(3600)

        
        