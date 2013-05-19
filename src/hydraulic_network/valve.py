# -*-coding:Utf-8 -*

class Valve(object):
    
    def __init__(self, inId, inStartingSeg):
        super(Valve, self).__init__()
        
        self.id = inId
        self.startingSegment = inStartingSeg
        self.endingSegment = None
         
    def __str__(self): #imprime l'id de la valve, ainsi que l'ID des deux segments qu'elle délimite
        if(self.endingSegment!= None):
            return self.id+ ": " + self.startingSegment.id +" - "+ self.endingSegment.id
        else:
            return self.id+ ": " + self.startingSegment.id +" - None"