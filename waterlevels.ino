// the setup routine runs once when you press reset:
int X;
int Y;
float TIME = 0;
float FREQUENCY = 0;
float WATER = 0;
float TOTAL = 0;
float LS = 0;
const int input = A0;
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  unsigned long currentMillis = millis();
  X = pulseIn(input, HIGH);
  Y = pulseIn(input, LOW);
  
  // the time is one pulse period
  TIME = X + Y;

  // frequency is 1/ time(sec) but time is ms
  FREQUENCY = 1000000 / TIME;
  // outputs 7.5 liters every 
  WATER = FREQUENCY / 7.5;
  //liters per second
  LS = WATER / 60;
  
  if (FREQUENCY >= 0) {
    //Serial.println(FREQUENCY);
    if(!isinf(FREQUENCY)){
      //Serial.print("Time: ");
      Serial.println(currentMillis);
      TOTAL = TOTAL + LS;
      //Serial.print("FLOW RATE: ");
      Serial.println(WATER);
      //Serial.println(" Liters per Minute");
      //Serial.print("TOTAL VOLUME: ");
      Serial.println(TOTAL);
      //Serial.println(" Liters");
    }
  } 

  delay(1000);
}
