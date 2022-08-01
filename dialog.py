import client

def quantify_plant_list(plants):
    dialog = "Select an option from below: \n"
    dialog = dialog + "x - Exit program \n"
    dialog = dialog + "0 - Add New Plant \n"
    counter = 0
    for plant in plants:
        counter +=1
        dialog = f'{dialog}{counter} - {plant["plantName"]} \n'
    return dialog

def get_user_input(option):
    confirmation = "x"
    
    while (confirmation == "x"):
        user_input = input("Enter {0}:".format(option))
        confirmation = input("Is {0} correct? \nPress Enter to confirm, or x to try again.".format(user_input)).lower()
    return user_input
    
    
def add_a_plant():
    print("New plant option selected!")
    plant_name = get_user_input("plant name")
    location = get_user_input("location")
    plant_object = client.format_new_plant(plant_name, location)
    response = client.add_plant(plant_object)
    return [response["_id"], plant_name]
    
def get_plant_id(plant_num, plants_list):
    plant_id = plants_list[plant_num-1]["_id"]
    plant_name = plants_list[plant_num-1]["plantName"]
    return [plant_id, plant_name]