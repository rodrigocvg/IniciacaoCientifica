from pydoc import classname
from re import S
from typing import Dict
import cv2
import time
import math
import copy

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

def merge(obj1,DictionaryFinal,classId,contDetec,idObj):
    dictionaryClassId = DictionaryFinal[classId] #passar esse
    if (dictionaryClassId is None):
       #cria nova entrada no DictionaryFinal e coloca obj1
       DictionaryFinal.append(obj1)
       print(1)
    else:        
      menorDistancia = distancia(obj1,dictionaryClassId[contDetec-1][idObj][0][0])
      menorDistObj = dictionaryClassId[contDetec-1][idObj][0][0]
    
                 
    #   for i in dictionaryClassId:
    #     for j in i.values():
    #       for f in j:
    #           for bx in f.values():
    #             di = distancia(obj1,bx)
    #             print("difora",di)
    #             if (di > menorDistancia):
    #                     print("di",di)
    #                     menorDistancia = di
    #                     menorDistObj = bx 
    print("Menor distancia = ", menorDistancia)
    limiar = 20

    if (menorDistancia <= limiar):
                    #unir obj com o menorDistObj;
                    #guardar a box e add no boat de menordist #adicionar mais um J do for
                    print('menordis < limiar')
    else:
                    #cria uma nova entrada com o obj no dictionaryClassId
                    DictionaryFinal[classId].append(obj1) 
                    print('nova entradaw')

    
def merge2(obj,DicioClassId,contDetec,classname,frameI):
    #print(contDetec,frameI)
    try:
        box = obj[contDetec][classname][0].get(frameI)
        #print(obj[contDetec][classname][0])  # descomentar
        #print(box)
    except:
          pass
    #print(box)
    #print("PRIMEIRA POSICAO",DicioClassId[contDetec][idObj][0][0])
    if(DicioClassId is None):
        DicioClassId.append(obj) 
    else:
        #retornar novo Dicio
        menorDistancia = 0
        # menorDistancia = distancia(box,DicioClassId[contDetec][class_names[classid]][0].get(frameI))
        #print("Merge: ",DicioClassId[contDetec][class_names[classid]][0].get(frameI))
        for i in DicioClassId:
            t =2 #elementos tipo
            #print("i",i)
            for j in i.values():
                t=2
                #print("j",j)
                for f in j:
                    t=2# cada elemento da lista ####nao vai existir mais (PEGAR SÓ A ULTIMA POSICAO J(ÚLTIMO FRAMESS))
                    #print("f",f) # f é um dic
                #print("j2",j)
                for bx in j[len(j)-1].values():
                    t=2
                    #print("bx, box", bx, box)
                    menorDistancia = distancia(box,bx) #descomentar
                    if(menorDistancia<10):
                        j.append(obj[contDetec][classname][0])
                        print(bx , " = ", box , "distancia entre :", menorDistancia)
                        #print("removido: " ,obj.pop())
                        
                 
                  #print("bx",bx) 
            #print(DicioClassId)


         # for i in DicioClassId:
        #     for j in i.values():
        #         for f in j:
        #             for bx in f.values():
        #                 #di = distancia(box,bx)
        #                 di=0
        #                 #print("difora",di)
        #                 if (di > menorDistancia):
        #                     #print("di",di)
        #                     menorDistancia = di
        #                     #menorDistObj = bx 
     





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
#Capturando os frames com OpenCv, loop infinito
while True:

    # Captura dos frames
    _, frame = cap.read()
    #print(i)
    
    #dicFrame[frameI] = []
    
    #Começo da contagem dos segundos(FPS)
    começo = time.time()

    #Detectando com model.detect
    classes,scores,boxes = model.detect(frame, 0.1, 0.2)

    #Fim da contagem 
    fim = time.time()
    
    # Laço para percorrer todas as detecções
    for(classid,score,box) in zip(classes,scores,boxes):

        #Gerando uma cor para a classe
        color = COLORS[int(classid) % len(COLORS)]
        
        #String para mostrar nome da classe e seu score (porcentagem de eficácia da detecção)
        text = f"{class_names[classid]} : {[score]}"
        
        #Desenhando o retângulo da classe
        cv2.rectangle(frame,box,color,2)

        #Escreve o nome da classe em cima da box
        cv2.putText(frame,text,(box[0], box[1]-15), cv2.QT_FONT_NORMAL,0.5,color,2)

        idObj = class_names[classid] + str(contDetec)

        if not idObj in DicValor:
                        DicValor[idObj] = []
                

                    
                    
        DicValor[idObj].append({frameI:box})

        if not classid+1 in Dicio:
                        Dicio[classid+1] = []


        Dicio[classid+1].append({idObj:DicValor[idObj]})
        
        if (frameI == 0):
              print("primeiro frame")

        else:
            #print(" fdsfsd ", Dicio.get(classid+1)[contDetec])
            merge2(Dicio.get(classid+1),Dicio[classid+1],contDetec,idObj,frameI)
                
                #Dicio2 = copy.deepcopy(Dicio)
                #Dicio2[classid+1].append({class_names[classid]:DicValor[class_names[classid]]})
                #Dicio2[classid+1].append({class_names[classid]:DicValor[class_names[classid]]})
            #print("BOXESELSE: ",Dicio[classid+1][contDetec-1][idObj][0][0])
            #merge(Dicio[classid+1][contDetec-1][idObj][0][0],Dicio,classid+1,contDetec,idObj)
        #print("Frame: ", frameI, " ",  Dicio[classid+1][0][class_names[classid]][0][0])
            # print("Frame: ", frameI, " ",  Dicio[classid+1][contDetec][class_names[classid]][0].get(frameI))
        # for i in Dicio[classid+1]:
        #     #print(i)
        #     for obj in i:
        #           print(i.get(obj))
            #for i in Dicio[classid+1]:
            #merge2(i,Dicio[classid+1],contDetec,idObj,frameI)
            #merge2(Dicio[classid+1][contDetec][class_names[classid]],Dicio[classid+1],contDetec,idObj,frameI)
            
                #merge2(Dicio.get(classid+1),Dicio[classid+1],contDetec,class_names[classid],frameI) #Dicio.get(classid+1) nao existe ainda
            a = 0
            #print("")


        contDetec+= 1
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
        
        break
    
    frameI = frameI+1
    if (frameI > 6):
        # for i in Dicio[classid+1]:
        #     print("Dic Inteiro: ", i)
        #     for obj in i:
        #         print("frame: box",i.get(obj))
        #         for x in i.get(obj):
        #             print(x[0])
                
                
                
        print(Dicio)
        #print(Dicio2) #Dicionário inteiro {classid: lista com ...}
        #print(Dicio.get(classid+1)[2]) #Lista com objetos da respectiva classid #print(Dicio[classid+1]) msm coisa  
        #print(Dicio.get(classid+1)[0]) #primeiro boat (primeira posicao da lista acima)
        #print(Dicio.get(classid+1)[0]['boat']) #Lista com os dicionários {frame: box}
        #print(Dicio.get(classid+1)[0]['boat'][0]) #Primeira posição lista com dicionários, vai ter mais só depois do merge AQUI SERÁ FEITO O APPEND
        #print(Dicio.get(classid+1)[0]['boat'][0].get(0)) #Acesso às boxes 
        
        break
    
# fazer esse for dentro da merge
    # for i in Dicio[classid+1]: #elementos tipo
    #  #print("i",i)
    #  for j in i.values():
    #       #dar o append nesse J
         
    #      #print("j",j)
    #      #j.append({3:array([1,2,3,4])}) será feito assim
    #      #print(len(j))  #outro dic
    #      for f in j: # cada elemento da lista ####nao vai existir mais (PEGAR SÓ A ULTIMA POSICAO J(ÚLTIMO FRAMESS))
    #         print("f",f) # f é um dic
             
    #          #print("j2",j)
    #      for bx in j[len(j)-1].values():
    #              #print("Distancia", distancia(bx,Dicio[9][0]['boat1'][0][0],))
    #              print("bx",bx) 

#Destruir todas janelas e fechar programa
cap.release()
cap.destroyAllWindows()
