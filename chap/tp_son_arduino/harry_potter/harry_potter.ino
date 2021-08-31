// tempo du morceau
int tempo = 150;

// fréquence des notes de musique
int la_ref = 880;
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
  tone(13, note, int(duration/1.));
  delay(duration);
}

void pause() {   delay(noire_duration * 2.); }
void silence() { delay(noire_duration); }
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

// Harry Potter
void loop() {
  pause();
  noire(note_si/2.);
  noire_point(note_mi);
  croche(note_sol);
  noire(note_sol_b);
  blanche(note_mi);
  noire(note_si);
  blanche_point(note_la);
  blanche_point(note_sol_b);
  noire_point(note_mi);
  croche(note_sol);
  noire(note_sol_b);
  blanche(note_mi_b);
  noire(note_fa);
  blanche_point(note_si/2.);

  pause();
  noire(note_si/2.);
  noire_point(note_mi);
  croche(note_sol);
  noire(note_sol_b);
  blanche(note_mi);
  noire(note_si);
  blanche(note_re*2.);
  noire(note_re_b*2.);
  blanche(note_do*2.);
  noire(note_la);
  noire_point(note_do*2.);
  croche(note_si);
  noire(note_si_b);
  blanche(note_si_b/2.);
  noire(note_sol);
  blanche_point(note_mi);

  pause();
  noire(note_sol);
  blanche(note_si);
  noire(note_sol);
  blanche(note_si);
  noire(note_sol);
  blanche(note_do*2.);
  noire(note_si);
  blanche(note_si_b);
  noire(note_sol_b);
  noire_point(note_sol);
  croche(note_si);
  noire(note_si_b);
  blanche(note_si_b/2.);
  noire(note_si/2.);
  blanche(note_si);
  silence();

  pause();
  noire(note_sol);
  blanche(note_si);
  noire(note_sol);
  blanche(note_si);
  noire(note_sol);
  blanche(note_re*2.);
  noire(note_re_b*2.);
  blanche(note_do*2.);
  noire(note_la_b);
  noire_point(note_do*2.);
  croche(note_si);
  noire(note_si_b);
  blanche(note_si_b/2.);
  noire(note_sol);
  blanche(note_mi);
  silence();
  pause();
  silence();
}
