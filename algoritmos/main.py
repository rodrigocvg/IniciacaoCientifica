import cv2
import time
import math
import json
 
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

    for boats in DicioClassId:
        for frameBox in boats.items():  # pegar ultimo de boats.values
            #print(frameBox)
            ultimoFrameBox = frameBox[1][len(frameBox[1])-1]
            distanciaI = distancia(box, list(ultimoFrameBox.values())[0])
            if (distanciaI < menorDist):
                menorDist = distanciaI
                menorDistObj = frameBox[0]
    

    if (menorDist < limiar):
        #list(menorDistObj.values()).append({frameI: box}) #não faz parte do dicio
        for boats2 in DicioClassId:
            for frameBox2 in boats2.items():
                if frameBox2[0] == menorDistObj:
                    frameBox2[1].append({frameI: box})

    else:
        DicioClassId.append({idObj: [{frameI: box}]})

#print(cv2.__version__)

# Cores
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# Carrega as classes do coco.names
class_names = []
with open("coco.names.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Carrega o vídeo usando OpenCv
cap = cv2.VideoCapture("E:\\IC\\videos\\vigilancia.mp4")



# Carregando os weights da rede neural
net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg.txt")

# Setar parametros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

frameI = 0

Dicio = {}
contDetec = 0

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

    # Programa finaliza no 'ESC'
    if cv2.waitKey(1) == 27:

        video_info = {
        "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        "fps": int(cap.get(cv2.CAP_PROP_FPS)),
        "frames": frameI
        }

        print(json.dumps(video_info))
        #Transformando Dicionário em json e salvando em arquivo
        json = json.dumps(Dicio)
        arq = open("outputs/arquivo.json", "w")
        arq.write(json)

        break


    if (frameI > 3000):

        json = json.dumps(Dicio)
        arq = open("outputs/arquivo.json", "w")
        arq.write(json)

        break

# Destruir todas janelas e fechar programa
cap.release()
cap.destroyAllWindows()
