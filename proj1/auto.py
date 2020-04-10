import pyautogui
import time

pages = 108
unit = "8"
# Point(x=1327, y=387) Point(x=726, y=748)
time.sleep(4)
for i in range(1, pages // 2):
    print(pyautogui.position())
    pyautogui.moveTo(1327, 387)
    pyautogui.press('printscreen')
    pyautogui.click(None, None, 1)
    time.sleep(3)

pyautogui.press('esc')
pyautogui.hotkey('ctrl', 'alt', 't')
pyautogui.write('cd Pictures/')
pyautogui.press('enter')
pyautogui.write('mkdir ' + unit, interval=0.25)
pyautogui.press('enter')
pyautogui.write('mv *png ./' + unit + '/', interval=0.25)
pyautogui.press('enter')
pyautogui.hotkey('win', 'shift', 'q')
time.sleep(4)
pyautogui.hotkey('ctrl', 'shift', 'q')
pyautogui.hotkey('ctrl', 'shift', 'n')

