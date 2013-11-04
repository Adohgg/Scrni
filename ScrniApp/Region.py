import wx
import Scrni

class Selection(wx.Frame):

    c1 = None
    c2 = None

    def __init__(self):
        super(Selection, self).__init__(None)

        self.img = Scrni.ImageHandle();

        self.panel = wx.Panel(self, size=self.GetSize())
        self.SetTransparent(10)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.panel.Bind(wx.EVT_MOTION, self.OnMouseMove)
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.panel.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
    def OnEraseBackground(self, event):
        pass # do nothing
    def OnKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_ESCAPE:
            self.Close()
        else:
            event.Skip()
    def OnMouseMove(self, event):
        if event.Dragging() and event.LeftIsDown():
            self.c2 = event.GetPosition()
            self.Refresh()

    def OnMouseDown(self, event):
        self.c1 = event.GetPosition()

    def OnMouseUp(self, event):
        self.Hide()
        self.img.capture_region(self.c1, self.c2)

    def OnPaint(self, event):
        if self.c1 is None or self.c2 is None: return

        dc = wx.PaintDC(self.panel)
        dc.CrossHair(self.c2.x, self.c2.y)
        dc.SetPen(wx.Pen('black', 2))
        dc.SetBrush(wx.Brush(wx.Color(0, 0, 0), wx.TRANSPARENT))

        dc.DrawRectangle(self.c1.x, self.c1.y, self.c2.x - self.c1.x, self.c2.y - self.c1.y)
