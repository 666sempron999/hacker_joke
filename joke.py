import sys
import time
import win32gui, win32con


if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk


def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()


def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        # print (hex(hwnd), win32gui.GetWindowText( hwnd ))
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)


if __name__ == '__main__':
    time.sleep(3)
    win32gui.EnumWindows( winEnumHandler, None )
    time.sleep(1)
    pilImage = Image.open("1.png")
    showPIL(pilImage)