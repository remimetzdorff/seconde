# le programme demande l'année de naissance de l'utilisateur
annee_Naissance = float(input("En quelle année es-tu né(e) ? "))

# le programme demande l'année en cours
annee_Actuelle = float(input("En quelle année sommes-nous ?1 "))

# on calcule l'âge de l'utilisateur
age = annee_Actuelle - annee_Naissance

# on affiche la réponse
print("Tu as actuellement ", age, " ans")