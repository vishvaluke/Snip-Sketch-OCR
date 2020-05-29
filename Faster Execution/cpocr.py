from multiprocessing import Process
from pyperclip import copy
def mino():
    import ctypes
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    copy('')
def starto():
    from os import system
    system('explorer ms-screenclip:')  
def runo():
    from PIL import ImageGrab as ig
    img= ig.grabclipboard()
    i=0
    from time import sleep
    while (img==None):
        i+=1
        sleep(1)
        img= ig.grabclipboard()
        if i>9:
            exit()
    img= ig.grabclipboard()
    img=img.convert('RGB')
    img.save('paste.png','PNG')
    import cv2
    
    img= cv2.imread('paste.png')
    grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    img = cv2.resize(th, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    #img = cv2.GaussianBlur(img, (5, 5), 0)
    img=cv2.bilateralFilter(img,9,75,75)
    cv2.imshow('Results',img)
    cv2.waitKey(0)
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd ='Tesseract-OCR/tesseract.exe'
    text=pytesseract.image_to_string(img)
    print(text)
    copy(text)

if __name__ == '__main__':
    p1=Process(target=starto)
    p1.start()
    p2=Process(target=mino)
    p2.start()
    p1.join()
    p2.join()
    runo()
