#https://pt.linkedin.com/pulse/remo%C3%A7%C3%A3o-de-ru%C3%ADdos-uma-imagem-utilizando-opencv-python-martins#:~:text=A%20suaviza%C3%A7%C3%A3o%20de%20imagens%20no,remo%C3%A7%C3%A3o%20de%20ru%C3%ADdos%20nela%20presentes.

import cv2
from matplotlib import pyplot as plt

# Lendo a imagem que esta presente no mesmo diretorio
# do arquivo mediana.py
img = cv2.imread('einsteinRuido.png')

# Aplicando o filtro de mediana da biblioteca OpenCV
# que é importada como cv2 e atribuindo a variavel median
# utilizando uma mascara 5x5﻿
median = cv2.medianBlur(img, 5)

# Codigo reponsavel por plotar a imagem original e 
# o resultado lado a lado a nivel de comparacao
# mais informacoes sobre: https://matplotlib.org/index.html 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Mediana')
plt.xticks([]), plt.yticks([])
plt.show()