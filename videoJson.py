import cv2
import json
from time import sleep
import time


# Carrega o vídeo usando OpenCv
cap = cv2.VideoCapture("E:\\IC\\videos\\vigilancia.mp4")

arq = open("E:\\IC\\outputs\\arquivo.json", "r")

Dicio = json.load(arq)
frameI = 0

tempos = {}
tempos2 = {}
dados_json = []


while True:

    # Captura dos frames
    _, frame = cap.read()

    contDetec = 0
    
    #Iterar sobre as chaves e valores do arquivo JSON
    for key, valor in Dicio.items():
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
                                        # tempos2["label"] = item_chave
                                        # tempos2["start"] = tempo_atual
                                        # tempos2["finish"] = None
                                        # tempos2["meeting"] = 0
                                        #print(tempos2)
                                        dados_json.append(tempos2)
                                    else:
                                        # Se a chave já está no dicionário de tempos, atualize o tempo de término
                                        #tempos[item_chave]["fim"] = tempo_atual
                                        tempos2["finish"] = tempo_atual
                                        

                                    x, y, width, height = coord
                                    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
                                    cv2.putText(frame, str(item_chave), (x, y - 10), cv2.QT_FONT_NORMAL, 0.5, (0, 255, 0), 2)
                                    
    sleep(0.1)
    #fim = time.time()
    
    #fps_text = f"FPS: {round((1.5/(fim - começo)),2)}"
    #cv2.putText(frame, fps_text, (0, 25),
   #             cv2.QT_FONT_NORMAL, 1, (0, 255, 0), 3)

    cv2.imshow("teste", frame)
    frameI = frameI + 1
    
    if cv2.waitKey(1) == 27:
        break
# print(tempos)

#print(json.dumps(dados_json))
detections = json.dumps(dados_json)
arq = open("outputs/myTime_bars_input.json", "w")
arq.write(detections)
