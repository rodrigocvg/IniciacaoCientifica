def merge5(DicioClassId, box, frameI, idObj):
    # print("len",len(DicioClassId), idObj)
    if (len(DicioClassId) is None):
        DicioClassId.append({idObj: [{frameI: box}]})
        # print ("adicionando novo")

    menorDist = 600

    for boats in DicioClassId:
        # print("boats" , boats)
        for frameBox in boats.values():
            # print("framebox",frameBox)
            for umavez in frameBox:  # roda apenas uma vez, pq so tem um
                #print("box", umavez)
                #print("frame corrente", frameI, " box corrente", box)
                for boxFOR in umavez.values():
                    distanciaI = distancia(box, boxFOR)
                    # print("box : ", box , "boxFor: ", boxFOR , "distancia entre" ,distanciaI)
                    if (distanciaI < menorDist):
                        menorDist = distanciaI
                        menorDistObj = box
                        # print(menorDist,menorDistObj)
                        if (menorDist < 10):
                            frameBox.append(
                                {str(frameI)+"da merge": menorDistObj})

                        else:
                            # print("kkdsadj")
                            DicioClassId.append(
                                {"da merge"+str(idObj): [{frameI: box}]})

                    # print(boxFOR)

def merge6(DicioClassId, box, frameI, idObj):
    # print("len",len(DicioClassId), idObj)

    # print ("adicionando novo")

    menorDist = 600

    for boats in DicioClassId:
        for frameBox in boats.values():  # pegar ultimo de boats.values
            #print("framebox", frameBox)
            for umavez in frameBox:  # roda apenas uma vez, pq so tem um
                for boxFOR in umavez.items():
                    if (frameI == boxFOR[0]+1):
                        #print("frameI", frameI, " keys", boxFOR)
                        distanciaI = distancia(box, boxFOR[1])
                    else:
                        distanciaI = 9000
                    # print("box : ", box , "boxFor: ", boxFOR , "distancia entre" ,distanciaI)
                    if (distanciaI < menorDist):
                        menorDist = distanciaI
                        menorDistObj = box
                        # print(menorDist,menorDistObj)
                        if (menorDist < 10):
                            frameBox.append({frameI: menorDistObj})

                        else:
                            DicioClassId.append({idObj: [{frameI: box}]})

def merge7(DicioClassId, box, frameI, idObj):
    menorDist = 600
    limiar = 20

    for boats in DicioClassId:
        for frameBox in boats.values():  # pegar ultimo de boats.values
            ultimoFrameBox = frameBox[len(frameBox)-1]
            distanciaI = distancia(box, list(ultimoFrameBox.values())[0])
            #print(len(frameBox)-1)
            #(box,list(ultimoFrameBox.values())[0])
            #print(box, list(ultimoFrameBox.values())[0],distanciaI)
            if (distanciaI < menorDist):
                menorDist = distanciaI
                menorDistObj = boats
    
    #print("objmenordist",menorDistObj)
    if (menorDist < limiar):
        #print("fazendo append")
        #if not{frameI:menorDistObj} in  frameBox:
            #frameBox.append({frameI: menorDistObj})
            list(menorDistObj.values()).append({frameI: box}) #não faz parte do dicio

    else:
        #print("nova entrada")
        #if not {idObj: [{frameI: box}]} in DicioClassId:
            DicioClassId.append({idObj: [{frameI: box}]})