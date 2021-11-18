import pyautogui,time,pywhatkit

pywhatkit.sendwhatmsg("+237657546685","salut je suis jarvis!",00,23)
time.sleep(5)
for i in range(2):
    pyautogui.write("je vous aime >>")
    pyautogui.press('enter')
