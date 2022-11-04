import time
import pyautogui
import pyperclip

pyautogui.PAUSE = 2

while True:  # Strat loop

    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.write('https://www.instagram.com')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('enter')
    time.sleep(4)


    arquivo_em_tela = pyperclip.paste()

    if arquivo_em_tela != "https://www.instagram.com/":
        pyautogui.hotkey('alt', 'f4')
        time.sleep(6)
    else:
        pyautogui.press('space')
        pyautogui.click(x=96, y=394)
        time.sleep(4)
        pyautogui.click(x=1320, y=650)
        pyautogui.write('siqueiramt_')
        pyautogui.click(x=1097, y=370)
        pyautogui.write('jonatasviolonista')
        pyautogui.click(x=1100, y=404)
        pyautogui.click(x=1098, y=257)
        time.sleep(2)
        pyautogui.write('Meus Camaradas!')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'w')



