// set data type for variables
int incoming;
int outgoing;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // sets pin to built in LED in output mode
  digitalWrite(LED_BUILTIN, LOW); // turns off LED prior to loop

  Serial.begin(9600);  // set baud rate
}


void loop() {
  while (!Serial.available()) {} // wait for data to arrive

  incoming = Serial.readString().toInt(); // reads data from serial

  // iterate through loop of turning LED on, waiting one second and turning LED off again
  // repeats loop as many times as specified by input from Python script.
  for (int i = 0; i< incoming; ++i){
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(100); //very short delay to ensure the LED turning off is visible to the observer
  }

  outgoing = random(1,10); // sets value for python to delay
  Serial.println(outgoing); // returns value to serial channel
}
