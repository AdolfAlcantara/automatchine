from node import *

class nfa:

    def __init__ (self,array_nodes,firstNode, lastNodes):
        self.arr_nodes = array_nodes
        self.initialNode = firstNode
        self.finalNodes = lastNodes
        self.new_arr_nodes = [self.initialNode]

    def toDFA(self):
        for nodo in self.new_arr_nodes:
            print(nodo.name)
            print(nodo.directionsDict)
            newDir = [] #new directions for the actual node
            for dirItem in nodo.directionsDict.items():
                # print(dirItem)
                print("len(diritem): ")
                print(len(dirItem[1]))
                print(dirItem)
                if len(dirItem[1])>1:
                    #namegetter
                    contador=0
                    arr_new_node_goesto = []
                    arr_new_node_goesto.extend(dirItem[1][contador].directionsDict.items())
                    node_name=dirItem[1][contador].name
                    contador+=1
                    while contador<len(dirItem[1]):
                        print("contador: ")
                        print(contador)
                        node_name+=","+dirItem[1][contador].name #get name for the new node
                        arr_new_node_goesto.extend(dirItem[1][contador].directionsDict.items()) #get directions for the new node
                        contador+=1
                    
                    new_node = node(node_name,False,False)
                    if new_node not in self.new_arr_nodes:
                        self.new_arr_nodes.append(new_node)
                    else:
                        break
                    
                    key  = dirItem[0]
                    # del nodo.directionsDict[key]
                    newDir.append((key,new_node))

                    print("new node goes to: ")
                    print(arr_new_node_goesto)
                    for x in arr_new_node_goesto:
                        if x[0] in new_node.directionsDict:
                            new_node.directionsDict[x[0]].extend(x[1])
                        else:
                            new_node.directionsDict[x[0]] = x[1]
                    arr_new_node_goesto.clear()

                    print("new node: ")
                    self.printNodos([new_node])
                    print("new node goes to: ")
                    print(arr_new_node_goesto)

                    # print("new arr nodes: ")
                    # self.printNodos(self.new_arr_nodes)
                    # print ("actual arr_nodes:")
                    # self.printNodos(self.arr_nodes)
                else:
                    if dirItem[1][0] in self.new_arr_nodes:
                        break
                    else:
                        self.new_arr_nodes.append(dirItem[1][0])
           
            for x in newDir:
                del nodo.directionsDict[x[0]]
                key = x[0]
                if key in nodo.directionsDict:
                    nodo.directionsDict[key].append(x[1])
                else:
                    nodo.directionsDict[key] = [x[1]]
            
            # self.printNodos(self.new_arr_nodes)
                

            
            


                    
    def directionsGetter(self, nodo):
        return 

    
    def printNodos(self,array):
        for x in array:
            print(x.name)
            print(x.init)
            print(x.final)
            print(x.directionsDict)
