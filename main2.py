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

def merge(obj1,DictionaryFinal,classId,contDetec,idObj):
    dictionaryClassId = DictionaryFinal[classId] #passar esse
    if (dictionaryClassId is None):
       #cria nova entrada no DictionaryFinal e coloca obj1
       DictionaryFinal.append(obj1)
       print(1)
    else:        
      distanciaI = distancia(obj1,dictionaryClassId[contDetec-1][idObj][0][0])
      menorDistObj = dictionaryClassId[contDetec-1][idObj][0][0]
    
                 
    #   for i in dictionaryClassId:
    #     for j in i.values():
    #       for f in j:
    #           for bx in f.values():
    #             di = distancia(obj1,bx)
    #             print("difora",di)
    #             if (di > distanciaI):
    #                     print("di",di)
    #                     distanciaI = di
    #                     menorDistObj = bx 
    print("Menor distancia = ", distanciaI)
    limiar = 20

    if (distanciaI <= limiar):
                    #unir obj com o menorDistObj;
                    #guardar a box e add no boat de menordist #adicionar mais um J do for
                    print('menordis < limiar')
    else:
                    #cria uma nova entrada com o obj no dictionaryClassId
                    DictionaryFinal[classId].append(obj1) 
                    print('nova entradaw')

    
def merge2(obj,DicioClassId,contDetec,classname,frameI):
    print(contDetec,frameI)
    try:
        box = obj[contDetec][classname][0].get(frameI) # descomentar
        print(box)
    except:
          pass
    #print(box)
    #print("PRIMEIRA POSICAO",DicioClassId[contDetec][idObj][0][0])
    if(DicioClassId is None):
        DicioClassId.append(obj)
    else:
        #retornar novo Dicio
        distanciaI = 0
        # distanciaI = distancia(box,DicioClassId[contDetec][class_names[classid]][0].get(frameI))
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
                  #print(bx, box)
                #   distanciaI = distancia(box,bx) descomentar
                #   if(distanciaI>300):
                #         j.append(f)
                #   print(distanciaI)
                 
                  #print("bx",bx) 
            #print(DicioClassId)


         # for i in DicioClassId:
        #     for j in i.values():
        #         for f in j:
        #             for bx in f.values():
        #                 #di = distancia(box,bx)
        #                 di=0
        #                 #print("difora",di)
        #                 if (di > distanciaI):
        #                     #print("di",di)
        #                     distanciaI = di
        #                     #menorDistObj = bx 
     

def merge3(dicMerge,DicioClassId,frameI,contDetec,classnames):
    #print(contDetec,frameI)
   
    #print(box)
    #print("PRIMEIRA POSICAO",DicioClassId[contDetec][idObj][0][0]
        #rornar novo Dicio
        menorDistanciaI = -1
        menorDistObj = {}
        #print(dicMerge)
        
        #print(distancia(dicMerge[frameI],DicioClassId[0]['boat'][0]))
        # distanciaI = distancia(box,DicioClassId[contDetec][class_names[classid]][0].get(frameI))
        #print("Merge: ",DicioClassId[contDetec][class_names[classid]][0].get(frameI))
        for i in DicioClassId:
            #print("i",i)
            
            for j in i.values():
                t=2
                #print("j",j)
                for f in j:
                    t=2# cada elemento da lista ####nao vai existir mais (PEGAR SÓ A ULTIMA POSICAO J(ÚLTIMO FRAMESS))
                print("f",f) # f é um dic
                #print("j2",j)
                #("teste",j)
                #print(f.values())
                for bx in j:
                    t=2
                    #print(bx)
                    #print("bx, box", bx, box)
                    #print("dicMerge", dicMerge.get(frameI))
                    
                    #distanciaI = distancia(box,bx) #descomentar
                    #print(distanciaI,menorDistanciaI)
                    #menorDistanciaI = distancia(box,DicioClassId[0][class_names[classid]][0].get(0))
                        #print(dicMerge.get(frameI),bx)
                    #print(distanciaI < menorDistanciaI)
                    if(distanciaI < menorDistanciaI):
                          print(1)
                          menorDistanciaI = distanciaI
                          menorDistObj = i
                          #print(menorDistObj)
                          
                          #print(bx , " = ", box , "distancia entre :", distanciaI)
                    if(menorDistanciaI<10):
                        #print(menorDistObj)
                        a=2
                        
                        #j.append(menorDistObj)
                
                #print("menorDist Obj", menorDistObj)
                    else:
                        DicioClassId.append({"oi":"oi"})
                    
                        #print(bx , " = ", box , "distancia entre :", distanciaI)
                        #print("removido: " ,obj.pop())

def merge4(DicioClassId,box,frameI):
        
        menorDistanciaI = -1
        menorDistObj = {}
        #print(box,frameI)
        for i in DicioClassId:
            for j in i.values():
                for f in j:
                    for bx in j[len(j)-1].values():
                        #print(dicMerge)
                        #distanciaI = distancia(dicMerge[frameI],bx) #descomentar
                        distanciaI = distancia(box,bx)
                        print(bx , " = ", box , "distancia entre :", distanciaI)
                            #print(dicMerge.get(frameI),bx)
                        if(distanciaI < menorDistanciaI):
                            menorDistanciaI = distanciaI
                            menorDistObj = i
                            #print(menorDistObj)
                            
                            print(bx , " = ", box , "distancia entre :", distanciaI)
                        if(menorDistanciaI<10):
                            print(menorDistObj)
                            
                            j.append(menorDistObj)
                    
                    #print("menorDist Obj", menorDistObj)
                        else:
                            DicioClassId.append({"oi":"oi"})
                        
                            #print(bx , " = ", box , "distancia entre :", distanciaI)
                            #print("removido: " ,obj.pop())
     
def merge5(DicioClassId,box,frameI,classnames):
     print("len",len(DicioClassId), classnames)
     if(len(DicioClassId) is None):
        DicioClassId.append({classnames:[{frameI:box}]})
        print ("adicionando novo")
     
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
        print(class_names[classid])

        #Gerando uma cor para a classe
        color = COLORS[int(classid) % len(COLORS)]
        
        #String para mostrar nome da classe e seu score (porcentagem de eficácia da detecção)
        text = f"{class_names[classid]} : {[score]}"
        
        #Desenhando o retângulo da classe
        cv2.rectangle(frame,box,color,2)

        #Escreve o nome da classe em cima da box
        cv2.putText(frame,text,(box[0], box[1]-15), cv2.QT_FONT_NORMAL,0.5,color,2)
        
        if (frameI == 0):
            

            
            idObj = class_names[classid] + str(contDetec) #boat1 boat2 

            if not class_names[classid] in DicValor:
                        DicValor[class_names[classid]] = []
             
            DicValor[class_names[classid]].append({frameI:box})

            if not classid+1 in Dicio:
                        Dicio[classid+1] = []


            Dicio[classid+1].append({class_names[classid]:DicValor[class_names[classid]]})
                    #classid+1 = chave, contDetec = detec , idObj = 'boat1', [0] = primeira posicao, [0], acessa as box
                    #print("BOXES: ",Dicio[classid+1][contDetec]) # acessa as boxes
                    #print("distancia ", distancia(Dicio[classid+1][contDetec][idObj][0][0],Dicio[classid+1][contDetec-1][idObj][0][0]))
                    #print(Dicio.items())
            # try:
            #     print(Dicio.get(classid+1)[2]," ", contDetec)
            # except:
            #      pass
        
        else:
            
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
                

                #try:
                merge5(Dicio[classid+1],box,frameI,class_names[classid]) #ta puxando idObj errado
                #except:
                     #ass
                #print(box)
                # dicMerge = {frameI: box}
                #print("Dic Merge = ", dicMerge)
            
                #merge2(dicMerge,Dicio[classid+1],contDetec,class_names[classid],frameI) #Dicio.get(classid+1) nao existe ainda
                #merge3(dicMerge,Dicio[classid+1],frameI,contDetec,class_names[classid])
                #merge4(Dicio[classid+1],box,frameI)
                a = 0
            #print("")


        contDetec+= 1
        print(contDetec,"contDETEC")
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
        # for i in Dicio[classid+1]:
        #     print("Dic Inteiro: ", i)
        #     for obj in i:
        #         print("frame: box",i.get(obj))
        #         for x in i.get(obj):
        #             print(x[0])
                
                
        # for boats in Dicio[classid+1]:
        #     print("boats" , boats)
        #     for frameBox in boats.values():
        #          print("framebox",frameBox)
        #          for umavez in frameBox: #roda apenas uma vez, pq so tem um
        #             print("box",umavez)
        #             for box in umavez.values():
        #
        #           print(box)
        print(Dicio)
        #print(dicMerge)
        
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
