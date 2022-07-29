import os
import subprocess as sp
import pyautogui

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'discord': "C:\\Users\\ibtih\\AppData\\Local\\Discord\\app-1.0.9005\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_notepad():
    sp.Popen(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])


def screenshot() -> None:
    img = pyautogui.screenshot()
    img.save('C:/Users/ibtih/OneDrive/Bureau/here/screenshot.png')