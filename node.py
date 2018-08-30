class node :

    #name=state,array_dir=where to connect,init and final boolean to know if its final or initial state 
    def __init__(self,name,init, final):
        self.name = name
        self.init = init
        self.final = final
        self.directionsDict = {}
