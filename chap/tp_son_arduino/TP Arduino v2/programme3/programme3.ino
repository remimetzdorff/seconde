// fonction d'initialisation de la carte
void setup() {
  pinMode(13, OUTPUT); // 13ème broche de la carte en mode sortie  
}

// fonction principale
void loop() {
  digitalWrite(13, HIGH); // place la broche 13 dans l'état haut
  delay(1000);
  digitalWrite(13, LOW);  // place la broche 13 dans l'état bas
  delay(1000);
}
