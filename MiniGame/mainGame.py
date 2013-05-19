#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class MainFrame(wx.Frame):
    
    
    LEVEL_1 = 1
    LEVEL_1_PIPES = [[0, 0, 1, 0],
                     [1, 0, 2, 0],
                     [2, 0, 3, 0],
                     [0, 0, 0, 1],
                     [1, 0, 1, 1],
                     [2, 0, 2, 1],
                     [3, 0, 2, 1],
                     [0, 1, 1, 1],
                     [2, 1, 3, 1],
                     [0, 1, 0, 2],
                     [2, 1, 1, 2],
                     [2, 1, 3, 2],
                     [3, 1, 3, 2],
                     [0, 2, 1, 2],
                     [0, 2, 0, 3],
                     [2, 2, 3, 2],
                     [0, 3, 2, 2],
                     [2, 2, 2, 3],
                     [2, 2, 3, 3],
                     [1, 3, 2, 3],
                     [2, 1, 2, 2],
                     [3, 2, 3, 3]]
    LEVEL_1_BROKEN_PIPE = [2, 1, 2, 2]
    LEVEL_1_ISOLATED_PIPES = []
    LEVEL_1_VALVES_LOC=  [[1, 0, 1, 0],
                          [3, 0, -1, 0],
                          [0, 1, 1, 0],
                          [2, 1, 0, 1],
                          [3, 1, 0, 1],
                          [1, 2, 1, -1],
                          [2, 2, 0, -1],
                          [2, 2, 1, 1],
                          [0, 3, 0, -1],
                          [2, 3, 0, -1]]
    LEVEL_1_VALVES_TO_CLOSE = [4, 7]
    
    LEVEL_2 = 2
    LEVEL_2_PIPES = LEVEL_1_PIPES
    LEVEL_2_BROKEN_PIPE = LEVEL_1_BROKEN_PIPE
    LEVEL_2_ISOLATED_PIPES = [[2, 1, 3, 1],
                              [2, 1, 3, 2],
                              [2, 2, 2, 3],
                              [3, 2, 3, 3],
                              [2, 2, 3, 3],
                              [2, 2, 3, 2],
                              [1, 3, 2, 3],
                              [3, 1, 3, 2]]
    LEVEL_2_VALVES_LOC = [[1, 0, 1, 0],
                          [3, 0, -1, 0],
                          [0, 1, 1, 0],
                          [3, 1, 0, 1],
                          [1, 2, 1, -1],
                          [2, 2, 1, 0],
                          [2, 2, 1, 1],
                          [0, 3, 0, -1],
                          [2, 3, 0, -1],
                          [2, 1, 0, -1],
                          [2, 1, 1, -1],
                          [2, 1, 1, 0],
                          [2, 1, 1, 1],
                          [2, 1, -1, 1],
                          [2, 2, 0, 1],
                          [2, 2, -2, 1]
                          ]
    LEVEL_2_VALVES_TO_CLOSE = [6, 7, 10, 11, 12, 13, 14, 15, 16]
    
    LEVEL_3 = 3
    LEVEL_3_PIPES = LEVEL_1_PIPES
    LEVEL_3_BROKEN_PIPE = LEVEL_1_BROKEN_PIPE
    LEVEL_3_ISOLATED_PIPES = [[1, 3, 2, 3],
                              [2, 2, 2, 3],
                              [1, 3, 2, 3],
                              [0, 3, 2, 2]]
    LEVEL_3_VALVES_LOC = [[1, 0, 1, 0],
                          [3, 0, -1, 0],
                          [0, 1, 1, 0],
                          [2, 1, 0, 1],
                          [3, 1, 0, 1],
                          [1, 2, 1, -1],
                          [2, 2, 1, 0],
                          [2, 2, 1, 1],
                          [0, 3, 0, -1],
                          [2, 3, 0, -1]]
    LEVEL_3_VALVES_TO_CLOSE = [4, 7, 8, 9, 10]
    
    LEVEL_4 = 4
    LEVEL_4_PIPES = LEVEL_1_PIPES
    LEVEL_4_BROKEN_PIPE = LEVEL_1_BROKEN_PIPE
    LEVEL_4_ISOLATED_PIPES = [[2, 0, 2, 1],
                              [3, 0, 2, 1],
                              [2, 1, 3, 1],
                              [2, 1, 3, 2],
                              [3, 1, 3, 2],
                              [2, 2, 3, 2],
                              [2, 2, 3, 3],
                              [3, 2, 3, 3],
                              [1, 3, 2, 3],
                              [2, 2, 2, 3],
                              [1, 3, 2, 3],
                              [0, 3, 2, 2],
                              [2, 1, 1, 2]]
    LEVEL_4_VALVES_LOC = [[1, 0, 1, 0],
                          [3, 0, -1, 0],
                          [0, 1, 1, 0],
                          [2, 0, 0, 1],
                          [3, 1, 0, 1],
                          [1, 2, 1, -1],
                          [2, 2, 1, 0],
                          [2, 2, 1, 1],
                          [0, 3, 0, -1],
                          [2, 3, 0, -1],
                          [3, 2, -1, -1]]
    LEVEL_4_VALVES_TO_CLOSE = [2, 4, 5, 6, 7, 8, 9, 10, 11]
    
    LEVEL_5 = 5
    LEVEL_5_PIPES = LEVEL_1_PIPES
    LEVEL_5_BROKEN_PIPE = [0, 3, 2, 2]
    LEVEL_5_ISOLATED_PIPES = [[0, 2, 0, 3],
                              [0, 1, 0, 2],
                              [2, 1, 3, 2],
                              [2, 1, 2, 2],
                              [3, 1, 3, 2],
                              [2, 2, 3, 2],
                              [2, 2, 3, 3],
                              [2, 2, 2, 3],
                              [1, 3, 2, 3],
                              [3, 2, 3, 3]]
    LEVEL_5_VALVES_LOC = [[0, 0, 1, 0],
                          [2, 0, -1, 0],
                          [2, 0, 0, 1],
                          [2, 0, 1, 0],
                          [3, 0, -1, 1],
                          [1, 1, 0, -1],
                          [0, 1, 0, 1],
                          [2, 1, 0, 1],
                          [2, 1, 1, 1],
                          [3, 1, 0, 1],
                          [0, 2, 1, 0],
                          [1, 2, -1, 0],
                          [1, 2, 1, -1],
                          [2, 2, 0, 1],
                          [3, 2, 0, 1],
                          [1, 3, 1, 0],
                          [3, 3, -1, -1]]
    LEVEL_5_VALVES_TO_CLOSE = [7, 8, 9, 10, 11, 14, 15, 17]
    
    
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, 
            size=(600, 750), style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        
        self.initUI()
        self.Centre()
        self.Show(True)
        self.level = None
        self.levelNbr = 0
    
    def initUI(self):
        
        menubar = wx.MenuBar()
        playMenu = wx.Menu()
        levelItem1 = wx.MenuItem(playMenu, self.LEVEL_1, 'Niveau 1')
        levelItem2 = wx.MenuItem(playMenu, self.LEVEL_2, 'Niveau 2')
        levelItem3 = wx.MenuItem(playMenu, self.LEVEL_3, 'Niveau 3')
        levelItem4 = wx.MenuItem(playMenu, self.LEVEL_4, 'Niveau 4')
        levelItem5 = wx.MenuItem(playMenu, self.LEVEL_5, 'Niveau 5')
        playMenu.AppendItem(levelItem1)
        playMenu.AppendItem(levelItem2)
        playMenu.AppendItem(levelItem3)
        playMenu.AppendItem(levelItem4)
        playMenu.AppendItem(levelItem5)
        self.Bind(wx.EVT_MENU, self.showLevel1, levelItem1)
        self.Bind(wx.EVT_MENU, self.showLevel2, levelItem2)
        self.Bind(wx.EVT_MENU, self.showLevel3, levelItem3)
        self.Bind(wx.EVT_MENU, self.showLevel4, levelItem4)
        self.Bind(wx.EVT_MENU, self.showLevel5, levelItem5)
        menubar.Append(playMenu, 'Jouer')
        self.SetMenuBar(menubar)
        
    def showLevel1(self, e):
        
        if(self.level != None):
            self.level.stopGame()
            self.level.Destroy()
        self.levelNbr = 1
        self.level = Level(self, self.LEVEL_1_PIPES, self.LEVEL_1_BROKEN_PIPE, self.LEVEL_1_ISOLATED_PIPES, self.LEVEL_1_VALVES_LOC, self.LEVEL_1_VALVES_TO_CLOSE)
        self.level.SetFocus()
        self.level.Show(True)
        self.SendSizeEvent()
        
    def showLevel2(self, e):
        
        if(self.level != None):
            self.level.stopGame()
            self.level.Destroy()
        self.levelNbr = 2
        self.level = Level(self, self.LEVEL_2_PIPES, self.LEVEL_2_BROKEN_PIPE, self.LEVEL_2_ISOLATED_PIPES, self.LEVEL_2_VALVES_LOC, self.LEVEL_2_VALVES_TO_CLOSE)
        self.level.SetFocus()
        self.level.Show(True)
        self.SendSizeEvent()
        
    def showLevel3(self, e):
        
        if(self.level != None):
            self.level.stopGame()
            self.level.Destroy()
        self.levelNbr = 3
        self.level = Level(self, self.LEVEL_3_PIPES, self.LEVEL_3_BROKEN_PIPE, self.LEVEL_3_ISOLATED_PIPES, self.LEVEL_3_VALVES_LOC, self.LEVEL_3_VALVES_TO_CLOSE)
        self.level.SetFocus()
        self.level.Show(True)
        self.SendSizeEvent()
        
    def showLevel4(self, e):
        
        if(self.level != None):
            self.level.stopGame()
            self.level.Destroy()
        self.levelNbr = 4
        self.level = Level(self, self.LEVEL_4_PIPES, self.LEVEL_4_BROKEN_PIPE, self.LEVEL_4_ISOLATED_PIPES, self.LEVEL_4_VALVES_LOC, self.LEVEL_4_VALVES_TO_CLOSE)
        self.level.SetFocus()
        self.level.Show(True)
        self.SendSizeEvent()
        
    def showLevel5(self, e):
        
        if(self.level != None):
            self.level.stopGame()
            self.level.Destroy()
        self.levelNbr = 5
        self.level = Level(self, self.LEVEL_5_PIPES, self.LEVEL_5_BROKEN_PIPE, self.LEVEL_5_ISOLATED_PIPES, self.LEVEL_5_VALVES_LOC, self.LEVEL_5_VALVES_TO_CLOSE)
        self.level.SetFocus()
        self.level.Show(True)
        self.SendSizeEvent()
    
    def nextLevel(self):
        
        self.levelNbr = self.levelNbr+1
        
        if self.levelNbr==2:
            self.showLevel2(None)
        elif self.levelNbr==3:
            self.showLevel3(None)
        elif self.levelNbr==4:
            self.showLevel4(None)
        elif self.levelNbr==5:
            self.showLevel5(None)
        elif self.levelNbr==6:
            self.levelNbr=1
            self.showLevel1(None)
            
    def previousLevel(self):
        
        self.levelNbr = self.levelNbr-1
        
        if self.levelNbr==1:
            self.showLevel1(None)
        elif self.levelNbr==2:
            self.showLevel2(None)
        elif self.levelNbr==3:
            self.showLevel3(None)
        elif self.levelNbr==4:
            self.showLevel4(None)
        elif self.levelNbr==0:
            self.showLevel5(None)
        
        
class Level(wx.Panel):
    
    Speed = 1000
    ID_TIMER = 1
      
    def __init__(self, parent, pipes, brokenPipe, isolatedPipes, valvesLoc, valveToClose):
        wx.Panel.__init__(self, parent)
        
        self.parent = parent
        
        self.timer = wx.Timer(self, Level.ID_TIMER)
        self.font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, 
            wx.FONTWEIGHT_BOLD, False, 'Comic Sans MS')
        
        self.gameStarted = False
        self.gameWon = False
        
        self.timerCount = 0
        self.valvesDict = dict()
        
        valveNbr = 0
        for valve in valvesLoc:
            valveNbr+=1
            self.valvesDict[valveNbr] = ValveButton(valve[0], valve[1], valve[2], valve[3])
        
    
        self.valvesToClose = valveToClose
        self.pipes = pipes
        self.brokenPipe = brokenPipe
        self.isolatedPipes = isolatedPipes

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Bind(wx.EVT_TIMER, self.OnTimer, id=Level.ID_TIMER)
        self.paintNow()
        
    def start(self):
        self.resetLevel()
        self.timer.Start(Level.Speed)
        self.gameStarted = True

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        self.render(dc)
        
    def OnMouseUp(self, event):
        pos = event.GetPosition()
        if self.gameStarted:
            for valve in self.valvesDict.values():
                if self.inRange(pos, valve):
                    valve.toggle()
            self.paintNow()
            if self.checkSolution():
                self.stopGame()
                self.gameWon = True
                self.paintNow()
                wx.MessageBox('Vous avez gagné!', 'Info', wx.OK | wx.ICON_INFORMATION)
                
        else:
            if pos.x > 50 and pos.x < 500 and pos.y > 550 and pos.y < 600:
                self.resetLevel()
                self.start()
        self.paintNow()
        
        if pos.x > 50 and pos.x < 260 and pos.y > 630 and pos.y < 680:
            self.previousLevel()
        elif pos.x > 290 and pos.x < 500 and pos.y > 630 and pos.y < 680:
            self.nextLevel()
        
    def OnTimer(self, event):
        if event.GetId() == Level.ID_TIMER:
            self.timerCount+=1;
            
            if self.timerCount == 30:
                self.stopGame()
                wx.MessageBox('Temps Ecoulé!', 'Info', wx.OK | wx.ICON_INFORMATION)
                self.resetLevel()
            self.paintNow()
        
        
    def paintNow(self):
        
        dc = wx.ClientDC(self)
        self.render(dc)
    
    def render(self, dc):
        dc.SetPen(wx.Pen('BLUE', 10, wx.SOLID))
        
        for pipe in self.pipes:
            if (self.gameStarted or self.gameWon) and pipe == self.brokenPipe:
                dc.SetPen(wx.Pen('RED', 10, wx.SOLID))
                self.drawPipe(dc, pipe[0], pipe[1], pipe[2], pipe[3])
                dc.SetPen(wx.Pen('BLUE', 10, wx.SOLID))
            elif self.gameWon and pipe in self.isolatedPipes:
                dc.SetPen(wx.Pen('GREY', 10, wx.SOLID))
                self.drawPipe(dc, pipe[0], pipe[1], pipe[2], pipe[3])
                dc.SetPen(wx.Pen('BLUE', 10, wx.SOLID))
            else:
                self.drawPipe(dc, pipe[0], pipe[1], pipe[2], pipe[3])
        
        
        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
        dc.SetBrush(wx.Brush('BLACK'))
        
        for i in range(4):
            for j in range(4):
                if (i==0 and j==0):
                    dc.SetBrush(wx.Brush('CYAN'))
                    dc.DrawRectangle(50-20, 50-20, 40, 40)
                    dc.SetBrush(wx.Brush('BLACK'))
                else:
                    dc.DrawCircle(50+i*150, 50+j*150, 20)
        
        for valve in self.valvesDict.values():
            valve.draw(dc)
            
        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
        dc.SetBrush(wx.Brush('BLACK'))
        dc.DrawRectangle(50, 550, 450, 50)
        
        if not self.gameStarted:
            dc.SetFont(self.font)
            dc.SetTextForeground('WHITE')
            if not self.gameWon:
                dc.DrawText( "Cliquez ici pour commencer", 160, 560)
            else:
                dc.DrawText( "Rejouer ce niveau?", 195, 560)
        
        dc.SetBrush(wx.Brush('BLUE'))
        dc.DrawRectangle(60, 560, 15*self.timerCount, 30)
        
        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
        dc.SetBrush(wx.Brush('BLACK'))
        dc.DrawRectangle(50, 630, 210, 50)
        dc.DrawRectangle(290, 630, 210, 50)
        
        dc.SetFont(self.font)
        dc.SetTextForeground('WHITE')
        dc.DrawText( "Niveau précédent", 80, 640)
        dc.DrawText( "Niveau suivant", 330, 640)
        
    def drawPipe(self, dc, xStart, yStart, xEnd, yEnd):
        dc.DrawLine(50+xStart*150, 50+yStart*150, 50+xEnd*150, 50+yEnd*150)
        
    
        
    def checkSolution(self):
        solutionFound = True
        for key, valve in self.valvesDict.items():
            isOpen = valve.isOpen
            if key in self.valvesToClose:
                if isOpen:
                    solutionFound = False
            elif not isOpen:
                solutionFound = False
        return solutionFound
    
    def resetLevel(self):
        for valve in self.valvesDict.values():
                valve.isOpen = True
        self.timerCount = 0
        self.gameWon = False
        
    def stopGame(self):
        self.gameStarted = False
        self.timerCount = 0
        self.timer.Stop()
        
    def nextLevel(self):
        self.stopGame()
        self.parent.nextLevel()
    
    def previousLevel(self):
        self.stopGame()
        self.parent.previousLevel()
    
    def inRange(self, pos, valve):
        return (pos.x > valve.centralX-10 and pos.x < valve.centralX+10 and pos.y > valve.centralY-10 and pos.y < valve.centralY+10)
    
class ValveButton(object):
    def __init__(self, nodeX, nodeY, dirX, dirY):
        super(ValveButton, self).__init__()
        self.nodeX = nodeX
        self.nodeY = nodeY
        self.dirX = dirX
        self.dirY = dirY
        self.centralX = 50+self.nodeX*150+self.dirX*30
        self.centralY = 50+self.nodeY*150+self.dirY*30
        self.isOpen = True
        
    def draw(self, dc):
        
        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
        if self.isOpen:
            dc.SetBrush(wx.Brush('GREEN'))
        else:
            dc.SetBrush(wx.Brush('RED'))
        
        dc.DrawCircle(self.centralX, self.centralY, 10)
        
        
    def toggle(self):
        if self.isOpen:
            self.isOpen = False
        else:
            self.isOpen = True
            
if __name__ == '__main__':
    app = wx.App()
    MainFrame(None, 'NetworkGame')
    app.MainLoop()