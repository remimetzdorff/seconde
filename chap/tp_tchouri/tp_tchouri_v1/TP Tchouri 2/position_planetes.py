import numpy as np
import matplotlib.pyplot as plt

# Lecture des fichiers de données pour récupérer les positions des planètes
# Terre
data_terre = np.loadtxt("earth.txt", skiprows=8)
X_terre, Y_terre = data_terre[:,0], data_terre[:,1]
# Tchouri
data_tchouri = np.loadtxt("tchouri.txt", skiprows=8)
X_tchouri, Y_tchouri = data_tchouri[:,0], data_tchouri[:,1]

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