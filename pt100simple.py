import board
import busio
import time
import digitalio
import adafruit_max31865
import adafruit_dht

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.

sensor = adafruit_max31865.MAX31865(spi, cs)
dhtDevice = adafruit_dht.DHT22(board.D6, use_pulseio=False)

while 1:
    #print(sensor.temperature)
    #print('Resistance: {0:0.3f} Ohms'.format(sensor.resistance))
    #time.sleep (3.0)
    
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(sensor.temperature)
        print('Resistance: {0:0.3f} Ohms'.format(sensor.resistance))
        print(temperature)
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(3.0)