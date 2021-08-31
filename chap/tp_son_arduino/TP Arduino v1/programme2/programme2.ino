// fonction d'initialisation de la carte
void setup() {
  pinMode(9, OUTPUT); // 9ème broche de la carte en mode sortie
}

// fonction principale
void loop() {
  tone(9, 440, 1000); // fonction générant un signal périodique
}
