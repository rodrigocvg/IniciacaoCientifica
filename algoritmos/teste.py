import cv2
import json

def draw_rectangles_on_frame(frame, dicio):
    color = (0, 255, 0)  # Cor do retângulo (verde)
    thickness = 2  # Espessura do retângulo

    for classId in dicio:
        for idObjs in dicio.get(classId):
            for boxFrame in idObjs.values():
                for frameDict in boxFrame:
                    for frameKey, coords in frameDict.items():
                        # Descompacta as coordenadas
                        x, y, w, h = coords

                        # Desenha o retângulo no frame
                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)

                        # Coloca o número do frame como texto na tela
                        cv2.putText(frame, frameKey, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

    return frame

arq = open("outputs/arquivo.json", "r")

Dicio = json.load(arq)

# Carrega o vídeo
video_path = 'videos/vid.mp4'
cap = cv2.VideoCapture(video_path)

# Verifica se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Obtém as informações do vídeo
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Configura o codec de vídeo para gravar o arquivo de saída
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_path = 'videos/output.mp4'
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Aplica a função para desenhar os retângulos no frame
    frame_com_retangulos = draw_rectangles_on_frame(frame, Dicio)

    # Grava o frame com os retângulos no arquivo de saída
    out.write(frame_com_retangulos)

    # Exibe o frame com os retângulos
    cv2.imshow('Frame com Retângulos', frame_com_retangulos)

    # Verifica se a tecla 'q' foi pressionada para interromper o loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos utilizados
cap.release()
out.release()
cv2.destroyAllWindows()