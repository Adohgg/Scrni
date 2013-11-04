import wx
import pyscreenshot as ImageGrab
import urllib2
import Region
import TrayIcon
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

class ImageHandle():

    def capture_desktop(self, event):
        im=ImageGrab.grab_to_file("temp.png")
        self.post_image()

    def select_region(self, event):
        sel = Region.Selection()
        sel.ShowFullScreen(True)

    def capture_region(self, c1, c2):
        p1, p2 = self.fixCoords(c1, c2)
        print "Point 1 (" + str(p1.x) + "," + str(p1.y) + ")"
        print "Point 2 (" + str(p2.x) + "," + str(p2.y) + ")"
        im=ImageGrab.grab(bbox=(p1.x, p1.y, p2.x - p1.x, p2.y - p1.y)).save("temp.png")
        self.post_image()

    def post_image(self):
        register_openers()
        datagen, headers = multipart_encode({"img": open("temp.png", "rb")})
        request = urllib2.Request("http://162.243.65.219/upload_image.php", datagen, headers)
        print urllib2.urlopen(request).read()

    def fixCoords(self, c1, c2):
        p1 = wx.Point(0, 0)
        p2 = wx.Point(0, 0)

        p1.x = min(c1.x, c2.x)
        p1.y = min(c1.y, c2.y)
        p2.x = max(c1.x, c2.x)
        p2.y = max(c1.y, c2.y)

        return p1, p2

#
# main
#

def main():
    app = wx.PySimpleApp()
    TrayIcon.TaskBarIcon()
    app.MainLoop()

if __name__ == '__main__':
    main()