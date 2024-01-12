import json

arq = open("E:\\IC\\outputs\\arquivo.json", "r")

Dicio = json.load(arq)
#print(Dicio)


dados_json = []

# Itere sobre as chaves (IDs) e os valores (listas de quadros) do dicionário de entrada
for id, quadros in Dicio.items():
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
detections = json.dumps(dados_json)
arq = open("outputs/myDetections.json", "w")
arq.write(detections)
