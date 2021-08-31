import numpy as npimport matplotlib.pyplot as plt########## DONNÉES#########t  = np.array([0.00,  0.45,  0.90,  1.35,  1.80,  2.25,  2.70])y1 = np.array([0.00, 10.69, 19.44, 26.25, 31.11, 34.03, 35.00])y2 = np.array([0.00,  0.97,  3.89,  8.75, 15.56, 24.31, 35.00])y3 = np.array([0.00,  5.83, 11.67, 17.50, 23.33, 29.17, 35.00])x1 = np.array([0.00,  0.00,  0.00,  0.00,  0.00,  0.00,  0.00])##################################################### REPRÉSENTATION GRAPHIQUE DES POSITIONS SUCCESSIVES####################################################fig = plt.figure(figsize=(8,6))# Le solplt.plot([-1,1], [35, 35], 'k')plt.fill_between([-1,1], [35, 35], [40, 40], facecolor='k', alpha=0.25)# Les positions successivesc = plt.plot(x1, y2, "o")################### VECTEURS VITESSE################### Point d'originex = 0y = y2[5]# Vitesseu = 0 # Vitesse horizontalev = (y2[6]-y2[5]) / 0.45 # Vitesse verticaleplt.quiver(x, y, u, v, color="red", angles='xy',scale=1.5, scale_units='xy')# Titre, nom des axes et légendeplt.title("Chute libre d'une plume dans le vide")plt.xlabel("Position (m)")plt.ylabel("Distance depuis le point du laché (m)")# Mise en forme du graphiqueticks = c[0].get_data()[1]ax = fig.axes[0]ax.set_xticks([0])ax.set_yticks(ticks)ax.invert_yaxis()for i, tick in enumerate(ticks):    ax.annotate(r"$M_{%i}$"%(i), (0, tick), textcoords="offset points", xytext=(10,0))plt.show()