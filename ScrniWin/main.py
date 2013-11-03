import win32api
import win32con
import win32ui
from SysTray import SysTrayIcon
import UploadProgress
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
try:
    import winxpgui as win32gui
except ImportError:
    import win32gui

lastUnqiueWindow = None;

if __name__ == '__main__':
    import itertools, glob
    
    icons = itertools.cycle(glob.glob('*.ico'))
    hover_text = "Scrni - a0.1"

    currWindow = win32gui.GetForegroundWindow()

    if currWindow != lastUnqiueWindow:
        lastUnqiueWindow = currWindow

    def switch_icon(sysTrayIcon, index=None):

        if index == None:
            sysTrayIcon.icon = icons.next()
        else:
            sysTrayIcon.icon = icons[index]
        
        sysTrayIcon.refresh_icon()

    def caputre_window(sysTrayIcon):
        wDC = win32gui.GetWindowDC(lastUnqiueWindow)
        rect = win32gui.GetWindowRect(lastUnqiueWindow)
        l = rect[0]
        t = rect[1]
        w = rect[2] - l
        h = rect[3] - t
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, "temp.png")

        register_openers()
        datagen, headers = multipart_encode({"img": open("temp.png", "rb")})
        request = urllib2.Request("http://162.243.65.219/upload_image.php", datagen, headers)
        print urllib2.urlopen(request).read()

        #prog = UploadProgress.Progress();
        #stream = UploadProgress.file_with_callback("temp.png", 'rb', prog.update, "File")
        #req = urllib2.Request("http://162.243.65.219/upload_image.php", stream)
        #print urllib2.urlopen(req).read()


    def caputre_desktop(sysTrayIcon):
        wDC = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
        w = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        h = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        l = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        t = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(w, h) , dcObj, (l,t), win32con.SRCCOPY)
        
        dataBitMap.SaveBitmapFile(cDC, i.strftime('%Y/%m/%dat%H:%M:%S.png'))

    def caputre_region(sysTrayIcon):
        print (time.strftime("%x at %X.bmp"))

    menu_options = (('Capture Current Window', None, caputre_window),
                    ('Capture Current Desktop', None, caputre_desktop),
                    ('Capture Current Area', None, caputre_region)
                   )
    
    SysTrayIcon(icons.next(), hover_text, menu_options, default_menu_index=1)