# -*-coding:Utf-8 -*
"""
INSTALLER WXPYTHON POUR EXECUTER CETTE CLASSE (INTERFACE GRAPHIQUE)
"""
import sys
sys.path.append('..')

from hydraulic_network import GlobalNetwork
import wx
import random
from optimization import *

class App(wx.App):
    def OnInit(self):
        app = GraphicalInterface(None,-1,"Localisation des vannes dans les systèmes de distribution d'eau")
        app.Center()
        app.Show()
        self.SetTopWindow(app)
        return True

class GraphicalInterface(wx.Frame):
    def __init__(self,  parent,id,title):
        wx.Frame.__init__(self,parent,id,title, pos=(0, 0), size=(442, 280), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX) )
        self.parent = parent
        self.initialize()
        self.Show(True)
    
    def initialize(self):
        imageFile = "../../images/mainmenu.png"
        png = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))

        button_start_simulation = wx.Button(self,-1,label="Commencer", pos = (330, 5), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_sim, button_start_simulation)

        button_doc = wx.Button(self,-1,label="Documentation", pos = (330, 45), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_doc, button_doc)

        button_exit = wx.Button(self,-1,label="Quitter", pos = (330, 220), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_exit, button_exit)
        
        self.Show(True)
    
    def on_button_click_sim(self,event):
        frame = GuiGraph()
        frame.Show()

    def on_button_click_exit(self,event):
        self.Destroy()

    def on_button_click_doc(self,event):
        frame = GuiDocumentation()
        frame.Show()


class GuiDocumentation(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, size=(574, 511), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Center()
        self.SetTitle('Documentation')
        self.initialize()
        self.Show(True)

    def initialize(self):
        self.label1 = wx.StaticText(self,-1,label='Ici vous pouvez apprendre davantage sur le sujet.', pos=(5, 0))
        questions = ['Veuillez choisir une question ici', 'A quoi sert cette simulation?', 'Quels sont les algorithmes utilisés et quelles sont les différences?', 'Quels sont les critères appliqués aux algorithmes?', 'Quelles sources a-t-on utilisé pour la réalisation du projet?']
        self.comboBox = wx.ComboBox(self, pos=(2, 30), size =(450, 50), choices=questions, style=wx.CB_READONLY, value = 'Veuillez choisir une question ici')
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        self.answers = wx.StaticText(self, -1, '')  
        self.answers2 = wx.StaticText(self, -1, '')
        self.answers3 = wx.StaticText(self, -1, '')
        self.answers4 = wx.StaticText(self, -1, '')
        self.answers5 = wx.StaticText(self, -1, '')
        self.answers6 = wx.StaticText(self, -1, '')
        self.answers7 = wx.StaticText(self, -1, '')
        self.answers8 = wx.StaticText(self, -1, '')
        
        button_exit = wx.Button(self,-1,label="Retour au menu principal", pos=(0, 431), size=(572, 50))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_exit, button_exit)
        self.Show(True)

    def OnSelect(self, event):
        self.clearLabels()
        if self.comboBox.GetValue()=='A quoi sert cette simulation?':
            self.posLabels(60, 80, 110, 130, 160, 180, 210, 230)
            self.answers.SetLabel("Dans les réseaux de distribution d'eau actuels, les valves jouent un rôle critique : elles permettent de réguler")
            self.answers2.SetLabel("la circulation de l'eau, en particulier en cas d'avaries dans le réseau.")
            self.answers3.SetLabel("Mais lors de la construction d'un de ces réseaux, plusieurs questions se posent : combien de valves placer ?")
            self.answers4.SetLabel("Où les placer ? Y a-t-il des meilleurs choix ? Et selon quels critères ?")
            self.answers5.SetLabel("Plus le réseau est grand, plus il y a de possibilités et plus ces questions sont cruciales.") 
            self.answers6.SetLabel("Placer efficacement ces valves permet de grandement améliorer la fiabilité d'un système de distribution d'eau,")
            self.answers7.SetLabel("Le but de ce projet est donc de créer un programme qui proposera des solutions de placements qui s'approcheront")    
            self.answers8.SetLabel("de la solution optimale pour les critères recherchés.")
        if self.comboBox.GetValue()=='Quels sont les algorithmes utilisés et quelles sont les différences?':
            self.posLabels(60, 90, 110, 130, 150, 180, 200, 220)
            self.answers.SetLabel("Les algorithmes utilisés sont l'Algorithme de recuit Simulé et l'Algorithme Genetique.")
            self.answers2.SetLabel("L'algorithme de recuit simulé provoque une légère modification aléatoire d'une solution proposée, suivie de la")
            self.answers3.SetLabel("comparaison de cette nouvelle solution avec l'ancienne. Si cette solution est meilleure, on l'accepte,")
            self.answers4.SetLabel("sinon il y a une chance pour qu'on l'accepte quand même afin d'explorer les solutions dérivées de celle-ci qui")
            self.answers5.SetLabel("seraient peut-être meilleures que la solution de départ.")
            self.answers6.SetLabel("L'algorithme génétique trouve la solution en imitant le méchanisme de l'évolution. Pour cela, une structure de donnée")
            self.answers7.SetLabel(" 'chromosome-like' est utilisée pour représenter les individus d'une population. Ainsi une sélection, un croisement")
            self.answers8.SetLabel("entre eux et une mutation sont opérés sur la population pour avoir un résultat.")
        if self.comboBox.GetValue()=='Quels sont les critères appliqués aux algorithmes?':
            self.posLabels(60, 90, 120, 140, 170, 190, 210, 230)     
            self.answers.SetLabel("Il existe plusieurs critères de sélection pour calculer l'efficacité de ces solutions.")
            self.answers2.SetLabel("La plus simple est le nombre de valves, que l'on cherchera à diminuer afin de limiter les coûts pour les placements.")
            self.answers3.SetLabel("Un autre critère est le nombre moyen de valves nécessaire pour isoler un segment.")
            self.answers4.SetLabel("En effet, les valves n'ont pas toutes 100% de chances de fonctionner lorsque l'on demande leur fermeture.")
            self.answers5.SetLabel("Enfin, le dernier critère est le nombre moyen de segments isolés involontairement du reste du réseau après")
            self.answers6.SetLabel("l'isolement dans les segments où une avarie est survenue.")
            self.answers7.SetLabel("Puisque même en cas d'avarie, il est important de permettre la distribution d'eau à un maximum de clients.")
            self.answers8.SetLabel("")
        if self.comboBox.GetValue()=='Quelles sources a-t-on utilisé pour la réalisation du projet?':
            self.posLabels(60, 90, 120, 150, 180, 210, 240, 270)
            self.answers.SetLabel('Voici quelques références qui nous ont aidé pour la réalisation du projet:')
            self.answers2.SetLabel("Hwandon Jun. Strategic valve locations in a water distribution system. PhD thesis, State University of Virginia, 2005.")
            self.answers3.SetLabel("Dimitris Bertsimas and John Tsitsiklis. Simulated annealing. Statistical Science, 1993.")
            self.answers4.SetLabel("S. Kirkpatrick, C. D. Gelatt, Jr., and M. P. Vecchii. Optimization by simulated annealing. Science, 1983.")
            self.answers5.SetLabel("Thomas Weise. Global Optimization Algorithms - Theory and Application. Self-Published, 2009.")
            self.answers6.SetLabel("Darrell Whitley. A genetic algorithm tutorial. Technical report, Computer Science Departement, 1994.")
            self.answers7.SetLabel("Balram Suman. Study of SA based algorithms for multiobjective optimization of a constrained problem, 2004.")
            self.answers8.SetLabel("Franco Busetti. Simulated annealing overview.")
        if self.comboBox.GetValue()=='Quelles sites devrais-je visiter pour en apprendre davantage?':
            self.posLabels(60, 90, 110, 130, 150, 170, 190, 210)
            self.answers.SetLabel('Si vous voulez apprendre davantage sur ce sujet, vous pouvez visiter les sites suivants:')
    
    def on_button_click_exit(self,event):
        self.Destroy()
        self.Close(True)


    def clearLabels(self):
        self.answers.SetLabel('')
        self.answers2.SetLabel('')
        self.answers3.SetLabel('')
        self.answers4.SetLabel('')
        self.answers5.SetLabel('')
        self.answers6.SetLabel('')
        self.answers7.SetLabel('')
        self.answers8.SetLabel('')
        
    def posLabels(self, a, b, c, d, e, f, g, h):
        self.answers.SetPosition((5, a))
        self.answers2.SetPosition((5, b))
        self.answers3.SetPosition((5, c))
        self.answers4.SetPosition((5, d))
        self.answers5.SetPosition((5, e))
        self.answers6.SetPosition((5, f))
        self.answers7.SetPosition((5, g))
        self.answers8.SetPosition((5, h))    
    
class GuiGraph(wx.Frame):
    
    def __init__(self):
        self.network = GlobalNetwork("randomNetwork", '../../input/randomNetwork.dot')       
        self.updateVar()
                
        wx.Frame.__init__(self, wx.GetApp().TopWindow, size=(500, 550), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.initialize()
        self.Center()
        self.SetTitle('Sélection du graphe')
        self.panel = wx.Panel(self, size=(500, 500))
        
        self.createMadeGraph5()
        self.type="Hwandon"

        
        self.panel.Bind(wx.EVT_PAINT, self.draw_graph)

        self.Fit()

    def initialize(self):
        button_random = wx.Button(self, -1, label='Créer graphe', pos = (102, 500), size=(80, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_createGraph, button_random)

        button_next = wx.Button(self, -1, label='Suivant', pos = (398, 500), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_next, button_next)
 
 
        self.info = wx.StaticText(self,-1,label='Veuillez choisir un réseau hydraulique', pos=(198, 505))        
        
        complexity = ['Très Simple', 'Simple', 'Moyen', 'Complexe', 'Aléatoire (Moyen)', 'Aléatoire']
        self.comboBox = wx.ComboBox(self, pos=(2, 502), size =(100, 500), choices=complexity, style=wx.CB_READONLY, value = 'Aléatoire')
        
        self.Show(True)

    def on_button_click_next(self,event):
        algo = GuiAlgorithmChoice(self.x, self.y)
        algo.Show()
        self.Close(True)

    def create_random(self):
        nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        pipes = ['-', '-']
        nbrLines = random.randint(3, 6)
        network = ""
        for i in range(nbrLines):
            nbrNodes = random.randint(2, 6)
            random.shuffle(nodes)
            for i in range(nbrNodes):
                network = network + nodes[i] + " " + pipes[random.randint(0, 1)] + pipes[random.randint(0, 1)] + " "
            network = network + nodes[nbrNodes] + ";\n"
        try:
            f = open("../../input/randomNetwork.dot", "w")
            try:                
                f.writelines(network) # Write a sequence of strings to a file
            finally:
                f.close()
        except IOError:
            pass
        self.type="Random"
        self.updateGraph()
    
    def on_button_click_createGraph(self, event):
        if self.comboBox.GetValue() == 'Aléatoire':
            self.create_random()
        elif self.comboBox.GetValue() == 'Aléatoire (Simple)':
            self.createCustomGraph(2)
        elif self.comboBox.GetValue() == 'Aléatoire (Moyen)':
            self.createCustomGraph(4)
        elif self.comboBox.GetValue() == 'Très Simple':
            self.createMadeGraph1()   
        elif self.comboBox.GetValue() == 'Simple':
            self.createMadeGraph3()
        elif self.comboBox.GetValue() == 'Moyen':
            self.createMadeGraph5()
        elif self.comboBox.GetValue() == 'Complexe':
            self.createMadeGraph6()
  
    def createMadeGraph1(self):
        try:
            f = open("../../input/randomNetwork.dot", "w") 
            try:                
                f.writelines('A -- B -- C;\n')
                f.writelines('D -- E -- F;\n')
                f.writelines('G -- H -- I;\n')
                f.writelines('A -- D -- G;\n')
                f.writelines('B -- E -- H;\n')
                f.writelines('C -- F -- I;\n')
                f.writelines('A -- E -- I;\n')
                f.writelines('C -- E -- G;\n')
            finally:
                    f.close()
        except IOError:
            pass

        self.type="Custom"
        self.updateGraph()

    def createMadeGraph2(self):
        try:
            f = open("../../input/randomNetwork.dot", "w") 
            try:                
                f.writelines('A -- B -- E;\n')
                f.writelines('D -- A -- G;\n')
                f.writelines('G -- H -- C;\n')
                f.writelines('A -- D -- C;\n')
                f.writelines('C -- A -- B;\n')
                f.writelines('C -- F -- I;\n')
                f.writelines('A -- G -- I;\n')
                f.writelines('C -- I -- G;\n')
                f.writelines('E -- H -- I;\n')
            finally:
                    f.close()
        except IOError:
            pass

        self.type="Custom"
        self.updateGraph()
        
    def createMadeGraph3(self):
        try:
            f = open("../../input/randomNetwork.dot", "w") 
            try:                
                f.writelines('A -- E -- H;\n')
                f.writelines('D -- E -- F;\n')
                f.writelines('G -- E -- B;\n')
                f.writelines('I -- F -- B;\n')
                f.writelines('B -- D;\n')
                f.writelines('H -- E -- C;\n')
                f.writelines('H -- G -- C;\n')
            finally:
                    f.close()
        except IOError:
            pass

        self.type="Custom"
        self.updateGraph()
        
    def createMadeGraph4(self):
        try:
            f = open("../../input/randomNetwork.dot", "w") 
            try:                
                f.writelines('A -- B -- I;\n')
                f.writelines('B -- G -- D;\n')
                f.writelines('G -- H -- I;\n')
                f.writelines('A -- D -- F;\n')
                f.writelines('B -- E -- G;\n')
                f.writelines('C -- F -- H;\n')
                f.writelines('A -- E -- I;\n')
            finally:
                    f.close()
        except IOError:
            pass

        self.type="Custom"
        self.updateGraph()
   
    def createMadeGraph5(self):
        try:
            f = open("../../input/randomNetwork.dot", "w") 
            try:                
                f.writelines('A -- B -- D -- E -- G -- I -- H -- C;\n')
                f.writelines('B -- C -- F -- H;\n')
                f.writelines('D -- F -- I;\n')
                f.writelines('F -- M -- O -- G -- J -- K;\n')
                f.writelines('M -- N -- O;\n')
                f.writelines('C -- F -- I;\n')
                f.writelines('J -- L;\n')
            finally:
                    f.close()
        except IOError:
            pass

        self.type="Hwandon"
        self.updateGraph()

    def createMadeGraph6(self):
        try:
            f = open("../../input/randomNetwork.dot", "w") 
            try:                
                f.writelines('A -- B -- C -- D;\n')
                f.writelines('E -- F -- B;\n')
                f.writelines('A -- E -- I -- M -- K -- O -- N;\n')
                f.writelines('C -- G -- K -- P -- L -- K;\n')
                f.writelines('L -- H -- G -- L;\n')
                f.writelines('C -- D -- G -- C;\n')
                f.writelines('I -- J -- G;\n')
            finally:
                    f.close()
        except IOError:
            pass

        self.type="Minigame"
        self.updateGraph()
   
    def createCustomGraph(self, nbrNodes):
        nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        pipes = ['-', '-']
        nbrLines = nbrNodes
        network = ""
        for i in range(nbrLines):
            nbrNodes = random.randint(2, nbrNodes+1)
            random.shuffle(nodes)
            for i in range(nbrNodes):
                network = network + nodes[i] + " " + pipes[random.randint(0, 1)] + pipes[random.randint(0, 1)] + " "
            network = network + nodes[nbrNodes] + ";\n"
        try:
            f = open("../../input/randomNetwork.dot", "w")
            try:                
                f.writelines(network) # Write a sequence of strings to a file
            finally:
                f.close()
        except IOError:
            pass
        self.type="Random"
        self.updateGraph()

        
        
    def updateGraph(self):        
        self.network = GlobalNetwork("randomNetwork", '../../input/randomNetwork.dot')
        self.updateVar()
        self.panel.Refresh()
    
    def updateVar(self):
        self.nodes = self.network.network.nodeMap.values()
        self.pipes = self.network.network.pipeMap.values()                
    
    def draw_graph(self, event):
        #LINES = PIPES, CIRCLE = NODES, RECTANGLE = VALVES
        dc = wx.PaintDC(self.panel)

        r=5
        dc.SetPen(wx.Pen('red', 1))
        dc.SetBrush(wx.Brush('yellow'))
        
        x_positions= dict()
        y_positions= dict()
            
        dc.DrawText("Les noeuds : cercles jaunes; Les pipes : lignes vertes", 5,  5)
                
        if self.type=="Random":
            positions = [(20,450) for i in range(len(self.nodes)*2)]
            layout = GeneticAlgorithm(positions, [self.space_count,self.cross_count])        
            for i, node in enumerate(self.nodes):
                x=layout.solution[i*2]
                y=layout.solution[i*2+1]
                x_positions[str(node)] = x
                y_positions[str(node)] = y
                if i==0:
                    dc.DrawRectangle(x-7, y-7, r+10, r+10)   
                else:
                    dc.DrawCircle(x, y, r) 
                    
                  
        elif self.type=="Hwandon":
            x=20
            y=50
            for i, node in enumerate(self.nodes):
                if node=='A':
                    x=70
                    y=50
                if node=='B':
                    x=140
                    y=50
                if node=='C':
                    x=140
                    y=250
                if node=='D':
                    x=240
                    y=50
                if node=='E':
                    x=400
                    y=50
                if node=='F':
                    x=240
                    y=250
                if node=='G':
                    x=440
                    y=250
                if node=='H':
                    x=240
                    y=450
                if node=='I':
                    x=360
                    y=450
                if node=='J':
                    x=500
                    y=250
                if node=='K':
                    x=500
                    y=50
                if node=='L':
                    x=500
                    y=450
                if node=='M':
                    x=300
                    y=250
                if node=='N':
                    x=340
                    y=200
                if node=='O':
                    x=380
                    y=250
                    
                if node=="A":
                    x=x-50
                    x_positions[str(node)] = x
                    y_positions[str(node)] = y
                    dc.DrawRectangle(x-7, y-7, r+10, r+10)
                    x=x+180
                    
                else:
                    x=x-50
                    x_positions[str(node)] = x
                    y_positions[str(node)] = y
                    dc.DrawCircle(x, y, r) 
                    x=x+180    


 
        elif self.type=="Minigame":
            x=20
            y=50
            for i, node in enumerate(self.nodes):
                if node=='A':
                    x=120
                    y=150
                if node=='B':
                    x=220
                    y=150
                if node=='C':
                    x=320
                    y=150
                if node=='D':
                    x=420
                    y=150
                if node=='E':
                    x=120
                    y=250
                if node=='F':
                    x=220
                    y=250
                if node=='G':
                    x=320
                    y=250
                if node=='H':
                    x=420
                    y=250
                if node=='I':
                    x=120
                    y=350
                if node=='J':
                    x=220
                    y=350
                if node=='K':
                    x=320
                    y=350
                if node=='L':
                    x=420
                    y=350
                if node=='M':
                    x=120
                    y=450
                if node=='N':
                    x=220
                    y=450
                if node=='O':
                    x=320
                    y=450
                if node=='P':
                    x=420
                    y=450

                if node=="A":
                    x=x-40
                    y=y-80
                    x_positions[str(node)] = x
                    y_positions[str(node)] = y
                    dc.DrawRectangle(x-7, y-7, r+10, r+10)
                    x=x+180
                    
                else:                
                    x=x-40
                    y=y-80
                    x_positions[str(node)] = x
                    y_positions[str(node)] = y
                    dc.DrawCircle(x, y, r)      
                    x=x+180    

        else:    
            x=20
            y=50
            for i, node in enumerate(self.nodes):
                if i==3 or i==6:
                    y=y+180
                    x=20
                x_positions[str(node)] = x
                y_positions[str(node)] = y

                if i==0:                    
                    dc.DrawRectangle(x-7, y-7, r+10, r+10)   
                else:
                    dc.DrawCircle(x, y, r)      
                x=x+180    

        for pipe in self.pipes:
            nodeA = pipe.id[0]
            nodeB = pipe.id[1]
            dc.SetPen(wx.Pen('green', 1))
            dc.SetBrush(wx.Brush('blue'))
            dc.DrawLine(x_positions[nodeA], y_positions[nodeA], x_positions[nodeB], y_positions[nodeB])

        for node in self.nodes:
            text = node.id
            dc.DrawText(text, x_positions[node],  y_positions[node])
        
        self.x = x_positions
        self.y = y_positions
                
    def cross_count(self, posNodes):
        nodesPos = dict ([(self.nodes[i].id,(posNodes[i*2], posNodes[i*2+1])) for i in range(len(self.nodes))])
        total=0
        for i in range(len(self.pipes)):
            for j in range(i+1, len(self.pipes)):
                (x1,y1),(x2,y2)=nodesPos[self.pipes[i].id[0]],nodesPos[self.pipes[i].id[1]]
                (x3,y3),(x4,y4)=nodesPos[self.pipes[j].id[0]],nodesPos[self.pipes[j].id[1]]
                
                #den sera égal à zéros uniquement si les droites sont parallèles car même proportions
                den=((y4-y3)*(x2-x1))-((x4-x3)*(y2-y1))
                
                if den==0: continue
                
                #D'accord elle ne sont pas parallèles mais il faut tester si elles se croisent.
                #On regarde donc sur quelle portion elles se croisent, si hors portion, elles ne sont pas parallèles,
                #mais ne se croisent pas. 
                ua=((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/float(den)
                ub=((x2-x1)*(y1-y3)-(y2-y1)*(x1-x3))/float(den)
                if ua>0 and ua<1 and ub>0 and ub<1:
                    total+=1
        return total
    
    def space_count(self, posNodes):
        nodesPos = [(posNodes[i*2], posNodes[i*2+1]) for i in range(len(self.nodes[::2]))]
        total=0
        for i in range(len(nodesPos)):
            for j in range(i+1, len(nodesPos)):
                (x1,y1)=nodesPos[i]
                (x2,y2)=nodesPos[j]
                den = abs(x1-x2)+abs(y1-y2)
                if den < 25:
                    total+=1
        return total

class GuiAlgorithmChoice(wx.Frame):

    def __init__(self, x, y):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, size=(442, 280), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.x=x
        self.y=y
        self.Center()
        self.SetTitle("Paramètres de l'algorithme")
        self.initialize()
        self.Show(True)

    def initialize(self):
        self.label = wx.StaticText(self,-1,label='Choisissez un algorithme à appliquer sur le graphe:', pos=(5, 10))
        self.cb_chooseSim = wx.CheckBox(self, -1, "Exécuter l'algorithme de recuit simulé", pos=(30, 30))
        self.cb_chooseGen = wx.CheckBox(self, -1, "Exécuter l'algorithme génétique", pos=(30, 50))
        
        self.label = wx.StaticText(self,-1,label="Ensuite, sélectionnez selon quel critère l'algorithme sera exécuté:", pos=(5, 70))
        self.cb_chooseCriteria_safe = wx.CheckBox(self, -1, 'Selon la taille moyenne de chaque segment', pos=(30, 130))
        self.cb_chooseCriteria_cost = wx.CheckBox(self, -1, "Selon la moyenne de différence de taille entre chaque segment", pos=(30, 90))        
        self.cb_chooseCriteria_distance = wx.CheckBox(self, -1, 'Selon le nombre moyen de vannes requis pour isoler un segment', pos=(30, 110))
        self.cb_chooseCriteria_isolation = wx.CheckBox(self, -1, "Selon le nombre moyen d'isolements involontaires", pos=(30, 150))
  
  
        self.label = wx.StaticText(self,-1,label="Compléxite de l'algorithme de recuit simulé (température):", pos=(5, 175))        
        self.inputNumberSimulatedAnnealing = wx.SpinCtrl(self, value='10000', pos=(290, 172), size=(60, -1), min=1, max=100000)

        self.label = wx.StaticText(self,-1,label="Compléxite de l'algorithme génétique (itérations max):", pos=(5, 200))        
        self.inputNumberGenetic = wx.SpinCtrl(self, value='30', pos=(270, 197), size=(60, -1), min=1, max=5000)


  
        button_next = wx.Button(self,-1,label="Suivant", pos = (330, 220), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.OnClick_button_Next, button_next)

        self.failVerify = wx.StaticText(self, -1, '', (5, 230))  

        self.Show(True)

    def OnClick_button_Next(self,event):
        if self.verifyInput() == True:
            self.failVerify.SetLabel("L'algorithme est entraîn de calculer, veuillez attendre...")
            self.failVerify.SetForegroundColour((78,50,255))                    
            self.failVerify.Update()
            self.network = GlobalNetwork("randomNetwork", '../../input/randomNetwork.dot')

            fitnessFunct = [self.network.nbr_valves]
            
            if self.cb_chooseCriteria_safe.GetValue()==True:  
                fitnessFunct.append(self.network.average_segment_size)    
            
            if self.cb_chooseCriteria_cost.GetValue()==True:
                fitnessFunct.append(self.network.standard_deviation_segment_size)
                    
            if self.cb_chooseCriteria_distance.GetValue()==True:  
                fitnessFunct.append(self.network.average_valves_per_segment)
                
            if self.cb_chooseCriteria_isolation.GetValue()==True:
                fitnessFunct.append(self.network.average_unintended_isolation)
            
            if self.cb_chooseGen.GetValue()==True:
                miter = self.inputNumberGenetic.GetValue()
                solGen = GuiShowSolution(self.x, self.y, "L'algorithme génétique", fitnessFunct, miter)
                solGen.Show()

            if self.cb_chooseSim.GetValue()==True:
                mtemperature = self.inputNumberSimulatedAnnealing.GetValue()
                solSim = GuiShowSolution(self.x, self.y, "L'algorithme de recuit simulé", fitnessFunct, mtemperature)
                solSim.Show()

            self.Close(True)            
        else:
            self.failVerify.SetLabel('Données erronées ou incomplètes dans un ou plusieurs champs.')
            self.failVerify.SetForegroundColour((255,0,0))

    def verifyInput(self):
        verify = True
        if self.cb_chooseSim.GetValue()==False and self.cb_chooseGen.GetValue()==False:
            verify=False 
        #elif self.cb_chooseCriteria_isolation.GetValue()==False and self.cb_chooseCriteria_cost.GetValue()==False and self.cb_chooseCriteria_distance.GetValue()==False and self.cb_chooseCriteria_safe.GetValue()==False:
            #verify=False                  
        return verify

class GuiShowSolution(wx.Frame):

    def __init__(self, x, y, algotitle, fitnessFunct, complexity):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, size=(500, 550), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.x=x
        self.y=y
        self.Center()
        self.algo="gen"
        if algotitle == "L'algorithme de recuit simulé":
            self.algo="sim"
        self.SetTitle("Le graphe de solution : " + algotitle)
        self.network=GlobalNetwork("randomNetwork", '../../input/randomNetwork.dot')
        self.iterationCount=0
        self.updateVar()    
        self.Show(True)
        self.panel = wx.Panel(self, size=(500, 500))
        self.panel.Bind(wx.EVT_PAINT, self.draw_graph)
        self.initialize()
        self.runAlgorithm(fitnessFunct, complexity)
        self.Fit()

    def runAlgorithm(self, fitnessFunct, complexity):
        pattern = [(0,1) for i in range(self.network.network.nbrPipes*2)]
        if self.algo=="gen":
            solution = GeneticAlgorithm(pattern, fitnessFunct, showInfo = self.updateValves, nbrOfGenerations = complexity)
        else:
            solution = SimulatedAnnealing(pattern, fitnessFunct, showInfo = self.updateValves, temperature=complexity)

        self.network.update(solution.solution)
        self.updateVar()
        self.iterationCount=0
        self.panel.Refresh()
        self.showSolutionScores()

    def initialize(self):
        self.label = wx.StaticText(self,-1,label='', pos=(0, 0))
        button_next = wx.Button(self, -1, label='Suivant', pos = (398, 525), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_next, button_next)
        button_prec = wx.Button(self, -1, label='Précédent', pos = (398, 500), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_prec, button_prec)
        self.showScores();
        self.Show(True)

    def showSolutionScores(self):
        self.label2 = wx.StaticText(self,-1,label="Nombre moyen de segments : " + str(round(self.network.average_segment_size(), 3)), pos=(0, 500))
        self.label3 = wx.StaticText(self,-1,label="Taille de la déviation de segments : " + str(round(self.network.standard_deviation_segment_size(), 3)), pos=(0, 515))
        self.label4 = wx.StaticText(self,-1,label="Nombre moyen de vannes par segment : " + str(round(self.network.average_valves_per_segment(), 3)), pos=(0, 530))
        self.label5 = wx.StaticText(self,-1,label="Nombre de valves : " + str(self.network.nbr_valves()) + " ; Coût (pour le prix d'une vanne de 500€) : " + str(self.network.nbr_valves()*500) + "€", pos=(0, 545))
        #self.label8 = wx.StaticText(self,-1,label="Nombre moyen d'isolements involontaires" + str(round(self.network.average_unintended_isolation)), pos=(0, 545))
        self.label7 = wx.StaticText(self,-1,label="___________________________________________________________________________________", pos=(0, 557))
        self.label6 = wx.StaticText(self,-1,label="Paramètres de l'algorithme:", pos=(0, 575))
        self.label6.SetForegroundColour((255,0,0))                

    def showCriteria(self):
        self.labelRed = wx.StaticText(self,-1,label="Critère d'exécution:", pos=(250, 575))
        self.labelRed.SetForegroundColour((255,0,0))                        
        self.cb_chooseCriteria_cost = wx.CheckBox(self, -1, 'Moyenne de la taille de chaque segment', pos=(250, 590))
        self.cb_chooseCriteria_distance = wx.CheckBox(self, -1, "Différence de taille entre chaque segment", pos=(250, 605))
        self.cb_chooseCriteria_safe = wx.CheckBox(self, -1, 'Nbre moyen de vannes pour isoler un segment', pos=(250, 620))
        self.cb_chooseCriteria_isolation = wx.CheckBox(self, -1, "Nombre moyen d'isolements involontaires", pos=(250, 635))

    def showScores(self):
        self.showSolutionScores()
        self.showCriteria()
        if self.algo=="sim":
            self.initSim()
        else:
            self.initGen()


    def initSim(self):
        self.label = wx.StaticText(self,-1,label="Vitesse de refroidissement (1-1000):", pos=(0, 590))
        self.inputCoolSpeed = wx.SpinCtrl(self, value='5', pos=(178, 587), size=(60, -1), min=0, max=1000)
        
        self.label = wx.StaticText(self,-1,label="Echelle de modification (1-100):", pos=(0, 610))
        self.inputModifictionRate = wx.SpinCtrl(self, value='10', pos=(178, 607), size=(60, -1), min=0, max=100)
        
        self.label = wx.StaticText(self,-1,label="Compléxite (température):", pos=(0, 630))        
        self.inputTemperature = wx.SpinCtrl(self, value='100000', pos=(158, 627), size=(80, -1), min=1, max=9999999)
              
        button_sim = wx.Button(self, -1, label='Mettre à jour', pos = (398, 655), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_sim, button_sim)
    
    def initGen(self):
        self.label = wx.StaticText(self,-1,label="Taille de la population:", pos=(0, 590))
        self.inputPopulationSize = wx.SpinCtrl(self, value='40', pos=(150, 587), size=(60, -1), min=0, max=250)
        
        self.label = wx.StaticText(self,-1,label="Taille du tournoi:", pos=(0, 610))
        self.inputTournmanetSize = wx.SpinCtrl(self, value='2', pos=(150, 607), size=(60, -1), min=0, max=100)
        
        self.label = wx.StaticText(self,-1,label="Facteur de sélection (%):", pos=(0, 630))
        self.inputSelectionRate = wx.SpinCtrl(self, value='50', pos=(150, 627), size=(60, -1), min=0, max=100)

        self.label = wx.StaticText(self,-1,label="Probabilité de crossover (%): ", pos=(0, 650))
        self.inputCrossOverProb = wx.SpinCtrl(self, value='50', pos=(150, 647), size=(60, -1), min=0, max=100)

        self.label = wx.StaticText(self,-1,label="Probabilité de mutation (%):", pos=(0, 670))
        self.inputMutationProba = wx.SpinCtrl(self, value='1', pos=(150, 667), size=(60, -1), min=0, max=100)

        self.label = wx.StaticText(self,-1,label="Facteur d'élitisme (1-1000):", pos=(0, 690))
        self.inputElitisme = wx.SpinCtrl(self, value='125', pos=(150, 687), size=(60, -1), min=0, max=1000)


        self.label = wx.StaticText(self,-1,label="Compléxite (itérations max):", pos=(0, 710))        
        self.inputMaxIter = wx.SpinCtrl(self, value='30', pos=(150, 707), size=(60, -1), min=1, max=99999999)
        
        button_gen = wx.Button(self, -1, label='Mettre à jour', pos = (398, 710), size=(100, 25))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_gen, button_gen)

    def on_button_click_sim(self,event):
        self.labelWorking = wx.StaticText(self,-1,label="L'algorithme est entraîn de calculer..", pos=(218, 660))
        self.labelWorking.SetForegroundColour((78, 50, 255))
        self.labelWorking.Update()

        fitnessFunct = [self.network.nbr_valves]
        
        if self.cb_chooseCriteria_safe.GetValue()==True:  
            fitnessFunct.append(self.network.average_segment_size)
                
        if self.cb_chooseCriteria_cost.GetValue()==True:
            fitnessFunct.append(self.network.standard_deviation_segment_size)
        if self.cb_chooseCriteria_distance.GetValue()==True:  
            fitnessFunct.append(self.network.average_valves_per_segment)
                
        if self.cb_chooseCriteria_isolation.GetValue()==True:
            fitnessFunct.append(self.network.average_unintended_isolation)

        coolS=float(self.inputCoolSpeed.GetValue())/1000
        modif=float(self.inputModifictionRate.GetValue())/100
        
        self.network=GlobalNetwork("randomNetwork", '../../input/randomNetwork.dot')
        pattern = [(0,1) for i in range(self.network.network.nbrPipes*2)]
        #solution = SimulatedAnnealing(pattern, self.network.average_segment_size, temperature=self.inputTemperature.GetValue(), coolSpeed=self.inputCoolSpeed.GetValue(), modificationRate=self.inputModifictionRate.GetValue())
        solution = SimulatedAnnealing(pattern, fitnessFunct, showInfo = self.updateValves, temperature=self.inputTemperature.GetValue(), coolSpeed=coolS, modificationRate=modif)
        
        self.network.update(solution.solution)
        self.updateVar()
        self.iterationCount=0
        self.panel.Refresh()
        self.showSolutionScores()

        self.labelWorking.SetLabel("")
        self.labelWorking.Update()

    def on_button_click_gen(self,event):
        self.labelWorking = wx.StaticText(self,-1,label="L'algorithme est entraîn de calculer..", pos=(218, 715))
        self.labelWorking.SetForegroundColour((78, 50, 255))
        self.labelWorking.Update()
        
        fact = float(self.inputSelectionRate.GetValue())/100
        elit = float(self.inputElitisme.GetValue())/1000
        cross = float(self.inputCrossOverProb.GetValue())/100
        muta = float(self.inputMutationProba.GetValue())/100

        fitnessFunct = [self.network.nbr_valves]

        if self.cb_chooseCriteria_safe.GetValue()==True:  
            fitnessFunct.append(self.network.average_segment_size)
                
        if self.cb_chooseCriteria_cost.GetValue()==True:
            fitnessFunct.append(self.network.standard_deviation_segment_size)
                    
        if self.cb_chooseCriteria_distance.GetValue()==True:  
            fitnessFunct.append(self.network.average_valves_per_segment)
                
        if self.cb_chooseCriteria_isolation.GetValue()==True:
            fitnessFunct.append(self.network.average_unintended_isolation)

        self.network=GlobalNetwork("randomNetwork", '../../input/randomNetwork.dot')
        pattern = [(0,1) for i in range(self.network.network.nbrPipes*2)]
        solution = GeneticAlgorithm(pattern, fitnessFunct, showInfo = self.updateValves, nbrOfGenerations = self.inputMaxIter.GetValue(), populationSize=self.inputPopulationSize.GetValue(), tournamentSize=self.inputTournmanetSize.GetValue(), selectionRate=fact, elitisme=elit, crossoverProb=cross, mutationProba=muta)
        
        self.network.update(solution.solution)
        self.updateVar()
        self.iterationCount=0
        self.panel.Refresh()
        self.showSolutionScores()

        self.labelWorking.SetLabel("")
        self.labelWorking.Update()
        
    def on_button_click_next(self,event):
        algo = GuiTerminateSimulation()
        algo.Show()
        self.Close(True)

    def on_button_click_prec(self,event):
        algo = GuiAlgorithmChoice(self.x, self.y)
        algo.Show()
        self.Close(True)

    def updateVar(self):
        self.nodes = self.network.network.nodeMap.values()
        self.pipes = self.network.network.pipeMap.values()                

    def updateValves(self, valvesCode, data):
        self.data=data
        
        self.network.update(valvesCode)
        self.updateVar()
        
        self.iterationCount=self.iterationCount+1
        self.showUpdateScores(data)

        self.panel.Refresh()
        self.panel.Update()
        
    def showUpdateScores(self, data):
        if self.algo=="gen":
            self.label5.SetLabel("Nombre de valves : " + str(data[0]) + " ; Coût (pour le prix d'une vanne de 500€) : " + str(data[0]*500) + "€")
            self.label5.Update()

    def draw_graph(self, event):
        #LINES = PIPES, CIRCLE = NODES, RECTANGLE = VALVES
        dc = wx.PaintDC(self.panel)
        r=5
        dc.SetPen(wx.Pen('red', 1))
        dc.SetBrush(wx.Brush('yellow'))
        
        x_positions= self.x
        y_positions= self.y
            
        scoreTotal=0
        for score in self.data:
            scoreTotal=scoreTotal+score

        if self.iterationCount!=0:
            
            dc.DrawText("Itération " + str(self.iterationCount) + " ; Score : " + str(round(scoreTotal, 3)), 5, 5)
        else:
            dc.DrawText("Qualité globale de la solution : " + str(round(scoreTotal, 3)) , 5,  5)

        for i, node in enumerate(self.nodes):
            if i==0:
                dc.DrawRectangle(x_positions[node]-7, y_positions[node]-7, r+10, r+10)
            else:                
                dc.DrawCircle(x_positions[node], y_positions[node], r)      
            
        for pipe in self.pipes:
            nodeA = pipe.id[0]
            nodeB = pipe.id[1]
            dc.SetPen(wx.Pen('green', 1))
            dc.SetBrush(wx.Brush('blue'))
            dc.DrawLine(x_positions[nodeA], y_positions[nodeA], x_positions[nodeB], y_positions[nodeB])

            y2 = float(y_positions[nodeB])
            y1 = float(y_positions[nodeA])
            x2 = float(x_positions[nodeB])
            x1 = float(x_positions[nodeA])

            b=0
            if x1==x2:
                dist=0
                signe=1
                if y1>y2:
                    dist=y1-y2
                    signe=-1
                else:
                    dist=y2-y1

                if pipe.valveAtStart:
                    dc.SetPen(wx.Pen('blue', 1))
                    dc.SetBrush(wx.Brush('blue'))
                    rect = wx.Rect(x1, y1+(dist*0.2*signe), 6, 6)
                    dc.DrawRoundedRectangleRect(rect, 1)
                if  pipe.valveAtEnd :
                    dc.SetPen(wx.Pen('blue', 1))
                    dc.SetBrush(wx.Brush('blue'))
                    #rect = wx.Rect(x2 + (-signe*15) , a*(x2-signe*15)+b, 6, 6)
                    rect = wx.Rect(x2, y2+(dist*0.2*(-signe)), 6, 6)
                    dc.DrawRoundedRectangleRect(rect, 1)

            if x1!=x2:
                b = (y2-(y1*x2/x1))/(1-(x2/x1))
                a = (y1-b)/x1
                pixel = 15
                if abs(a)>4:
                    pixel=2
                signe = -1
                if x1<x2:
                    signe = 1
                
                if pipe.valveAtStart:
                    dc.SetPen(wx.Pen('blue', 1))
                    dc.SetBrush(wx.Brush('blue'))
                    #rect = wx.Rect(x1+(signe*15), a*(x1+signe*15)+b, 6, 6)
                    rect = wx.Rect(x1+(signe*pixel), a*(x1+signe*pixel)+b, 6, 6)
                    dc.DrawRoundedRectangleRect(rect, 1)
                if  pipe.valveAtEnd :
                    dc.SetPen(wx.Pen('blue', 1))
                    dc.SetBrush(wx.Brush('blue'))
                    #rect = wx.Rect(x2 + (-signe*15) , a*(x2-signe*15)+b, 6, 6)
                    rect = wx.Rect(x2 + (-signe*pixel) , a*(x2-signe*pixel)+b, 6, 6)
                    dc.DrawRoundedRectangleRect(rect, 1)

        for node in self.nodes:
            text = node.id
            dc.DrawText(text, x_positions[node],  y_positions[node])

class GuiTerminateSimulation(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, size=(574, 511), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.Center()
        self.SetTitle('Fin de la simulation')
        self.initialize()
        self.Show(True)

    def initialize(self):
        imageFile = "../../images/endsim.png"
        png = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (0, 0), (png.GetWidth(), png.GetHeight()))

        
        self.label1 = wx.StaticText(self,-1,label='La simulation est terminée.', pos=(5, 0))
        self.label2 = wx.StaticText(self,-1,label="N'hésitez pas à nous faire parvenir toute question ou remarque, pour que nous puissions vous répondre...", pos=(5, 20))
        self.label3 = wx.StaticText(self,-1,label='Vous pouvez également visiter la documentation du menu principal pour les questions fréquemment posées.', pos=(5, 40))

        button_exit = wx.Button(self,-1,label="Fin de la simulation", pos=(0, 431), size=(572, 50))
        self.Bind(wx.EVT_BUTTON, self.on_button_click_exit, button_exit)
        self.Show(True)

    def on_button_click_exit(self,event):
        self.Destroy()
        self.Close(True)

if __name__ == "__main__":
    app = App(False)
    app.MainLoop()