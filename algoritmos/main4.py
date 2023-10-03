from pydoc import classname
from re import S
from typing import Dict
import cv2
import time
import math
import copy
import json

import pickle

from numpy import append
from numpy import array
import numpy as np


def distancia(obj1, obj2):
    Umx1 = obj1[0]
    Umx2 = obj1[2]
    Umy1 = obj1[1]
    Umy2 = obj1[3]

    Doisx1 = obj2[0]
    Doisx2 = obj2[2]
    Doisy1 = obj2[1]
    Doisy2 = obj2[3]

    CentroLofX = Umx2 - (Umx1/2)
    CentroLofY = Umy2 - (Umy1/2)

    CentroLatuX = Doisx2 - (Doisx1/2)
    CentroLatuY = Doisy2 - (Doisy1/2)

    dist = math.sqrt((CentroLofX - CentroLatuX)**2 +
                     (CentroLofY - CentroLatuY)**2)

    return dist

def distancia2(obj1,obj2):
    Umx1 = obj1[0]
    Umx2 = obj1[2]
    Umy1 = obj1[1]
    Umy2 = obj1[3]

    Doisx1 = obj2[0]
    Doisx2 = obj2[2]
    Doisy1 = obj2[1]
    Doisy2 = obj2[3]

    CentroLofX = Umx2 - (Umx1/2)
    CentroLofY = Umy2 - (Umy1/2)

    CentroLatuX = Doisx2 - (Doisx1/2)
    CentroLatuY = Doisy2 - (Doisy1/2)

    dist = math.sqrt((CentroLofX - CentroLatuX)**2 +
                     (CentroLofY - CentroLatuY)**2)

    return dist



def merge5(DicioClassId, box, frameI, idObj):
    # print("len",len(DicioClassId), idObj)
    if (len(DicioClassId) is None):
        DicioClassId.append({idObj: [{frameI: box}]})
        # print ("adicionando novo")

    menorDist = 600

    for boats in DicioClassId:
        # print("boats" , boats)
        for frameBox in boats.values():
            # print("framebox",frameBox)
            for umavez in frameBox:  # roda apenas uma vez, pq so tem um
                print("box", umavez)
                print("frame corrente", frameI, " box corrente", box)
                for boxFOR in umavez.values():
                    distanciaI = distancia(box, boxFOR)
                    # print("box : ", box , "boxFor: ", boxFOR , "distancia entre" ,distanciaI)
                    if (distanciaI < menorDist):
                        menorDist = distanciaI
                        menorDistObj = box
                        # print(menorDist,menorDistObj)
                        if (menorDist < 10):
                            frameBox.append(
                                {str(frameI)+"da merge": menorDistObj})

                        else:
                            # print("kkdsadj")
                            DicioClassId.append(
                                {"da merge"+str(idObj): [{frameI: box}]})

                    # print(boxFOR)


def merge6(DicioClassId, box, frameI, idObj):
    # print("len",len(DicioClassId), idObj)

    # print ("adicionando novo")

    menorDist = 600

    for boats in DicioClassId:
        for frameBox in boats.values():  # pegar ultimo de boats.values
            print("framebox", frameBox)
            for umavez in frameBox:  # roda apenas uma vez, pq so tem um
                for boxFOR in umavez.items():
                    if (frameI == boxFOR[0]+1):
                        print("frameI", frameI, " keys", boxFOR)
                        distanciaI = distancia(box, boxFOR[1])
                    else:
                        distanciaI = 9000
                    # print("box : ", box , "boxFor: ", boxFOR , "distancia entre" ,distanciaI)
                    if (distanciaI < menorDist):
                        menorDist = distanciaI
                        menorDistObj = box
                        # print(menorDist,menorDistObj)
                        if (menorDist < 10):
                            frameBox.append({frameI: menorDistObj})

                        else:
                            DicioClassId.append({idObj: [{frameI: box}]})


def merge7(DicioClassId, box, frameI, idObj):

    menorDist = 600
    limiar = 20

    for boats in DicioClassId:

        for frameBox in boats.values():  # pegar ultimo de boats.values
            ultimoFrameBox = frameBox[len(frameBox)-1]
            distanciaI = distancia(box, list(ultimoFrameBox.values())[0])
            #print(box, list(ultimoFrameBox.values())[0],distanciaI)

            
            if (distanciaI < menorDist):
                menorDist = distanciaI
                menorDistObj = box

                
    if (menorDist < limiar):
        #print("fazendo append")
        frameBox.append({frameI: menorDistObj})

    else:
        #print("nova entrada")
        DicioClassId.append({idObj: [{frameI: box}]})


# Cores
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# Carrega as classes do coco.names
class_names = []
with open("coco.names.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Carrega o vídeo usando OpenCv
cap = cv2.VideoCapture("videos/vid.mp4")

# Carregando os weights da rede neural
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg.txt")

# Setar parametros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)
var = 1
frameI = 0


ListaDetcAtual = []
DicDetcOfic = {}
DicValor = {}
Dicio = {}
dicFrame = {}
contDetec = 0
dicMerge = []
# Capturando os frames com OpenCv, loop infinito
while True:

    # Captura dos frames
    _, frame = cap.read()

    # Começo da contagem dos segundos(FPS)
    começo = time.time()

    # Detectando com model.detect
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)

    # Fim da contagem
    fim = time.time()

    

    # Laço para percorrer todas as detecções
    for (classid, score, box) in zip(classes, scores, boxes):
        # print(class_names[classid])

        # Gerando uma cor para a classe
        color = COLORS[int(classid) % len(COLORS)]

        # String para mostrar nome da classe e seu score (porcentagem de eficácia da detecção)
        text = f"{class_names[classid]} : {[score]}"

        # Desenhando o retângulo da classe
        cv2.rectangle(frame, box, color, 2)

        # Escreve o nome da classe em cima da box
        cv2.putText(frame, text, (box[0], box[1]-15),
                    cv2.QT_FONT_NORMAL, 0.5, color, 2)
        idObj = class_names[classid] + str(contDetec)  # boat1 boat2

        classidINT = int(classid+1)
        


        if not classid+1 in Dicio:
            Dicio[classid+1] = []
            #print(box)
            Dicio[classid+1].append({idObj: [{frameI: box}]})

        else:
            merge7(Dicio[classid+1], box, frameI, idObj)

        contDetec += 1
        var = var + 1

    # Calculando o FPS
    fps_text = f"FPS: {round((1.5/(fim - começo)),2)}"

    # Colocando FPS na tela
    cv2.putText(frame, fps_text, (0, 25), cv2.QT_FONT_NORMAL, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_text, (0, 25),
                cv2.QT_FONT_NORMAL, 1, (0, 255, 0), 3)

    # Mostrando imagem
    cv2.imshow("teste", frame)

    # Programa finaliza no 'ESC'
    if cv2.waitKey(1) == 27:
       # print(Dicio)
        # print(str(Dicio))
        # data = json.dumps(str(Dicio))
        #print(Dicio[9])
        print(Dicio)
        arr = np.array(Dicio)
        arr_as_list = arr.tolist()
        #print(arr_as_list)
        json = json.dumps(arr_as_list)
        arq = open("outputs/arquivo.json", "w")
        arq.write(json)
        break

    frameI = frameI+1
    if (frameI > 20):

        print("tamanho dic", len(Dicio[9]))
        print(Dicio)
        json = json.dumps(Dicio[9][0])
        arq = open("outputs/arquivo.json", "w")
        
        arq.write(json)
        break

# Destruir todas janelas e fechar programa
cap.release()
cap.destroyAllWindows()
