import time
import board
import math
import lcdsample
import adafruit_dht
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

mylcd=lcdsample.lcd()

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/home/pi/Desktop/envmon-hardware/sakey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {'databaseURL': 'https://envmon-12b11-default-rtdb.europe-west1.firebasedatabase.app/'})
 
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
 
while True:
    try:
        # Print the values to the serial port
        mylcd.lcd_clear()
        temp = dhtDevice.temperature
        hum = dhtDevice.humidity
        mylcd.lcd_display_string("Temp: "+str(temp)+" C", 1)
        mylcd.lcd_display_string("Hum: "+str(hum)+"%", 2)
        millisnow=math.trunc(time.time()*1000)
        print(millisnow)
        ref = db.reference('temp/Control Room')
        result = ref.update({str(millisnow):int(temp)})
        ref = db.reference('hum/Control Room')
        result = ref.update({str(millisnow):int(hum)})            
        print("Temp: "+str(temp)+" C, Hum: "+str(hum)+"%")
        
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(60)