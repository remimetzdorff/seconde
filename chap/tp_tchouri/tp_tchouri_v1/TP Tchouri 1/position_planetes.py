import numpy as np
import matplotlib.pyplot as plt

# Lecture des fichiers de données pour récupérer les positions des planètes
# Terre
data_terre = np.loadtxt("earth.txt", skiprows=8)
x_terre, y_terre = data_terre[:,0], data_terre[:,1]
# Tchouri
data_tchouri = np.loadtxt("tchouri.txt", skiprows=8)
x_tchouri, y_tchouri = data_tchouri[:,0], data_tchouri[:,1]

#######################
# PARAMETRES DE L'ETUDE
#######################
# Pendant combien de jours veut-on représenter la position des planètes ?
nb_jours = 200

# Combien de jours entre deux positions successives ?
delta_jours = 75

###########################
# MISE A JOUR DES POSITIONS
###########################
# Liste des positions de la Terre : X_Terre (abscisses) et Y_Terre (ordonnées)
X_terre = [x_terre[i] for i in range(len(x_terre[:nb_jours])) if i%delta_jours==0]
Y_terre = [y_terre[i] for i in range(len(y_terre[:nb_jours])) if i%delta_jours==0]
# Liste des positions de la Tchouri : X_Tchouri (abscisses) et Y_Tchouri (ordonnées)
X_tchouri = [x_tchouri[i] for i in range(len(x_tchouri[:nb_jours])) if i%delta_jours==0]
Y_tchouri = [y_tchouri[i] for i in range(len(y_tchouri[:nb_jours])) if i%delta_jours==0]

########################################
# REPRESENTATION GRAPHIQUE DES POSITIONS
########################################
fig = plt.figure()

# Le Soleil
plt.plot([0],[0], "*", color="gold", markersize=20, label="Soleil")

# La Terre
plt.plot(X_terre, Y_terre, "o", color="blue", label="Terre")

# Tchouri
# À compléter

# Changement d'échelle pour les axes (limites du graphe)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

# Titre, nom des axes et légende
plt.title("Évolution de la position de quelques objets du système solaire")
plt.xlabel("Abscisse par rapport au soleil\nen unités astronomiques (au)")
plt.ylabel("Ordonnée par rapport au soleil\nen unités astronomiques (au)")
plt.legend(loc = "upper left")
fig.axes[0].set_aspect("equal")
plt.show()