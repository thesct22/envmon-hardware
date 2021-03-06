import board
import busio
import time
import math
import lcdsample
import digitalio
import adafruit_max31865
import adafruit_dht


spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.

sensor = adafruit_max31865.MAX31865(spi, cs)

mylcd=lcdsample.lcd()

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D6, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        
        temp = sensor.temperature
        hum = dhtDevice.humidity
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Temp: "+"{:.2f}".format(temp)+" C", 1)
        mylcd.lcd_display_string("Hum: "+str(hum)+"%", 2)    
        print("Temp: "+str(temp)+" C, Hum: "+str(hum)+"%")
        
        
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(1.0)
