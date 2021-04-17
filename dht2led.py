import time
import board
import adafruit_dht
 
dhtDevice = adafruit_dht.DHT22(board.D4)
 
while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(2.0)

