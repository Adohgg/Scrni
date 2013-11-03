import wx
import pyscreenshot as ImageGrab
import urllib2
import Region
import TrayIcon
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

frame = None

class ImageHandle():

    def capture_desktop(self, event):
        im=ImageGrab.grab_to_file("temp.png")
        self.post_image()

    def select_region(self, event):
        frame.reset()
        frame.show()

    def capture_region(c1, c2):
        im=ImageGrab.grab(bbox=(c1.x, c1.y, c2.x - c1.x, c2.y - c1.y)).save("temp.png")
        self.post_image()

    def post_image():
        register_openers()
        datagen, headers = multipart_encode({"img": open("temp.png", "rb")})
        request = urllib2.Request("http://162.243.65.219/upload_image.php", datagen, headers)
        print urllib2.urlopen(request).read()

#
# main
#

def main():
    app = wx.PySimpleApp()
    TrayIcon.TaskBarIcon()
    frame = Region.Selection()
    frame.ShowFullScreen(True)
    frame.Hide()
    app.MainLoop()

if __name__ == '__main__':
    main()