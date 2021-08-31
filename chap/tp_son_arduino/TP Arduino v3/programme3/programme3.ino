void setup() {
  pinMode(9, OUTPUT); // 13ème broche de la carte en mode sortie  
}

void loop() {
  tone(9, 131, 200);
  delay(400);
  tone(9, 131, 200);
  delay(400);
  tone(9, 131, 200);
  delay(400);
  tone(9, 147, 200);
  delay(400);
  tone(9, 165, 400);
  delay(800);
}
