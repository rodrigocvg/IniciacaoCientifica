from pydoc import classname
from re import S
from typing import Dict
import cv2
import time
import math

from numpy import append
from numpy import array
import numpy as np



# DETECÇÃO = LISTA[0][0] = X1 / LISTA[0][1] = Y1 / LISTA[0][2] = x2 / LISTA[0][3] = Y2 //// 
def merge(Dic):
    novoD = {} #criar novo dicionario?
    limiar = 20
    for obj in Dic:
        print(obj)
        for x in range(0,len(Dic[obj])):
        #for x in Dic[obj]:
            print(Dic[obj][x])
            #print(x["box"]["box"])
            print(Dic[obj][x]["box"]["frame"])
            print(Dic[obj][x+1]["box"]["frame"]+1)
            #if Dic[obj][x]["box"]["frame"] == Dic[obj][x+1]["box"]["frame"]+1:

                

            #dist = menorDistancia4(Dic[obj][x],Dic[obj][x+1])
            #print(dist)
            #print (j["box"]["box"])
            #if dist <= limiar:
            #    novoD[obj].append(Dic[x])

    return novoD


#print(Dicio[9][0]['boat1'][0][0]) #acessa as boxes
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


def merge(obj1,DictionaryFinal,classId,cont,idObj):
    dictionaryClassId = DictionaryFinal[classId] #passar esse
    if (dictionaryClassId is None):
       #cria nova entrada no DictionaryFinal e coloca obj1
       DictionaryFinal.append(obj1)
       print(1)
    else:        
      menorDistancia = distancia(obj1,dictionaryClassId[cont-1][idObj][0][0])
      menorDistObj = dictionaryClassId[cont-1][idObj][0][0]
    
                 
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
cont = 0
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
        
        if (frameI == 0):
            

            
            idObj = class_names[classid] + str(cont)

            if not idObj in DicValor:
                DicValor[idObj] = []
        

            
            
            DicValor[idObj].append({frameI:box})

            if not classid+1 in Dicio:
                Dicio[classid+1] = []


            Dicio[classid+1].append({idObj:DicValor[idObj]})
            #classid+1 = chave, cont = detec , idObj = 'boat1', [0] = primeira posicao, [0], acessa as box
            #print("BOXES: ",Dicio[classid+1][cont]) # acessa as boxes
            #print("distancia ", distancia(Dicio[classid+1][cont][idObj][0][0],Dicio[classid+1][cont-1][idObj][0][0]))
            #print(Dicio.items())
            

        else:
            #print("BOXESELSE: ",Dicio[classid+1][cont-1][idObj][0][0])
            #merge(Dicio[classid+1][cont-1][idObj][0][0],Dicio,classid+1,cont,idObj)
            print(22)

        

        
        #print(Dicio[9][0]['boat1'][0][0]) #acessa as boxes
       
        #for chave in Dicio.keys(): #percorrendo Dicionário
            #print(chave) #9
            #merge(Dicio[9][0]['boat1'][0][0],Dicio,9)
       
       # merge(Dicio[9][0]['boat1'][0][0],Dicio,9)

        #print(Dicio[classid+1][cont])
        #print(Dicio[classid+1])
        
        
        
        cont+= 1
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
        
        #print(Dicio)
        
        


        #for j in range(len(ListaDetcAtual)):
            #print("Distancia entre os objetos", 0, "(",ListaDetcAtual[j][1],") e", j+1, "(",ListaDetcAtual[j+1][1],")" )
            #print(menorDistancia(ListaDetcAtual[0],ListaDetcAtual[j+1]))
            


        #print(menorDistancia(ListaDetcAtual[0],ListaDetcAtual[1]))
        break
    
    frameI = frameI+1
    if (frameI > 10):
        print(Dicio)
        break
        
    
# fazer esse for dentro da merge
for i in Dicio[classid+1]: #elementos tipo
    #print("i",i)
    for j in i.values():
        #print("j",j)
        print(len(j))  #outro dic
        #for f in j: # cada elemento da lista ####nao vai existir mais (PEGAR SÓ A ULTIMA POSICAO J(ÚLTIMO FRAMESS))
            #print(f) # f é um dic
        for bx in j[len(j)-1].values():
                #print("Distancia", distancia(bx,Dicio[9][0]['boat1'][0][0],))
                print(bx) 



                          
print(Dicio)
#print(Dicio[9])
#print(distancia(Dicio[9][0]['boat1'][0][0],Dicio[9][1]['boat2'][0][0]))
#print(Dicio[9][0]['boat1'][0][0][0])


    
    
    
   

#Destruir todas janelas e fechar programa
cap.release()
cap.destroyAllWindows()
