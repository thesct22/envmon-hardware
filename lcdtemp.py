import time
import board
import math
import lcdsample
import adafruit_dht

mylcd=lcdsample.lcd()
 
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
 
while True:
    try:
        # Print the values to the serial port
        
        temp = dhtDevice.temperature
        hum = dhtDevice.humidity
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Temp: "+str(temp)+" C", 1)
        mylcd.lcd_display_string("Hum: "+str(hum)+"%", 2)            
        #print("Temp: "+str(temp)+" C, Hum: "+str(hum)+"%")
        
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(2)
