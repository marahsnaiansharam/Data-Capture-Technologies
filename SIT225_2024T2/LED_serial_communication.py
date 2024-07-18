""" Communicates with Arduino across serial input to blink the built-in LED
    receives a return value to trigger a waiting period to allow time to process the LED blink before repeating"
"""

import serial
import random
import time

"set serial transfer rate"
baud_rate = 9600 



"assign serial port Arduino is connected to, timeout set to 20 to allow time for arduino to execute LED flashes"
arduino = serial.Serial('/dev/cu.usbmodem1101', baud_rate, timeout=20)
print("\n---------------")
while True:
    led_blink_number = random.randint(1,10)
    print("Value sent to Arduino")

    data_size = arduino.write(bytes(str(led_blink_number), 'utf-8'))
    print(f"Send >>> {led_blink_number} ({data_size} bytes)")

    wait_time = arduino.readline().decode("utf-8")
    
    
    print(f"Wait duration: {wait_time}")
    try:
        wait_time = int(wait_time)
        time.sleep(wait_time)
        print("Sleep Complete")
        print("---------------")
    except ValueError:
        print(f"Invalid wait time received from Arduino: {wait_time}")    


