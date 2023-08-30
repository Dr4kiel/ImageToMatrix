'''
Programme transformant une image en matrice de nombres entre 0 et 1
'''

# Importation des bibliothèques
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


def main(argc, argv):
    # Liste des images à traiter (dans le dossier data/to_convert)
    images_name = os.listdir("data/to_convert")
    for img_name in images_name:
        # Importation de l'image
        image = mpimg.imread("data/to_convert/" + img_name)

        # Conversion de l'image en matrice de nombres entre 0 et 1
        image = np.array(image[:, :, 0])
        image = 1 - image
        image = image / np.max(image)

        if argc > 1 and argv[1] == "-v":
            # Affichage de l'image
            plt.imshow(image, cmap="gray")
            plt.show()

        # Exportation de l'image
        np.savetxt("data/done/" + img_name, image)

        print(img_name + " done !")

    # si on lance le programme avec l'option -dataset, on sauvegarde les images dans un fichier dataset
    if argc > 1 and argv[1] == "-d":
        # Copie des matrices dans un fichier input_data.txt où chaque ligne correspond à une image
        input_data = open("data/input_data.txt", "w")
        for img_name in images_name:
            image = np.loadtxt("data/done/" + img_name)
            for line in image:
                for number in line:
                    input_data.write(str(number) + " ")
            input_data.write("\n")
        input_data.close()

        print("Dataset done !")


main(len(os.sys.argv), os.sys.argv)
