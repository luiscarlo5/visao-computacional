import cv2
import numpy as np
import Tecnicas_de_Aprimoramento as ta
import Metricas_de_Qualidade as mq
import mostrar_metricas as mm
from PIL import Image

def mostrar_imagens(imagens):
    cv2.imshow("(a) Imagem Original", imagens[0])
    cv2.imshow("(d) Equalizacao do Histograma", imagens[2])
    cv2.imshow("(b) Filtro Bilateral", imagens[1])
    cv2.imshow("(c) Correcao de gama = 1.5", imagens[3])
    cv2.imshow("(c) Correcao de gama = 0.6", imagens[4])
    cv2.imshow("(x) EH para correcao de gama = 3.5 ", imagens[5])
    cv2.waitKey(0)

while True:
    entrada = int(input("TESTE DE APRIMORAMENTO DE IMAGENS\n0 - para sair;\n1 - raio-x do pé;\n2 - raio-x da mão;\n3 - raio-x do joelho;\n4 - raio-x do tórax;\nDigite o numero conforme a imagem médica a ser utilizada: "))
    if entrada == 1:
        img = cv2.imread('images/053.jpg')
    elif entrada == 2:
        img = cv2.imread('images/020.jpg')
    elif entrada == 3:
        img = cv2.imread('images/016.jpg')
    elif entrada == 4:
        img = cv2.imread('images/012.jpg')
    elif entrada == 0:
        break

    img = cv2.resize(img, (550, 620))
    imgs = ta.aprimoramento_de_imgs(img)
    rmse, cnr, ambe = mq.metricas(imgs)
    while True:
        exibir  = int(input("Digite 1 para exibir as imagens, 2 para exibir as métricas de aprimoramento ou 0 para recomeçar: "))
        if exibir == 1:
            print("\nAgora veja as imagens e depois clique em ESC para recomeçar!!\n")
            mostrar_imagens(imgs)
        elif exibir == 2:
            mm.mostrar_metricas(rmse, cnr, ambe)
        elif exibir == 0:
            cv2.destroyAllWindows()
            break

print("\nFim de programa!!\n")

