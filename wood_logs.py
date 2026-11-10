import pygame
from config import LOG_SIZES

# ======================== PARTIE 3.1 ===========================
# 
# TODO : Définir un dictionnaire pour les bûches en bois avec trois tailles différentes : petite, moyenne et longue
# 
# Étapes à suivre : 
# - Créer un dictionnaire nommé `logs_dict` avec les trois clés suivantes : 
#      - short
#      - medium
#      - long 
#
# - Utilisez "pygame.image.load()" pour charger l'image "log.png" (à partir du dossier "images/")
#   trois fois, c'est-à-dire une fois pour chaque taille.
# - Redimensionnez (avec "pygame.transform.scale") chaque image en utilisant les clés du dictionnaire LOG_SIZES. 
image_log = pygame.image.load("images/log.png")

vraie_short = pygame.transform.scale (image_log,LOG_SIZES["short"])
vraie_med = pygame.transform.scale (image_log,LOG_SIZES["medium"])
vraie_long = vraie_short = pygame.transform.scale (image_log,LOG_SIZES["long"])

logs_dict = {"short" : vraie_short, "medium" : vraie_med,"long": vraie_long}

# ===============================================================