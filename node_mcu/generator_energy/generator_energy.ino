#define voltage_generator 5
#define equivalent_resistor 12.5

void setup() {
  pinMode(D0,LOW);
  pinMode(D1,LOW);
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {

  //int sensorValue = analogRead(A0)-analogRead(A1);

  
  pinMode(D1,LOW);
  pinMode(D0, HIGH);
  float val1 = analogRead(A0);
  pinMode(D0,LOW);
  pinMode(D1, HIGH);
  float val2 = analogRead(A0);
  float sensorValue = val1-val2;
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  float current = voltage/equivalent_resistor;
  // print out the value you read:
   //Serial.print(current*1000);
   //Serial.println("mA");
  float power = voltage_generator * (current);
  Serial.print(power*1000);
  Serial.println("mW");
  delay(1000);

}
