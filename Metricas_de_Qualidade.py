import numpy as np
import cv2
import scipy
import copy

# Erro quadrático médio
def RMSE(img1, img2):
    array_1 = np.array(img1)
    array_2 = np.array(img2)

    mse = np.mean(np.square(array_1 - array_2))
    rmse = np.sqrt(mse)

    return rmse

# Relação de contraste para ruído
def CNR(img1, img2):
    im1_32F = np.float32(img1) / 255.0
    im1 = cv2.convertScaleAbs(im1_32F)
    x = scipy.ndimage.mean(im1)

    im2_32F = np.float32(img2) / 255.0
    im2 = cv2.convertScaleAbs(im2_32F)
    y = scipy.ndimage.mean(im2)

    C = x-y
    N = 0
    for i in range(len(img1)):
        for j in range(len(img1[0])):
          N += (im1[i][j] - x )**2
        N/=(len(img1)*len(img1[0]))

    return C/np.sqrt(N)

# Erro de brilho médio absoluto
def AMBE(img1, img2):

    im1_32F = np.float32(img1) / 255.0
    im1 = cv2.convertScaleAbs(im1_32F)
    #im1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY) nao é usado pois nao suporta imagens de 64 bits e sim de 32
    meanstat1 = scipy.ndimage.mean(im1)

    im2_32F = np.float32(img2) / 255.0
    im2 = cv2.convertScaleAbs(im2_32F)
    #im2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    meanstat2 = scipy.ndimage.mean(im2)

    return meanstat1 - meanstat2

def metricas(imagens):
    img_ori = imagens[0]
    metricas_rmse = []
    metricas_cnr = []
    metricas_ambe = []
    img_aux = imagens[:]
    img_aux.pop()
    for img in img_aux:
        img_clone1 = copy.copy(img)
        img_clone2 = copy.copy(img)
        metricas_rmse.append(RMSE(img_ori, img))
        metricas_cnr.append(CNR(img_ori, img_clone1))
        metricas_ambe.append(AMBE(img_ori, img_clone2))

    return metricas_rmse, metricas_cnr, metricas_ambe