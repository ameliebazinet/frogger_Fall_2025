import pygame
from config import CAR_COLORS, CARS_SIZE



# ======================== PARTIE 2.1 ========================
# TODO : 
# 1. Parcourir la liste des couleurs (CAR_COLORS) à l'aide d'une boucle
# 2. Pour chaque couleur :
#    - Chargez l'image vers la droite ("_right") et celle vers la gauche ("_left") à l'aide de pygame.image.load().
#    - Redimensionnez chaque image à CARS_SIZE à l’aide de la fonction pygame.transform.scale().
#    - Ajoutez les images redimensionnées dans la bonne liste ("left" ou "right") du dictionnaire cars_dict.

# Écrire votre code ici : 

# Dictionnaire pour les voitures de différentes couleurs et directions
cars_dict = {
    "left": [],
    "right": []
}
for couleur_right in CAR_COLORS:
    image_right = pygame.image.load(f"images/car_{couleur_right}_right.png")
    #transformation de la taille 
    image_right = pygame.transform.scale(image_right,CARS_SIZE)
    #ajout au dictionnaire 
    cars_dict["right"].append(image_right)

for couleur_left in CAR_COLORS:
    image_left = pygame.image.load(f"images/car_{couleur_left}_left.png")
    #transformation de la taille 
    image_left = pygame.transform.scale(image_left,CARS_SIZE)
    #ajout au dictionnaire 
    cars_dict["left"].append(image_left)







# ===============================================================
