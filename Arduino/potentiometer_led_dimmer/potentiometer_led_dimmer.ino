int analogPin = A0;
int ledPin = 3;

//Can be used with a Photo Resistor, Force sensitive resistor, and anything that has resistance to be measured
void setup() {
  Serial.begin(9600);             //see Tools > Serial Monitor for output
  pinMode(analogPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int analogVal = analogRead(analogPin);
  Serial.println(analogVal);
  analogWrite(ledPin, analogVal/4);         //analogRead values [0,1024], analogWrite values [0,255]
}
