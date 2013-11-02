import win32api
import win32con
import win32ui
from SysTray import SysTrayIcon
try:
    import winxpgui as win32gui
except ImportError:
    import win32gui

if __name__ == '__main__':
    import itertools, glob
    
    icons = itertools.cycle(glob.glob('*.ico'))
    hover_text = "Scrni - a0.1"

    def switch_icon(sysTrayIcon, index=None):

        if index == None:
            sysTrayIcon.icon = icons.next()
        else:
            sysTrayIcon.icon = icons[index]
        
        sysTrayIcon.refresh_icon()

    def caputre_window(sysTrayIcon):
        wDC = win32gui.GetWindowDC(win32gui.GetForegroundWindow())
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
        dataBitMap.SaveBitmapFile(cDC, "img.bmp")

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
        dataBitMap.SaveBitmapFile(cDC, "img.bmp")

    def caputre_region(sysTrayIcon):
        print ("wubba")

    menu_options = (('Capture Current Window', None, caputre_window),
                    ('Capture Current Desktop', None, caputre_desktop),
                    ('Capture Current Area', None, caputre_region)
                   )
    
    SysTrayIcon(icons.next(), hover_text, menu_options, default_menu_index=1)