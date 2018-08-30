from node import *

class regularexpresion:

    def __init__(self, arr_nodes):
        self.arr_nodos = arr_nodes

    def addEpsilonStates(self,initialNode):
        
        tempNode = initialNode
        tempNode.init = False
        newInitNode = node("initial",True,False)
        newInitNode.directionsDict['$'] = [tempNode]
        newFinalNode = node("final",False,True)
        for x in self.arr_nodos:
            if x.final:
                x.directionsDict['$'] = [newFinalNode]
                x.final = False
        self.arr_nodos.extend([newInitNode,newFinalNode])


    def getRE(self):
        for x in self.arr_nodos:
            if (not x.init and not x.final):
                self.deleteNode(x)
                self.getRE()
        value=""
        for x in self.arr_nodos:
            if(x.init):
                for y in x.directionsDict.items():
                    if not y[1]:
                        continue
                    else:
                        value+=y[0]+"+"
        print (value)
        return 

    def deleteNode(self,delNode):

        arr_comesFrom=[]
        arr_goesTo=[]
        arr_ciclo = []

        for x in delNode.directionsDict.items():
            if delNode in x[1]:
                arr_ciclo.append(x[0])
        
        if len(arr_ciclo)==0:
            valorCiclo=""
        elif len(arr_ciclo)==1:
            valorCiclo="("
            for x in arr_ciclo:
                valorCiclo+=x
            valorCiclo+=")*"
        else:
            valorCiclo="("
            for x in arr_ciclo:
                valorCiclo+=x+"+"
            valorCiclo+=")*"
            

        for x in self.arr_nodos:
            for y in x.directionsDict.items():
                if delNode in y[1]:
                    arr_comesFrom.append((y[0]+valorCiclo,x))
                    y[1].remove(delNode)

        for x in delNode.directionsDict.items():
            for y in x[1]:
                arr_goesTo.append((x[0],y))
                     
        print(arr_comesFrom)
        print(arr_goesTo)
        self.arr_nodos.remove(delNode)
        print(arr_comesFrom)
        # print(arr_comesFrom2)
        print(arr_goesTo)

        for x in arr_comesFrom:
            for y in arr_goesTo:
                x[1].directionsDict[x[0]+y[0]] =[ y[1] ]
        self.printNodos()


    def printNodos(self):
        for x in self.arr_nodos:
            print(x.name)
            print(x.init)
            print(x.final)
            print(x.directionsDict)