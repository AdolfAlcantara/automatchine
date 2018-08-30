from tkinter import *
from node import *
from regularexpresion import *
from nfa import *


class MainWindow:
    

    def __init__(self,master):

        self.master=master
        self.master.geometry('300x150')
        self.master.title('Automatas')

        #labels
        self.states = Label(master,text="Estados: ")
        self.alphabet = Label(master,text="Alfabeto: ")
        self.initial_state = Label(master,text="Estado inicial: ")
        self.final_states = Label(master,text="Estados finales: ")

        #entrys
        self.entry_states = Entry(master)
        self.entry_states.insert(END,'0,1,2,3,4,5')
        self.entry_alphabet = Entry(master)
        self.entry_alphabet.insert(END,'a,b')
        self.entry_istate = Entry(master)
        self.entry_istate.insert(END,'0')
        self.entry_fstates = Entry(master)
        self.entry_fstates.insert(END,'2,3,4')

        #buttons
        self.start_btn = Button(master,text="Crear",command=self.createTable)

        #grid construction
        self.states.grid(row=0,sticky=W)
        self.alphabet.grid(row=1,sticky=W)
        self.initial_state.grid(row=2,sticky=W)
        self.final_states.grid(row=3,sticky=W)

        self.entry_states.grid(row=0,column=1,sticky=W)
        self.entry_alphabet.grid(row=1,column=1,sticky=W)
        self.entry_istate.grid(row=2,column=1,sticky=W)
        self.entry_fstates.grid(row=3,column=1,sticky=W)

        self.start_btn.grid(row=3,column=2)


        
        # states_array = states.get().split(",")
        # fstates_array = final_states.get().split(",")
        # istate = initial_state.get()



    def createTable(self):
        root2=Toplevel(self.master)
        myGUI = TransitionTable(
            root2,
            self.entry_states.get().split(","),
            self.entry_alphabet.get().split(","),
            self.entry_fstates.get().split(","),
            self.entry_istate.get())

class TransitionTable:

    def __init__(self,master,array_states,array_alpha,array_fstates,istate):
        self.master=master
        self.master.title('Automatas')

        self.fstates = array_fstates
        self.valuesGotten = False
        self.arr_alpha = array_alpha
        self.arr_nodos=[]
        self.transitionDict={}

        def isFinal(value):
            for x in self.fstates:
                if x == value:
                    return True
            return False

        counter = 0
        for x in array_states:
            counter+=1
            # label = Label(master, text=x)
            # label.grid(row=counter,sticky=W+E+N+S)
            if x == istate:
                if isFinal(x):
                    label = Label(master, text=x, foreground="blue", background="green",font=("Helvetica", 16))
                    label.grid(row=counter,sticky=W+E+N+S)
                    self.arr_nodos.append(node(x,True,True))
                    continue
                else:
                    label = Label(master, text=x,foreground="blue",font=("Helvetica", 16))
                    label.grid(row=counter,sticky=W+E+N+S)
                    self.arr_nodos.append(node(x,True,False))
                    continue
            elif isFinal(x):
                    label = Label(master, text=x,background="green",font=("Helvetica", 16))
                    label.grid(row=counter,sticky=W+E+N+S)
                    self.arr_nodos.append(node(x,False,True))
                    continue
            else:
                label = Label(master, text=x,font=("Helvetica", 16))
                label.grid(row=counter,sticky=W+E+N+S)
                self.arr_nodos.append(node(x,False,False))
                continue

        counter = 1
        for x in array_alpha:
            label = Label(master, text=x,font=("Helvetica", 16)).grid(row=0,column=counter)
            counter+=1
        
        valores = ['1,4','3','1','2','5','5','5','5','5','4','5','5']
        contador=0
        counterx = 1
        for x in array_states:
            countery = 1
            for y in array_alpha:
                celda = Entry(master)
                celda.insert(END,valores[contador])
                celda.grid(row=counterx,column=countery)
                self.transitionDict[(counterx,countery)] = celda
                contador+=1
                countery+=1
            counterx+=1

        self.cadena = Entry(master)
        self.cadena.grid(row=counterx,column=countery-2,columnspan=2)
        self.DFA = Button(master,text="DFA",command=self.getDFA).grid(row=counterx,column=countery)
        self.ER = Button(master,text="ER",command=self.toRE).grid(row=counterx-1,column=countery)
        self.NFA = Button(master,text="NFA", command=self.getNFA).grid(row=counterx-2,column=countery)


    def getDFA(self):
        if not self.valuesGotten:
            self.getValuesFromTable()
            self.valuesGotten=True
        self.EvaluateString()
        self.transitionDict.clear()

    def getNFA(self):
        self.getValuesFromTable()
        tempNode = self.getInitialState()
        _nfa = nfa(self.arr_nodos,tempNode,self.fstates)
        _nfa.toDFA()
        # for x in self.arr_nodos:
        #     print(x.name)
        #     print(x.init)
        #     print(x.final)
        #     print(x.directionsDict)
            


    def getNodo(self,nodename):
        for x in self.arr_nodos:
            if(x.name == nodename):
                return x

    def EvaluateString(self):
        # count=0
        tempNode = self.getInitialState()
        print(tempNode.directionsDict)
        # while count<len(self.cadena.get()):
        for x in self.cadena.get():
            if x in tempNode.directionsDict:
                tempNode = tempNode.directionsDict[x][0]
                print("Inside loop")
                print(tempNode)
            else:
                break
        if(tempNode.final):
            print("Aceptada")
        else:
            print("No aceptada")
    
    def getInitialState(self):
        for x in self.arr_nodos:
            if x.init:
                return x
        print("Error, no initial state")

    def getValuesFromTable(self):
        contadorx = 1
        for x in self.arr_nodos:
            contadory = 1 
            for y in self.arr_alpha:
                for z in self.transitionDict[(contadorx,contadory)].get().split(","):
                    nodo = self.getNodo(z)
                    if y in  x.directionsDict:
                        x.directionsDict[y].append(nodo)
                    else:
                        x.directionsDict[y] = [nodo]
                contadory+=1
            contadorx+=1

    def toRE(self): 
        if not self.valuesGotten:
            self.getValuesFromTable()
            self.valuesGotten=True

        re = regularexpresion(self.arr_nodos)
        re.addEpsilonStates(self.getInitialState())
        re.getRE()
       

def main():
    root = Tk()
    main = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()