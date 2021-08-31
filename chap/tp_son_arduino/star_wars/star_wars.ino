// tempo du morceau
int tempo = 100;

// fréquence des notes de musique
int la_ref = 220;
int note_do    = la_ref/(powf(2, 9./12));
int note_re_b  = la_ref/(powf(2, 8./12));
int note_re    = la_ref/(powf(2, 7./12));
int note_mi_b  = la_ref/(powf(2, 6./12));
int note_mi    = la_ref/(powf(2, 5./12));
int note_fa    = la_ref/(powf(2, 4./12));
int note_sol_b = la_ref/(powf(2, 3./12));
int note_sol   = la_ref/(powf(2, 2./12));
int note_la_b  = la_ref/(powf(2, 1./12));
int note_la    = la_ref;
int note_si_b  = la_ref*(powf(2, 1./12));
int note_si    = la_ref*(powf(2, 2./12));

int noire_duration = 1000.*60/tempo;

void make_note(int note, int duration) {
  tone(13, note, int(duration/1.5));
  delay(duration);
}

void blanche_point(int note) {  make_note(note, noire_duration * 3.); }
void blanche(int note) {        make_note(note, noire_duration * 2.); }
void noire_point(int note) {    make_note(note, noire_duration * 3./2.); }
void noire(int note) {          make_note(note, noire_duration * 1.); }
void croche_point(int note) {   make_note(note, noire_duration * 3./4.); }
void croche(int note) {         make_note(note, noire_duration * 1./2.); }
void double_croche(int note) {  make_note(note, noire_duration * 1./4); }

void setup() {
  pinMode(13, OUTPUT);
}

// Star Wars
void loop() {
  noire(note_sol);
  noire(note_sol);
  noire(note_sol);
  croche_point(note_mi_b);
  double_croche(note_si_b);
  noire(note_sol);
  croche_point(note_mi_b);
  double_croche(note_si_b);
  blanche(note_sol);
  
  noire(2*note_re);
  noire(2*note_re);
  noire(2*note_re);
  croche_point(2*note_mi_b);
  double_croche(note_si_b);
  noire(note_sol_b);
  croche_point(note_mi_b);
  double_croche(note_si_b);
  blanche(note_sol);
  delay(1000);
}
