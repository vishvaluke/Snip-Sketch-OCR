from PIL import ImageGrab as ig
from PIL import Image as iqo
import pytesseract,pyperclip,cv2,time,ctypes,webbrowser,wx,os
import numpy as np
def snap():
    #ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    time.sleep(1)
    pyperclip.copy('')
    os.system('explorer ms-screenclip:')
    img=ig.grabclipboard()
    i=0
    while img==None:
        i=i+1
        time.sleep(1)
        img=ig.grabclipboard()
        if i>9:
            exit()
    main()
def todo(x,text):
    if (x == 'Copy'):
        pyperclip.copy(text)
    elif (x=='Notepad'):
        f=open('copied.txt','w',encoding='utf-8')
        f.write(text)
        f.close()
        webbrowser.open('copied.txt')
    elif (x=='Exit'):
        exit()
def quit_loop(text):
    class Example(wx.Frame): 
            
        def __init__(self, parent, title): 
            super(Example, self).__init__(parent, title = title,size = (200,200)) 
            self.InitUI() 
        def InitUI(self):    
            pnl = wx.Panel(self) 
            self.cb1 = wx.CheckBox(pnl, label = 'Copy',pos = (10,10)) 
            self.cb2 = wx.CheckBox(pnl, label = 'Notepad',pos = (10,40)) 
            self.cb3 = wx.CheckBox(pnl, label = 'Exit',pos = (10,70)) 
            self.Bind(wx.EVT_CHECKBOX,self.onChecked) 
            self.Centre() 
            self.Show(True) 
        def onChecked(self, e): 
            cb = e.GetEventObject() 
            print (cb.GetLabel(),' is clicked',cb.GetValue())
            x=cb.GetLabel()
            todo(x,text)
  
    ex= wx.App() 
    Example(None,'CheckBox') 
    ex.MainLoop()
def main():
    img=ig.grabclipboard()
    img=np.array(img)
    img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img=iqo.fromarray(img,'RGB')
    img.save('paste.png','PNG')
    img= cv2.imread('paste.png')
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    text=pytesseract.image_to_string(th)
    os.remove('paste.png')
    quit_loop(text)
snap()
