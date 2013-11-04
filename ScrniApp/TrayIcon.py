import wx
import Scrni

TRAY_TOOLTIP = 'Scrni'
TRAY_ICON = 'icon.ico'

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item

class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()

        self.img = Scrni.ImageHandle();

        self.set_icon(TRAY_ICON)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.img.select_region)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        #create_menu_item(menu, 'Capture Current Window', self.capture_window)
        create_menu_item(menu, 'Capture Desktop', self.img.capture_desktop)
        create_menu_item(menu, 'Capture Region', self.img.select_region)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
