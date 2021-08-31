masse_nucleon = 1.67e-27    # masse d'un nucléon en kg
masse_electron = 9.1e-31    # masse d'un électron en kg

#Z = 6                       # nombre de protons ou numéro atomique
#A = 14                      # nombre de nucléons ou nombre de masse

# Valeurs de Z et A pour le fer
Z = 26
A = 56

masse = A * masse_nucleon
print("La masse de l'atome est ", masse, " kg")

masse_nuage_electronique = Z * masse_electron
print("La masse du nuage electronique est ", masse_nuage_electronique, " kg")

comparaison = masse/masse_nuage_electronique
print("L'atome est ", comparaison, " fois plus lourds que son nuage électronique")