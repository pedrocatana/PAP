import subprocess
import time
import pyautogui
import os

os.system("start chrome.exe --start-maximized --start-fullscreen  --new-window https://www.valdorio.net/images/pdfs/20222023_Calendario_EE_v01.pdf")
time.sleep(1)
pyautogui.press("tab",presses=10)
pyautogui.press(["enter","down","down","down","enter"])
os.system("start chrome.exe --new-window https://apphorarios.pt/assets/TETO22.png")
time.sleep(1)
pyautogui.press("F11")
pyautogui.keyDown("win")
pyautogui.press("left")
pyautogui.press("left")
pyautogui.keyUp("win")
os.system("start chrome.exe --new-window https://apphorarios.pt/assets/TETO21.png")
time.sleep(1)
pyautogui.press("F11")
pyautogui.keyDown("win")
pyautogui.press("left")
pyautogui.keyUp("win")
os.system("start chrome.exe --new-window https://apphorarios.pt/assets/TETO20.png")
time.sleep(1)
pyautogui.press("F11")
pyautogui.keyDown("win")
pyautogui.press("left")
pyautogui.press("left")
pyautogui.keyUp("win")
os.system("start chrome.exe --new-window https://valdorio.net")
time.sleep(1)
pyautogui.press("F11")
pyautogui.keyDown("win")
pyautogui.press("left")
pyautogui.keyUp("win")
time.sleep(30)
pyautogui.keyDown("ctrl")
pyautogui.press("w")
pyautogui.press("w")
pyautogui.press("w")
pyautogui.press("w")
pyautogui.press("w")
pyautogui.keyUp("ctrl")
