#include <DHT.h>

DHT dht(2, DHT22);

float humidity, temperature;

void setup() 
{

  // Set serial baud rate
  Serial.begin(9600);

  dht.begin();

}

void loop() 
{
  
  //retreive data from sensor, store in variable
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  // output humidity and temperature data
  Serial.println(String(humidity) + "," + String(temperature));
  
  // delay until next reading
  delay(1000);

}


