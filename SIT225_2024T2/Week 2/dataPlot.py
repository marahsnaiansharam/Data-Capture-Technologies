import matplotlib.pyplot as plt
import csv
from datetime import datetime
from mpl_toolkits.axes_grid1 import host_subplot

readingtime = []
temperature = []
humidity = []

csv_file_path = '/Users/iansharam/Documents/Education/Deakin University/2024/Trimester 2/Data Capture/Week - 2/CaptureProject/temperature_data.csv'

with open(csv_file_path, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        readingtime.append(datetime.strptime(row[0], '%Y%m%d%H%M%S'))
        temperature.append(float(row[1]))
        humidity.append(float(row[2]))

host = host_subplot(111)
parasite = host.twinx()

host.set_xlabel("Time")
host.set_ylabel("Temperature")
parasite.set_ylabel("Humidity")

p1 = host.plot(readingtime,temperature,label = "Temperature")
p2 = parasite.plot(readingtime, humidity, label = "Humidity")

host.set_ylim(min(temperature), max(temperature))
parasite.set_ylim(min(humidity), max(humidity))

host.legend(loc='upper left')
parasite.legend(loc='upper right')

plt.title("Ambient Bedroom Temperature and Humidity Overnight")
plt.show()

