# IniciacaoCientifica
Detecção e Rastreamento de Objetos com YOLOv4-tiny e OpenCV
Este código utiliza a biblioteca OpenCV e a arquitetura de rede neural YOLOv4-tiny para realizar a detecção e rastreamento de objetos em um vídeo. O código foi desenvolvido em Python e é dividido em três partes principais:

Detecção e Rastreamento Inicial (detect_track.py):

Realiza a detecção de objetos em cada frame do vídeo usando a arquitetura YOLOv4-tiny.
Rastreia a movimentação dos objetos entre frames, utilizando um algoritmo de cálculo de distância entre bounding boxes.
Gera um arquivo JSON contendo informações sobre as detecções, como coordenadas dos objetos, frames correspondentes, e informações do vídeo.
Instruções de Uso:

Execute o script com o comando python detect_track.py video.mp4.
Substitua "video.mp4" pelo caminho do vídeo desejado.

O que faz?

Carrega o arquivo JSON gerado na etapa anterior.
Utiliza as informações para criar uma representação visual temporal das detecções no vídeo.
Cada objeto é representado por uma barra horizontal, indicando o tempo em que o objeto esteve presente no vídeo.

Exportação de Dados:

Carrega o arquivo JSON de detecções.
Converte as informações para um formato desejado, a ser utilizado em outros contextos.
Exporta os dados para um novo arquivo JSON.

Dependências:
OpenCV
Numpy
Observações:
Certifique-se de ter o arquivo "coco.names.txt" contendo os nomes das classes no mesmo diretório.
Os arquivos "yolov4-tiny.weights" e "yolov4-tiny.cfg.txt" devem estar presentes no mesmo diretório para a detecção funcionar.
O código está configurado para processar até 5000 frames do vídeo. Este valor pode ser ajustado conforme necessário.
