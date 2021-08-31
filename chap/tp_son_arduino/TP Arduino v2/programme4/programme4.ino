void setup() {
  pinMode(13, OUTPUT); // 13ème broche de la carte en mode sortie  
}

void loop() {
  tone(13, 131, 200);
  delay(400);
  tone(13, 131, 200);
  delay(400);
  tone(13, 131, 200);
  delay(400);
  tone(13, 147, 200);
  delay(400);
  tone(13, 165, 400);
  delay(800);
}
