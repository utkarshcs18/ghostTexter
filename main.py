from dotenv import load_dotenv
load_dotenv()

import pydirectinput
import pyautogui
import pyperclip
import time
import os
from google import genai


pydirectinput.FAILSAFE = False
pyautogui.FAILSAFE = False

WHATSAPP_ICON = (1246, 1050)
CHAT_START = (541, 169)
CHAT_END = (1828, 918)
INPUT_BOX = (634, 970)   
SEND_BUTTON = (1868, 968)

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

def load_context():
    with open("profile.txt", "r", encoding="utf-8") as f:
        profile = f.read()
    with open("chat.txt", "r", encoding="utf-8") as f:
        examples = f.read()
    return profile, examples

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

def capture_chat():
    pyautogui.click(*WHATSAPP_ICON)
    time.sleep(2)
    drag_select(CHAT_START, CHAT_END)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('c')
    pydirectinput.keyUp('ctrl')
    time.sleep(0.3)
    pyautogui.click(*INPUT_BOX)
    time.sleep(0.3)
    return pyperclip.paste()

def generate_reply(chat_text, profile, examples):
    prompt = f"""You are texting as this person. Stay fully in character.

PERSON PROFILE:
{profile}

EXAMPLES OF HOW THEY TEXT:
{examples}

CHAT HISTORY (most recent messages, respond to the latest one):
{chat_text}

Write ONLY the next reply message, in their exact texting style.
No explanations, no quotes, just the message text."""

    response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
    )
    
    return response.text.strip()

def send_reply(text):
    pyautogui.click(*INPUT_BOX)
    time.sleep(0.3)
    pyperclip.copy(text)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')
    time.sleep(0.3)
    pyautogui.click(*SEND_BUTTON)

if __name__ == "__main__":
    profile, examples = load_context()
    chat_text = capture_chat()
    print("Captured chat:\n", chat_text)

    reply = generate_reply(chat_text, profile, examples)
    print("Generated reply:\n", reply)

    send_reply(reply)
    print("Sent.")