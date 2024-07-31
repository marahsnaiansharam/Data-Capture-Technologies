
import serial
from datetime import datetime
import csv
import time

"set serial transfer rate"
baud_rate = 9600 

"assign serial port Arduino is connected to"
arduino = serial.Serial('/dev/cu.usbmodem1101', baud_rate, timeout=15)

csv_file_path = '/Users/iansharam/Documents/Education/Deakin University/2024/Trimester 2/Data Capture/Week - 2/CaptureProject/temperature_data.csv'

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)

    while True: 
        data = arduino.readline().decode("utf-8")
        print(data)
        if data:
            try:
                humidity, temp = data.split(',')
                readingtime = datetime.now().strftime('%Y%m%d%H%M%S')
                if len(temp) > 1 and len (humidity) > 1:
                    writer.writerow([readingtime,temp,humidity])
                    print(temp,humidity,readingtime)
                time.sleep(5)
            except ValueError:
                print(f"Invalid data received from Arduino: {data}")
    

