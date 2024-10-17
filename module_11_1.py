
'''
    pyautogui совместно с Pillow
    позволяет получать цвет пикселя
    по координатам на экране
'''

def getPixelForPython(x,y):
    import os

    try:
        import pyautogui
    except:
        os.system('pip install pyautogui')
        import pyautogui

    try:
        screenshot = pyautogui.screenshot()
    except:
        os.system('pip install Pillow')
        screenshot = pyautogui.screenshot()

    color = screenshot.getpixel((x, y))
    return color

#print(getPixelForPython(50,50))



'''
    subprocess совместно с Popen
    позволяет запускать exe
    либо открывать web страницу по адресу
'''

def shellExecuteForPython(pathToExec):
    import os
    try:
        import subprocess
    except:
        os.system('pip install subprocess')
        import subprocess

    if pathToExec[0:6] != 'https:':
        txt = pathToExec.replace('\\','@')
        pathToExec = txt.replace('@','\\')
    subprocess.Popen(['start', pathToExec], shell=True)

#shellExecuteForPython('https://mail.ru/')
#shellExecuteForPython('c:\\Windows\\System32\\calc.exe')