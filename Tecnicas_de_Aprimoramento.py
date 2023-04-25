import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model


#bilateral
def filtro_bilateral(imagem):
    # Aplicando filtro bilateral
    imagem_filtrada = cv2.bilateralFilter(imagem, 9, 75, 75)

    return imagem_filtrada

#Equalização do histograma:
def equalizacao_do_histograma(img):

    # Convertendo a imagem para YUV
    img_to_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    # Aplicando equalização do histograma
    img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
    # Convertendo para escala BGR
    equalizado = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
    return equalizado

#Correção de gama
def correcao_de_gama(img):
    img = img/255.0
    img1 = cv2.pow(img,1.5)
    img2 = cv2.pow(img,0.6)
    return img1, img2

def correcao_de_gama_especial(img):
    img = img/255.0
    img1 = cv2.pow(img,3.5)
    return img1

def aprimoramento_de_imgs(img):
    imgs = []
    # Imagem original
    imgs.append(img)
    # Bilateral
    imgs.append(filtro_bilateral(img))
    # Equalização do histograma
    imgs.append(equalizacao_do_histograma(img))
    img_EH = equalizacao_do_histograma(img)
    # Correção de gama
    gama15, gama06 = correcao_de_gama(img)
    imgs.append(gama15)
    imgs.append(gama06)
    # Caso especial (EH para correção de gama = 3,5)
    imgs.append(correcao_de_gama_especial(img_EH))
    #print(imgs)
    return imgs