# Un programme pour faciliter les calculs

############
# Constantes
############
G      = 6.67e-11 # Constante gravitationnelle en m^3 kg^-1 s^-2
g      = 9.81     # Accélération de pesanteur (Terre) en m s^-2

###########
# Grandeurs
###########
# Masses en kg
m_tintin  = 70
m_asterix = 40
m_obelix  = 150
m_lune    = 7.6e22
m_mars    = 6.39e23
m_terre   = 5.97e24
m_soleil  = 1.99e30
# Distance en m
d_terre_soleil = 149e9
r_lune         = 1.7e6
r_mars         = 3.4e6
r_terre        = 6.37e6

#########################
# Affichage des résultats
#########################

# Force d'interaction gravitationnelle du Soleil sur la Terre
F_soleil_terre = G * m_soleil * m_terre / d_terre_soleil**2
print("La force d'interaction graviationnelle entre la Terre et le Soleil vaut", F_soleil_terre, "N")

# Force d'interaction gravitationnelle de la Terre sur Tintin ?



# Poids de Tintin sur Terre ?



# Poids de Tintin sur la Lune ?



# Accélération de pesanteur sur la Lune : g_lune ?



# Accélération de pesanteur sur Mars : g_mars ?
