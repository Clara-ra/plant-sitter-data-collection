import time
import board
import adafruit_bh1750
from adafruit_htu21d import HTU21D
import adafruit_pcf8591.pcf8591 as PCF
from adafruit_pcf8591.analog_in import AnalogIn

from datetime import datetime



#board setup
i2c = board.I2C()
adc = PCF.PCF8591(i2c)
light_sensor = adafruit_bh1750.BH1750(i2c)
t_and_h_sensor = HTU21D(i2c)
moisture_sensor = AnalogIn(adc, PCF.A0)

wet = 595 #This was the highest value seen after calibration
dry = 223 #This was the lowest value seen after calibration

def translate_to_percent(value):
    original_range = wet - dry
    #convert the value into a percent of the original range
    valuePercent = float(value - dry)/ float(original_range)
    #Return percentage as whole number, not decimal
    return valuePercent * 100

def get_light():
    return light_sensor.lux

def get_temp():
    return t_and_h_sensor.temperature

def get_humidity():
    return t_and_h_sensor.relative_humidity

def get_moisture():
    raw_value = moisture_sensor.value
    moisture_percent = translate_to_percent(raw_value)
    return moisture_percent

def get_time():
    raw_timestamp = datetime.now()
    formatted_time = raw_timestamp.strftime("%d-%m-%Y, %H:%M")
    return formatted_time

def format_data(time, temp, humidity, light, moisture):
    return {"timestamp": time, "temperature": temp, "humidity": humidity, "light": light, "moisture": moisture}

def collect():
    timstamp = get_time()
    light = get_light()
    temp = get_temp()
    humidity = get_humidity()
    moisture = get_moisture()
    return format_data(timestamp, temp, humidity, light, moisture)

if __name__ == "__main__":
    while True:
        print("begin sensor reading.")
        print(collect())
        sleep(5)

    
