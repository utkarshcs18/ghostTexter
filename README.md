# GhostTexter

GhostTexter is an automated, AI-powered WhatsApp auto-responder. It uses computer vision/GUI automation (`pyautogui` & `pydirectinput`) to capture incoming messages from your WhatsApp screen and generates contextual, personality-driven replies using the Google Gemini AI API. It then automatically types and sends the message for you.

## Features

- **Automated Chat Capture**: Uses GUI automation to copy the latest messages from WhatsApp.
- **AI-Powered Replies**: Uses Google's Gemini 3.5 Flash model to generate intelligent responses.
- **Personality Mimicry**: Tailor the AI's texting style using `profile.txt` and `chat.txt` to sound exactly like you (or any persona you choose).
- **Rich Console UI**: Uses `rich` to provide a visually pleasing status output in the terminal.

## Prerequisites

- Python 3.x
- Google Gemini API Key
- WhatsApp Desktop or WhatsApp Web open on your screen

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd ghostTexter
   ```

2. Install the required Python packages:
   ```bash
   pip install pydirectinput pyautogui pyperclip python-dotenv google-genai rich
   ```

3. Create a `.env` file in the root directory and add your Google API Key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Configuration

Because GhostTexter relies on screen coordinates to interact with WhatsApp, you must configure the exact pixel locations for your specific monitor setup.

### 1. Find Your Screen Coordinates
You can use the provided script in `setup.txt` to find the exact X, Y coordinates of your mouse on the screen. Run a simple python script with:
```python
import pyautogui
while True:
    print(pyautogui.position())
```
Hover over the necessary elements in WhatsApp to find their coordinates.

### 2. Update `main.py`
Open `main.py` and update the following variables with your screen's specific coordinates:
- `WHATSAPP_ICON`: Coordinate to click on the WhatsApp window/icon to focus it.
- `CHAT_START`: The top-left coordinate to start selecting the chat history.
- `CHAT_END`: The bottom-right coordinate to end selecting the chat history.
- `INPUT_BOX`: Coordinate of the text input box where messages are typed.
- `SEND_BUTTON`: Coordinate of the send button.

### 3. Customize Your AI Persona
- **`profile.txt`**: Define the personality, tone, and rules the AI should follow when generating replies (e.g., "Sarcastic, short sentences, Hinglish").
- **`chat.txt`**: Provide some example messages to give the AI context on how you typically text.

## Usage

1. Ensure WhatsApp is visible on your screen and open to the chat you want to respond to.
2. Run the script:
   ```bash
   python main.py
   ```
3. Do not move your mouse! The script will take control to highlight the chat, copy it, generate a reply, and send it automatically.

## Disclaimer

This tool uses mouse and keyboard automation. Ensure you do not interfere with the mouse while the script is running. Use responsibly and in accordance with WhatsApp's terms of service.
