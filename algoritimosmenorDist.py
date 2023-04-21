# def merge(latu):  #merge(lof,latu)
   # lof = {box,class_names[classid]}
  #  limiar = 20
   # for (class_names[classid]) in latu:
    #    listaObj = buscarPorClassid(lof[1][0],class_names[classid])    # fazer buscaPorClassid
     #   if listaObj != [] :
     #       for i in range(i,listaObj):
     #           menorDist = menorDistancia(lof,latu)    #menorDistancia(lof.box, latu.box)
      #          if menorDist <= limiar:
       #             print("1")
                    #lof[1] = class_names[classid]
   # return lof
def merge(obj1,DictionaryFinal,classId):
    dictionaryClassId = DictionaryFinal[classId]
    if (dictionaryClassId is None):
       #cria nova entrada no DictionaryFinal e coloca obj1
       DictionaryFinal.append(obj1)
       print(1)
    else:        
      menorDistancia = distancia(obj1,dictionaryClassId[0]['boat1'][0][0])
      menorDistObj = dictionaryClassId[0]
      for i in dictionaryClassId:
          print("dentro da merge",i['boat1'][0][0])
          di = distancia(obj1,i['boat1'][0][0])
          if (di < menorDistancia):
             menorDistancia = di
             menorDistObj = i  
          
      print("Menor distancia = ", menorDistancia)
      limiar = 20
    if (menorDistancia <= limiar):
        #unir obj com o menorDistObj;
        DictionaryFinal.popitem() #exclui ultimo elemento adicionado
        print('menordis < limiar')
    else:
        #cria uma nova entrada com o obj no dictionaryClassId
        DictionaryFinal.append(obj1)
        print('nova entradaw')


    
#lista
def menorDistancia4(obj1,obj2):
    Umx1 = obj1["box"]["box"][0]
    Umx2 = obj1["box"]["box"][2]
    Umy1 = obj1["box"]["box"][1]
    Umy2 = obj1["box"]["box"][3]
 

    Doisx1 = obj2["box"]["box"][0]
    Doisx2 = obj2["box"]["box"][2]
    Doisy1 = obj2["box"]["box"][1]
    Doisy2 = obj2["box"]["box"][3]

    CentroLofX = Umx2 - (Umx1/2)
    CentroLofY = Umy2 - (Umy1/2)


    CentroLatuX = Doisx2 - (Doisx1/2)
    CentroLatuY = Doisy2 - (Doisy1/2)


    dist = math.sqrt((CentroLofX - CentroLatuX)**2 + (CentroLofY - CentroLatuY)**2)

    return dist
    


# def buscaPorClassid(lof,class_names):
#DicDetcOfic[9][0]["box"]["box"][0] = x1
#Parametros = Dicionario, classid, i e j = objetos que serão comparados
def menorDistancia3(DicDetcOfic,classid,i,j): 
    Ob1x1 = DicDetcOfic[classid][i]["box"]["box"][0]
    Ob1x2 = DicDetcOfic[classid][i]["box"]["box"][2]
    Ob1y1 = DicDetcOfic[classid][i]["box"]["box"][1]
    Ob1y2 = DicDetcOfic[classid][i]["box"]["box"][3]

    Ob2x1 = DicDetcOfic[classid][j]["box"]["box"][0]
    Ob2x2 = DicDetcOfic[classid][j]["box"]["box"][2]
    Ob2y1 = DicDetcOfic[classid][j]["box"]["box"][1]
    Ob2y2 = DicDetcOfic[classid][j]["box"]["box"][3]
    CentroLofX = Ob1x2 - Ob1x1/2
    CentroLofY = Ob1y2 - Ob1y1/2


    CentroLatuX = Ob2x2 - Ob2x1/2
    CentroLatuY = Ob2y2 - Ob2y1/2

    dist = math.sqrt((CentroLofX - CentroLatuX)**2 + (CentroLofY - CentroLatuY)**2)

    return dist


#mudar menorDistancia para Dicionario

def menorDistancia(lof,latu):   
    #retornar de quem é a menor distancia tb
    #CentroLofX = x2 - x1/2 
   CentroLofX = lof[0][2] - (lof[0][0]/2)
    #CentroLofY= y2 - y1/2
   CentroLofY = lof[0][3] - (lof[0][1]/2)
    #CentroLatuY = x2 -x1/2
   CentroLatuX = latu[0][2] - (latu[0][0]/2)
    #CentroLofY= y2 - y1/2
   CentroLatuY = latu[0][3] - (latu[0][1]/2)
    

   dist = math.sqrt((CentroLofX - CentroLatuX)**2 + (CentroLofY - CentroLatuY)**2)

   #dist = math.sqrt((lof[0][0] - lof[0][1])^2 + (latu[0][0] - latu[0][1])^2)   # provavel errado
   return dist


def menorDistancia2(lof,latu):
    x1lof = lof[0][0] 
    y1lof = lof[0][1]
    x2lof = lof[0][2]
    y2lof = lof[0][3]
    CentroLof = math.sqrt((x1lof - x2lof)^2 + (y1lof - y2lof)^2)
    x1latu = latu[0][0] 
    y1latu= latu[0][1]
    x2latu= latu[0][2]
    y2latu = latu[0][3]
    CentroLatu = math.sqrt((x1latu - x2latu)^2 + (y1latu - y2latu)^2)
    dist = CentroLof - CentroLatu
    return dist

 

#dicionario = chave = classnames[class id]
#             valor = listaObj


def menorDistancia5(obj1,obj2):
    Umx1 = obj1["box"]["box"][0]
    Umx2 = obj1["box"]["box"][2]
    Umy1 = obj1["box"]["box"][1]
    Umy2 = obj1["box"]["box"][3]

    #for 
    Doisx1 = obj2["box"]["box"][0]
    Doisx2 = obj2["box"]["box"][2]
    Doisy1 = obj2["box"]["box"][1]
    Doisy2 = obj2["box"]["box"][3]




    #Demais códigos

    #DicValor.update(dicFrame)
        #DicValor[idObj] = dicFrame
        #DicValor[idObj].append({"DicFrame":dicFrame})

     #print(i,box, class_names[classid])
        # var = var + 1
        #ListaDetcAtual = [box, class_names[classid]]
        #ListaDetecOfic = merge(ListaDetecAtual)
        #print(i, ListadetcAtual) 
        #DicDetcOfic = {classid+1:ListaDetcOfic}  #DicDetcOfc = {class_names[classid]:ListadetcOfc}
        #valor = DicDetcOfic[classid+1]
        #if not classid+1 in DicDetcOfic:
            #DicDetcOfic[classid+1] = [{class_names[classid],box}] 
           # DicDetcOfic[classid+1] = []
        #if not frameI in dicFrame:
        

        
        #merge(box, Dicio[classid+1])


        #print(Dicio[classid+1]) #classID
        
        #DicValor = {}
        #else:
        #DicDetcOfic[classid+1].append({class_names[classid],box})
        # fazendo append de todas as detecções e colocando em apenas um dicionário
        #DicDetcOfic[classid+1].append({"classname": class_names[classid], "box": box, "frame":i})
        #DicDetcOfic[classid+1].append({"classname": class_names[classid], "box": {"frame":i,"box":box}})
        #ListaDetcAtual.append([box,class_names[classid]])   
        # DicDetcOfic[9][0]["classname"] = boat / 9 = key, 0 = primeira detecção
        #print(ListadetcAtual[0][0])

        #print(DicDetcOfic)
        #print()
        #print(ListaDetcAtual)
        #print(DicDetcOfic[9][0]["box"]["box"][0])
        #print(menorDistancia3(DicDetcOfic,9,0,1))
        #print(menorDistancia4(DicDetcOfic[9][0],DicDetcOfic[9][1]))
        #print(merge(DicDetcOfic)) 

for i in Dicio[classid+1]: #elementos tipo
    #print("i",i)
    for j in i.values():
        #print("j",j)
        print(len(j))  #outro dic
        for f in j: # cada elemento da lista ####nao vai existir mais (PEGAR SÓ A ULTIMA POSICAO J(ÚLTIMO FRAMESS))
            #print(f) # f é um dic
            for bx in f.values():
                #print("Distancia", distancia(bx,Dicio[9][0]['boat1'][0][0],))
                print(bx)
