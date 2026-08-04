import pydirectinput
import pyautogui
import pyperclip
import time

pydirectinput.FAILSAFE = True

def drag_select(start, end, steps=40, step_delay=0.02):
    pydirectinput.moveTo(*start)
    time.sleep(0.2)
    pydirectinput.mouseDown()
    time.sleep(0.1)

    for i in range(1, steps + 1):
        x = start[0] + (end[0] - start[0]) * i / steps
        y = start[1] + (end[1] - start[1]) * i / steps
        pydirectinput.moveTo(int(x), int(y))
        time.sleep(step_delay)

    pydirectinput.mouseUp()
    time.sleep(0.3)

# Open WhatsApp
pyautogui.click(1246, 1050)
time.sleep(2)

# Select chat text
drag_select((541, 169), (1828, 918))

# Copy to clipboard
pydirectinput.keyDown('ctrl')
pydirectinput.press('c')
pydirectinput.keyUp('ctrl')
time.sleep(0.3)

pyautogui.click(634,970)

copied_text = pyperclip.paste()
print("Copied text:")
print(copied_text)