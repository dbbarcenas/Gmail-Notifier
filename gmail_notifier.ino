int outPin = 12; // Output connected to digital pin 12
int mail = LOW; // Is there new mail?
int val; // Value read from the serial port

void setup()
{
    pinMode(outPin, OUTPUT); // sets the digital pin as output
    Serial.begin(9600);
    Serial.flush();
}

void loop()
{
    // Read from serial port
    if (Serial.available())
    {
        val = Serial.read();  //sets the serial.read as val
        Serial.println(val);
        if (val == 'M') mail = HIGH; //if "M" and "N" is detected trough the serial port sent   
        else if (val == 'N') mail = LOW;   //by check-gmail.py file, it sets mail to HIGH or LOW.
  }
    // Set the status of the output pin
  digitalWrite(outPin, mail);
  
}
