import os
import requests
from dotenv import load_dotenv

load_dotenv() # this is where the url for the server is stored.
URL = os.environ.get("SERVER_URL")

def get_plants_list(): #GET request 
    response = requests.get(url)
    data = response.json()
    return data

def add_plant(plant): #POST request
    response = requests.post(url+"addPlant", json=plant)
    data = response.json()
    return data

def add_plant_data(plant_id, plant_data): #POST request to :id
    plant_url = url + "plant/addData/" + plant_id #concat id to the string
    response = requests.post(plant_url, json=plant_data)
    data = response.json()
    return data
 
def format_plant_data(time, temp, humidity, light, moisture):
    return {"timestamp": time, "temperature": temp, "humidity": humidity, "light": light, "moisture": moisture}

def format_new_plant(plant_name, location):
    return {"plantName": plant_name, "location": location}


if __name__ == "__main__":
    list = get_plants_list()

