import cv2
import time
import math
import json
import sys
from time import sleep
 
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

def merge(DicioClassId, box, frameI, idObj):

    menorDist = 600
    #limiar diferentes para cada tipo obj
    limiar = 100

    for objs in DicioClassId:
        for frameBox in objs.items():  # pegar ultimo de boats.values
            ultimoFrameBox = frameBox[1][len(frameBox[1])-1]
            distanciaI = distancia(box, list(ultimoFrameBox.values())[0])
            if (distanciaI < menorDist):
                menorDist = distanciaI
                menorDistObj = frameBox[0]
    

    if (menorDist < limiar):
        for objs2 in DicioClassId:
            for frameBox2 in objs2.items():
                if frameBox2[0] == menorDistObj:
                    frameBox2[1].append({frameI: box})

    else:
        DicioClassId.append({idObj: [{frameI: box}]})

# Cores
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# Carrega as classes do coco.names
class_names = []
with open("coco.names.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
 
for parametro in sys.argv:
        if('.mp4' in parametro):
            video = parametro

cap2 = cv2.VideoCapture(video)

# Carregando os weights da rede neural
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg.txt")

# Setar parametros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

frameI = 0
Dicio = {}
contDetec = 0
DicioFinal = {}

# Capturando os frames com OpenCv, loop infinito
while True:

    # Captura dos frames
    _, frame = cap2.read()

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
        cv2.putText(frame, text, (box[0], box[1]-15),cv2.QT_FONT_NORMAL, 0.5, color, 2)

        idObj = class_names[classid] + str(contDetec)  # boat1 boat2

        classidINT = int(classid+1)
        
        box2 = box.tolist()

        if not classidINT in Dicio:
            Dicio[classidINT] = []
            
            Dicio[classidINT].append({idObj: [{frameI: box2}]})

        else:
            merge(Dicio[classidINT], box2, frameI, idObj)

        #Contagem das detecções
        contDetec += 1

    # Calculando o FPS
    fps_text = f"FPS: {round((1.5/(fim - começo)),2)}"

    # Colocando FPS na tela
    cv2.putText(frame, fps_text, (0, 25), cv2.QT_FONT_NORMAL, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_text, (0, 25),
                cv2.QT_FONT_NORMAL, 1, (0, 255, 0), 3)

    # Mostrando imagem
    cv2.imshow("teste", frame)

    #Frames
    frameI = frameI+1
    

    #finaliz 5000 frames
    if (frameI > 5000):
        break

video_info = {
        "width": int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height": int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        "fps": int(cap2.get(cv2.CAP_PROP_FPS)),
        "frames": frameI
        }

DicioFinal['DicioDeteccoes'] = Dicio
DicioFinal['VideoInfos'] = video_info
json2 = json.dumps(Dicio)
arq = open("outputs/arquivo.json", "w")
arq.write(json2)
# Destruir todas janelas e fechar programa
cap2.release()
# cap2.destroyAllWindows()


#Parte 2
# Carrega o vídeo usando OpenCv
cap = cv2.VideoCapture(video)

arq = open("outputs/arquivo.json", "r")

Dicio3 = json.load(arq)
frameI = 0

tempos = {}
tempos2 = {}
dados_json = []

while True:

    # Captura dos frames
    _, frame = cap.read()

    contDetec = 0
    
    #Iterar sobre as chaves e valores do arquivo JSON
    for key, valor in Dicio3.items():
            for item in valor:
                # Iterar sobre as chaves e valores do items
                for item_chave, item_valor in item.items():
                        # Iterar sobre os retângulos do item
                        for rectangle_data in item_valor:
                           #print(rectangle_data) 
                           for frameItem, coord in rectangle_data.items():
                                if int(frameItem)==frameI:
                                    tempo_atual = frameI / cap.get(cv2.CAP_PROP_FPS)
                                    if item_chave not in tempos:
                                        # Se a chave ainda não está no dicionário de tempos, registre o tempo de início
                                        tempos[item_chave] = {"inicio": tempo_atual, "fim": None}

                                        tempos2 = {
                                             "label":item_chave,
                                             "start": tempo_atual,
                                             "finish": None,
                                             "meeting": 0
                                        }
                                        dados_json.append(tempos2)
                                    else:
                                        # Se a chave já está no dicionário de tempos, atualize o tempo de término
                                        tempos2["finish"] = tempo_atual

                                    x, y, width, height = coord
                                    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
                                    cv2.putText(frame, str(item_chave), (x, y - 10), cv2.QT_FONT_NORMAL, 0.5, (0, 255, 0), 2)
                                    
    sleep(0.1)

    cv2.imshow("teste", frame)
    frameI = frameI + 1
    
    # if cv2.waitKey(1) == 27:
    #     break
    if (frameI > 5000):
        break

DicioFinal['MY_Time_bars_input_Cibelle'] = dados_json
detections = json.dumps(dados_json)
arq = open("outputs/myTime_bars_input.json", "w")
arq.write(detections)


#Parte 3
arq = open("outputs/arquivo.json", "r")

Dicio2 = json.load(arq)

dados_json = []

# Itere sobre as chaves (IDs) e os valores (listas de quadros) do dicionário de entrada
for id, quadros in Dicio2.items():
    for quadro in quadros:
        # Crie um dicionário com a estrutura desejada
        for chave,item in quadro.items():

            novo_dicionario = {
                "label":chave,  # Obtém o rótulo do dicionário
                "trajectory": []
            }
            #print(item)
            for i in item:
                listaBox = list(i.values())[0]
                frame_data = {
                    "frame": 0,
                     "cx": listaBox[0],
                    "cy": listaBox[1],
                    "dx": listaBox[2],
                    "dy": listaBox[3]
                }
                novo_dicionario["trajectory"].append(frame_data)
                dados_json.append(novo_dicionario)

#print(dados_json)
DicioFinal['My_Detections_Cibelle'] = dados_json

DicioFinalJson = json.dumps(DicioFinal)
arqFinal = open("outputs/DicioFinal.json", "w")
arqFinal.write(DicioFinalJson)




