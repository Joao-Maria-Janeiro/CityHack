#include <math.h>

int pinOut = 10;
int pinIn = 9;
static bool circuit_on = false;

void circuit_on_off() {
  
  if(circuit_on){
    digitalWrite(pinOut, LOW);
    circuit_on = false;
  }else{
    digitalWrite(pinOut, HIGH);
    circuit_on = true;
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(pinOut, OUTPUT);
  pinMode(pinIn, INPUT);
  
  
}

void loop() {                   
    if(digitalRead(pinIn))  circuit_on_off();
    Serial.println(digitalRead(pinIn));

    
}


