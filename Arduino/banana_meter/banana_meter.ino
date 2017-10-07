int analogPin = A0;

void setup() {
  Serial.begin(9600);             //see Tools > Serial Monitor for output
  pinMode(analogPin, INPUT);
}

void loop() {
  Serial.println(analogRead(analogPin));
}
