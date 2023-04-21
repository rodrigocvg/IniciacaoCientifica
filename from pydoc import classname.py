from pydoc import classname
from re import S
from typing import Dict
import cv2
import time
import math
import copy
import json

from numpy import append
from numpy import array
import numpy as np


def distancia(obj1,obj2):
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


    dist = math.sqrt((CentroLofX - CentroLatuX)**2 + (CentroLofY - CentroLatuY)**2)

    return dist 
     
def merge5(DicioClassId,box,frameI,classnames):
     #print("len",len(DicioClassId), classnames)
     if(len(DicioClassId) is None):
        DicioClassId.append({classnames:[{frameI:box}]})
        #print ("adicionando novo")
     
     menorDist = 600
     for boats in DicioClassId:
                #print("boats" , boats)
                for frameBox in boats.values():
                    #print("framebox",frameBox)
                    for umavez in frameBox: #roda apenas uma vez, pq so tem um
                        #print("box",umavez)
                        for boxFOR in umavez.values():
                            distanciaI = distancia(box,boxFOR)
                            #print("box : ", box , "boxFor: ", boxFOR , "distancia entre" ,distanciaI)
                            if(distanciaI<menorDist):
                                 menorDist = distanciaI
                                 menorDistObj = box
                                 #print(menorDist,menorDistObj)
                                 if(menorDist<5):
                                    frameBox.append({frameI:menorDistObj})
                                 else:
                                    DicioClassId.append({classnames:[{frameI:box}]})

                            #print(boxFOR)


#Cores
COLORS = [(0,255,255), (255,255,0), (0,255,0), (255,0,0)]

#Carrega as classes do coco.names
class_names = []
with open("coco.names.txt","r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

#Carrega o vídeo usando OpenCv
cap = cv2.VideoCapture("vid.mp4")

#Carregando os weights da rede neural 
net = cv2.dnn.readNet("yolov4-tiny.weights","yolov4-tiny.cfg.txt")

#Setar parametros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416),scale=1/255)
var = 1
frameI = 0


ListaDetcAtual = []
DicDetcOfic = {}
DicValor = {}
Dicio = {}
dicFrame = {}
contDetec = 0
dicMerge = []
#Capturando os frames com OpenCv, loop infinito
while True:

    # Captura dos frames
    _, frame = cap.read()

    #Começo da contagem dos segundos(FPS)
    começo = time.time()

    #Detectando com model.detect
    classes,scores,boxes = model.detect(frame, 0.1, 0.2)

    #Fim da contagem 
    fim = time.time()
    
    # Laço para percorrer todas as detecções
    for(classid,score,box) in zip(classes,scores,boxes):
        #print(class_names[classid])

        #Gerando uma cor para a classe
        color = COLORS[int(classid) % len(COLORS)]
        
        #String para mostrar nome da classe e seu score (porcentagem de eficácia da detecção)
        text = f"{class_names[classid]} : {[score]}"
        
        #Desenhando o retângulo da classe
        cv2.rectangle(frame,box,color,2)

        #Escreve o nome da classe em cima da box
        cv2.putText(frame,text,(box[0], box[1]-15), cv2.QT_FONT_NORMAL,0.5,color,2)
        idObj = class_names[classid] + str(contDetec) #boat1 boat2
        
        if (frameI == 0):

            

            if not class_names[classid] in DicValor:
                        DicValor[class_names[classid]] = []
             
            DicValor[class_names[classid]].append({frameI:box})

            if not classid+1 in Dicio:
                        Dicio[classid+1] = []


            Dicio[classid+1].append({class_names[classid]:DicValor[class_names[classid]]})
        
        else:
                
                if not class_names[classid] in DicValor:
                        DicValor[class_names[classid]] = []
                if not classid+1 in Dicio:
                        Dicio[classid+1] = []
                #try:
                # print(classid)
                # print("class_names[classid]",class_names[classid])
                # print("Dicio[classid+1]",Dicio[classid+1])
                # print("box",box)
                # print("frameI",frameI)
                
                
                merge5(Dicio[classid+1],box,frameI,class_names[classid]) #ta puxando idObj errado
                #except:
                     #pass
        contDetec+= 1
        #print(contDetec,"contDETEC")
        var = var + 1
    

    #Calculando o FPS
    fps_text = f"FPS: {round((1.5/(fim - começo)),2)}"

    #Colocando FPS na tela
    cv2.putText(frame,fps_text, (0,25), cv2.QT_FONT_NORMAL, 1,(0,0,0), 5)
    cv2.putText(frame,fps_text, (0,25), cv2.QT_FONT_NORMAL, 1,(0,255,0), 3)

    #Mostrando imagem
    cv2.imshow("teste", frame)

    #Programa finaliza no 'ESC'
    if cv2.waitKey(1) == 27:
        print(Dicio)
        break
    
    frameI = frameI+1
    if (frameI > 20000):
      
        print(Dicio)
        break

#Destruir todas janelas e fechar programa
cap.release()
cap.destroyAllWindows()
