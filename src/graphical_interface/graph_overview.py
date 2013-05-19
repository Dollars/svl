# -*-coding:Utf-8 -*
import wx
import random

class GraphOverview(wx.Frame):
    def __init__(self, parent=None, id=-1, title=None):
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self, size=(500, 500))
        self.panel.Bind(wx.EVT_PAINT, self.graph_overview)

        self.Fit()
                
    def graph_overview(self, event):
        #LINES = PIPES, CIRCLE = NODES, RECTANGLE = VALVES
        dc = wx.PaintDC(self.panel)
        dotFilePath = "../../input/myNetwork.dot"
        lecture = open(dotFilePath, "r")
        x=5
        y=5 
        r=5
        for i in lecture:
            dc.SetPen(wx.Pen('red', 1))
            dc.SetBrush(wx.Brush('yellow'))

            x=x+60
            y=5
            lineNodes = i[:-2].split(" ")
            charA = lineNodes.pop(0)
            dc.DrawText(charA, x, y)
            dc.DrawCircle(x, y, r)
            savex=x
            savey=y
            y=y+30
            
            for pipeInfo, nodeID in zip(lineNodes[0::2], lineNodes[1::2]):
                charB = nodeID
                dc.SetPen(wx.Pen('red', 1))
                dc.SetBrush(wx.Brush('yellow'))

                dc.DrawCircle(x, y, r)
                dc.DrawLine(savex, savey, x, y)
                y=y+30

                if pipeInfo[0] == "|":
                    dc.SetPen(wx.Pen('blue', 1))
                    dc.SetBrush(wx.Brush('green'))
                                        
                    rect = wx.Rect(savex, savey, 10, 10)
                    dc.DrawRoundedRectangleRect(rect, 1)
                if pipeInfo[1] == "|" :
                    dc.SetPen(wx.Pen('blue', 1))
                    dc.SetBrush(wx.Brush('green'))

                    rect = wx.Rect(x, y-30, 10, 10)
                    dc.DrawRoundedRectangleRect(rect, 1)
                dc.DrawText(charB, x, y-30)

        lecture.close

app = wx.PySimpleApp()
frame1 = GraphOverview(title='Overview the sequences in myNetwork.dot')
frame1.Center()
frame1.Show()
app.MainLoop()

