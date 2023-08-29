'''
Programme transformant une image en matrice de nombres entre 0 et 1
'''

# Importation des bibliothèques
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Liste des images à traiter (dans le dossier data/to_convert)
images_name = os.listdir("data/to_convert")
for img_name in images_name:
    # Importation de l'image
    image = mpimg.imread("data/to_convert/" + img_name)

    # Conversion de l'image en matrice de nombres entre 0 et 1
    image = np.array(image[:, :, 0])
    image = 1 - image
    image = image / np.max(image)

    # Affichage de l'image
    # plt.imshow(image, cmap="gray")
    # plt.show()

    # Exportation de l'image
    np.savetxt("data/done/" + img_name, image)

    print(img_name + " done !")